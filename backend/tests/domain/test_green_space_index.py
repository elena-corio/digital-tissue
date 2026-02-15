from unittest.mock import patch
import pytest
from domain.metrics.green_space_index import (
    is_green_program,
    get_level_gap_to_nearest_green,
    get_distance_range_entry,
    calculate_green_space_index,
    calculate_green_space_index_avg,
    calculate_green_space_index_per_level,
    calculate_green_space_index_per_cluster,
    calculate_distance_range_percentages,
    get_green_space_index_metric
)
from domain.model.enum import ProgramType
from domain.model.elements import OpenSpace, Unit


@pytest.fixture
def mock_rulebook():
    """Create mock rulebook data."""
    return {
        "program_types": {
            "Living": {"is_green": False},
            "Working": {"is_green": False},
            "Community": {"is_green": True},
            "Circulation": {"is_green": False}
        },
        "green_index_score": [
            {"max_gap": 5, "score": 1.0},
            {"max_gap": 10, "score": 0.8},
            {"max_gap": 20, "score": 0.5},
            {"max_gap": 50, "score": 0.2},
            {"max_gap": 100, "score": 0.0}
        ]
    }


@pytest.fixture
def mock_residential_units():
    """Create mock residential unit data."""
    return [
        Unit(cluster_id="1", speckle_type="unit", geometry=None, name=ProgramType.LIVING, area=100.0, level=1),
        Unit(cluster_id="1", speckle_type="unit", geometry=None, name=ProgramType.LIVING, area=120.0, level=2),
        Unit(cluster_id="2", speckle_type="unit", geometry=None, name=ProgramType.LIVING, area=90.0, level=5),
    ]


@pytest.fixture
def mock_green_units():
    """Create mock green space unit data."""
    return [
        Unit(cluster_id="1", speckle_type="unit", geometry=None, name=ProgramType.COMMUNITY, area=50.0, level=0),
        Unit(cluster_id="2", speckle_type="unit", geometry=None, name=ProgramType.COMMUNITY, area=60.0, level=4),
    ]


def test_is_green_program(mock_rulebook):
    """Test checking if a program type is green."""
    assert is_green_program(ProgramType.COMMUNITY, mock_rulebook) is True
    assert is_green_program(ProgramType.LIVING, mock_rulebook) is False
    assert is_green_program(ProgramType.WORKING, mock_rulebook) is False


def test_get_level_gap_to_nearest_green(mock_residential_units, mock_green_units):
    """Test level gap calculation."""
    # Residential at level 1, green at 0 and 4 -> gap = 1
    gap = get_level_gap_to_nearest_green(mock_residential_units[0], mock_green_units)
    assert gap == 1.0


def test_get_level_gap_to_nearest_green_no_green(mock_residential_units):
    """Test level gap with no green spaces."""
    gap = get_level_gap_to_nearest_green(mock_residential_units[0], [])
    assert gap == 100.0


def test_get_distance_range_entry(mock_rulebook):
    """Test distance range entry lookup."""
    # Gap 3 should fall in 0-5 range
    entry = get_distance_range_entry(3.0, mock_rulebook)
    assert entry["max_gap"] == 5
    assert entry["score"] == 1.0
    
    # Gap 15 should fall in 0-20 range
    entry = get_distance_range_entry(15.0, mock_rulebook)
    assert entry["max_gap"] == 20
    assert entry["score"] == 0.5
    
    # Gap 150 should return None (exceeds all ranges)
    entry = get_distance_range_entry(150.0, mock_rulebook)
    assert entry is None


def test_calculate_green_space_index(mock_residential_units, mock_green_units, mock_rulebook):
    """Test green space index calculation returns score and range."""
    # Unit at level 1, green at level 0 -> gap = 1 -> score = 1.0, range = "0-5"
    score, range_key = calculate_green_space_index(mock_residential_units[0], mock_green_units, mock_rulebook)
    assert score == 1.0
    assert range_key == "<5"


def test_calculate_green_space_index_different_ranges(mock_green_units, mock_rulebook):
    """Test index calculation for different gap ranges."""
    # Green units at level 0 and 4
    # Unit at level 12: nearest green at 4, gap = 8 -> score = 0.8, range = "0-10"
    unit = Unit(cluster_id="1", speckle_type="unit", geometry=None, name=ProgramType.LIVING, area=100.0, level=12)
    score, range_key = calculate_green_space_index(unit, mock_green_units, mock_rulebook)
    assert score == 0.8
    assert range_key == "<10"


def test_calculate_green_space_index_avg(mock_residential_units, mock_green_units, mock_rulebook):
    """Test average calculation and range counts."""
    avg_score, range_counts = calculate_green_space_index_avg(mock_residential_units, mock_green_units, mock_rulebook)
    
    # Unit 0: gap=1 (0-5, score=1.0)
    # Unit 1: gap=2 (0-5, score=1.0)
    # Unit 2: gap=1 (0-5, score=1.0)
    # Average = 3.0 / 3 = 1.0
    assert avg_score == 1.0
    assert range_counts["<5"] == 3
    assert range_counts["<10"] == 0


def test_calculate_green_space_index_avg_empty_list(mock_green_units, mock_rulebook):
    """Test with empty units list."""
    avg_score, range_counts = calculate_green_space_index_avg([], mock_green_units, mock_rulebook)
    assert avg_score == 0.0
    assert all(count == 0 for count in range_counts.values())


def test_calculate_green_space_index_per_level(mock_residential_units, mock_green_units, mock_rulebook):
    """Test per-level calculation."""
    levels = [1, 2, 5]
    result = calculate_green_space_index_per_level(mock_residential_units, mock_green_units, levels, mock_rulebook)
    
    assert len(result) == 3
    assert result[1] == 1.0  # gap=1, score=1.0
    assert result[2] == 1.0  # gap=2, score=1.0
    assert result[5] == 1.0  # gap=1, score=1.0


def test_calculate_green_space_index_per_level_empty_level(mock_residential_units, mock_green_units, mock_rulebook):
    """Test per-level with missing levels."""
    levels = [1, 2, 3, 5]  # Level 3 doesn't exist
    result = calculate_green_space_index_per_level(mock_residential_units, mock_green_units, levels, mock_rulebook)
    
    assert len(result) == 3  # Only levels with units
    assert 3 not in result


def test_calculate_green_space_index_per_cluster(mock_residential_units, mock_green_units, mock_rulebook):
    """Test per-cluster calculation."""
    clusters = ["1", "2"]
    result = calculate_green_space_index_per_cluster(mock_residential_units, mock_green_units, clusters, mock_rulebook)
    
    assert len(result) == 2
    assert result["1"] == 1.0  # 2 units at level 1,2 with gaps 1,2 -> avg = 1.0
    assert result["2"] == 1.0  # 1 unit at level 5 with gap 1 -> score = 1.0


def test_calculate_green_space_index_per_cluster_empty_cluster(mock_residential_units, mock_green_units, mock_rulebook):
    """Test per-cluster with missing clusters."""
    clusters = ["1", "2", "3"]  # Cluster 3 doesn't exist
    result = calculate_green_space_index_per_cluster(mock_residential_units, mock_green_units, clusters, mock_rulebook)
    
    assert len(result) == 2
    assert "3" not in result


def test_calculate_distance_range_percentages():
    """Test conversion of counts to percentages."""
    range_counts = {"<5": 10, "<10": 5, "<20": 5}
    percentages = calculate_distance_range_percentages(range_counts)
    
    assert percentages["<5"] == 50.0
    assert percentages["<10"] == 25.0
    assert percentages["<20"] == 25.0


def test_calculate_distance_range_percentages_empty():
    """Test percentages with zero counts."""
    range_counts = {"<5": 0, "<10": 0}
    percentages = calculate_distance_range_percentages(range_counts)
    
    assert percentages["<5"] == 0.0
    assert percentages["<10"] == 0.0


def test_calculate_distance_range_percentages_single_range():
    """Test percentages with single range."""
    range_counts = {"<5": 20}
    percentages = calculate_distance_range_percentages(range_counts)
    
    assert percentages["<5"] == 100.0


@patch("domain.green_space_index.METRICS", {
    "Green Space Index": {"benchmark": 0.8, "action": "Increase proximity to green spaces"}
})
@patch("domain.green_space_index.RULEBOOK", {
    "program_types": {
        "Living": {"is_green": False},
        "Working": {"is_green": False},
        "Community": {"is_green": True},
    },
    "green_index_score": [
        {"max_gap": 5, "score": 1.0},
        {"max_gap": 10, "score": 0.8},
        {"max_gap": 20, "score": 0.5},
        {"max_gap": 50, "score": 0.2},
        {"max_gap": 100, "score": 0.0}
    ]
})
def test_get_green_space_index_metric():
    """Test complete metric generation."""
    units = [
        Unit(cluster_id="1", speckle_type="unit", geometry=None, name=ProgramType.LIVING, area=100.0, level=1),
        Unit(cluster_id="1", speckle_type="unit", geometry=None, name=ProgramType.COMMUNITY, area=50.0, level=0),
        Unit(cluster_id="2", speckle_type="unit", geometry=None, name=ProgramType.WORKING, area=80.0, level=5),
    ]
    green_spaces = [OpenSpace(cluster_id="1", speckle_type="open_space", geometry=None, area=50.0, level=0)]
    levels = [1, 5]
    clusters = ["1", "2"]
    
    result = get_green_space_index_metric(units, green_spaces, levels, clusters)
    
    assert result.name == "Green Space Index"
    assert result.benchmark == 0.8
    assert result.total_value == 1.0  # Only LIVING has gap 1
    assert len(result.value_per_level) == 1  # Only level 1 has residential
    assert len(result.value_per_cluster) == 1  # Only cluster 1 has residential
    assert result.action == "Increase proximity to green spaces"
    assert result.chart_data is not None
    assert result.chart_data.label == "Green Space Distance Distribution"
    assert result.chart_data.values.get("<5") == 100.0  # All units in 0-5 range


@patch("domain.green_space_index.METRICS", {
    "Green Space Index": {"benchmark": 0.8, "action": "Test"}
})
@patch("domain.green_space_index.RULEBOOK", {
    "program_types": {
        "Living": {"is_green": False},
        "Community": {"is_green": True},
    },
    "green_index_score": [
        {"max_gap": 5, "score": 1.0},
        {"max_gap": 100, "score": 0.0}
    ]
})
def test_get_green_space_index_metric_no_residential():
    """Test metric with no residential units."""
    units = [
        Unit(cluster_id="1", speckle_type="unit", geometry=None, name=ProgramType.COMMUNITY, area=50.0, level=0),
    ]
    green_spaces = [OpenSpace(cluster_id="1", speckle_type="open_space", geometry=None, area=100.0, level=0)]
    levels = [1]
    clusters = ["1"]
    
    result = get_green_space_index_metric(units, green_spaces, levels, clusters)
    
    assert result.value_per_level == {}
    assert result.value_per_cluster == {"1": 1.0}  # COMMUNITY is residential and green with gap=0, score=1.0
