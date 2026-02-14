from unittest.mock import patch
import pytest
from domain.green_space_index import (
    is_green_program,
    calculate_green_space_index,
    calculate_green_space_index_avg,
    calculate_green_space_index_per_level,
    calculate_green_space_index_per_cluster,
    get_green_space_index_metric
)
from domain.model.enum import ProgramType
from domain.model.model import Unit


@pytest.fixture
def mock_rulebook():
    """Create mock rulebook data."""
    return {
        "program_types": {
            "Living": {"is_green": False, "is_service": False},
            "Working": {"is_green": False, "is_service": False},
            "Community": {"is_green": True, "is_service": False},
            "Circulation": {"is_green": False, "is_service": True}
        }
    }


@pytest.fixture
def mock_residential_units():
    """Create mock residential unit data."""
    return [
        Unit(
            cluster_id="1",
            speckle_type="unit",
            geometry=None,
            name=ProgramType.LIVING,
            area=100.0,
            level=1
        ),
        Unit(
            cluster_id="1",
            speckle_type="unit",
            geometry=None,
            name=ProgramType.LIVING,
            area=120.0,
            level=2
        ),
        Unit(
            cluster_id="2",
            speckle_type="unit",
            geometry=None,
            name=ProgramType.LIVING,
            area=90.0,
            level=5
        ),
    ]


@pytest.fixture
def mock_green_units():
    """Create mock green space unit data."""
    return [
        Unit(
            cluster_id="1",
            speckle_type="unit",
            geometry=None,
            name=ProgramType.COMMUNITY,
            area=50.0,
            level=0
        ),
        Unit(
            cluster_id="2",
            speckle_type="unit",
            geometry=None,
            name=ProgramType.COMMUNITY,
            area=60.0,
            level=4
        ),
    ]


def test_is_green_program(mock_rulebook):
    """Test checking if a program type is green."""
    assert is_green_program(ProgramType.COMMUNITY, mock_rulebook) is True
    assert is_green_program(ProgramType.LIVING, mock_rulebook) is False
    assert is_green_program(ProgramType.WORKING, mock_rulebook) is False


def test_calculate_green_space_index_closest_green(mock_residential_units, mock_green_units):
    """Test calculation finds the closest green space."""
    # Residential unit at level 1, green spaces at level 0 and 4
    # Should find level 0 (gap = 1)
    result = calculate_green_space_index(mock_residential_units[0], mock_green_units)
    assert result == 1.0


def test_calculate_green_space_index_higher_level(mock_residential_units, mock_green_units):
    """Test calculation with residential unit at higher level."""
    # Residential unit at level 5, green spaces at level 0 and 4
    # Should find level 4 (gap = 1)
    result = calculate_green_space_index(mock_residential_units[2], mock_green_units)
    assert result == 1.0


def test_calculate_green_space_index_middle_level(mock_residential_units, mock_green_units):
    """Test calculation with residential unit between green spaces."""
    # Residential unit at level 2, green spaces at level 0 and 4
    # Should find level 0 or level 4 (both gap = 2)
    result = calculate_green_space_index(mock_residential_units[1], mock_green_units)
    assert result == 2.0


def test_calculate_green_space_index_no_green_spaces(mock_residential_units):
    """Test calculation with no green spaces."""
    result = calculate_green_space_index(mock_residential_units[0], [])
    assert result == 100.0  # Default max gap


def test_calculate_green_space_index_same_level():
    """Test calculation when green space is on same level."""
    res_unit = Unit(
        cluster_id="1",
        speckle_type="unit",
        geometry=None,
        name=ProgramType.LIVING,
        area=100.0,
        level=3
    )
    green_unit = Unit(
        cluster_id="1",
        speckle_type="unit",
        geometry=None,
        name=ProgramType.COMMUNITY,
        area=50.0,
        level=3
    )
    result = calculate_green_space_index(res_unit, [green_unit])
    assert result == 0.0


def test_calculate_green_space_index_avg(mock_residential_units, mock_green_units):
    """Test average green space index calculation."""
    result = calculate_green_space_index_avg(mock_residential_units, mock_green_units)
    
    # Unit at level 1: gap = 1
    # Unit at level 2: gap = 2
    # Unit at level 5: gap = 1
    # Average = (1 + 2 + 1) / 3 = 1.333...
    expected = (1.0 + 2.0 + 1.0) / 3
    assert result == pytest.approx(expected, rel=1e-6)


def test_calculate_green_space_index_avg_empty_list():
    """Test average with empty residential units list."""
    result = calculate_green_space_index_avg([], [])
    assert result == 0.0


def test_calculate_green_space_index_per_level(mock_residential_units, mock_green_units):
    """Test green space index calculation per level."""
    levels = [1, 2, 5]
    result = calculate_green_space_index_per_level(mock_residential_units, mock_green_units, levels)
    
    assert len(result) == 3
    assert result[1] == 1.0  # Single unit at level 1, gap = 1
    assert result[2] == 2.0  # Single unit at level 2, gap = 2
    assert result[5] == 1.0  # Single unit at level 5, gap = 1


def test_calculate_green_space_index_per_level_empty_level(mock_residential_units, mock_green_units):
    """Test behavior when a level has no residential units."""
    levels = [1, 2, 3, 5]  # Level 3 has no units
    result = calculate_green_space_index_per_level(mock_residential_units, mock_green_units, levels)
    
    assert len(result) == 3  # Only levels with units
    assert 3 not in result


def test_calculate_green_space_index_per_cluster(mock_residential_units, mock_green_units):
    """Test green space index calculation per cluster."""
    clusters = ["1", "2"]
    result = calculate_green_space_index_per_cluster(mock_residential_units, mock_green_units, clusters)
    
    assert len(result) == 2
    # Cluster 1: units at level 1 and 2, gaps = 1 and 2, average = 1.5
    assert result["1"] == pytest.approx(1.5, rel=1e-6)
    # Cluster 2: unit at level 5, gap = 1
    assert result["2"] == 1.0


def test_calculate_green_space_index_per_cluster_empty_cluster(mock_residential_units, mock_green_units):
    """Test behavior when a cluster has no residential units."""
    clusters = ["1", "2", "3"]  # Cluster 3 has no units
    result = calculate_green_space_index_per_cluster(mock_residential_units, mock_green_units, clusters)
    
    assert len(result) == 2
    assert "3" not in result


@patch("domain.green_space_index.METRICS", {
    "Green Space Index": {
        "benchmark": 2.0,
        "action": "Add more green spaces"
    }
})
@patch("domain.green_space_index.RULEBOOK", {
    "program_types": {
        "Living": {"is_green": False, "is_service": False},
        "Working": {"is_green": False, "is_service": False},
        "Community": {"is_green": True, "is_service": False},
        "Circulation": {"is_green": False, "is_service": True}
    }
})
def test_get_green_space_index_metric():
    """Test the complete metric result generation."""
    units = [
        Unit(
            cluster_id="1",
            speckle_type="unit",
            geometry=None,
            name=ProgramType.LIVING,
            area=100.0,
            level=1
        ),
        Unit(
            cluster_id="1",
            speckle_type="unit",
            geometry=None,
            name=ProgramType.COMMUNITY,
            area=50.0,
            level=0
        ),
        Unit(
            cluster_id="2",
            speckle_type="unit",
            geometry=None,
            name=ProgramType.WORKING,
            area=80.0,
            level=2
        ),
    ]
    levels = [1, 2]
    clusters = ["1", "2"]
    
    result = get_green_space_index_metric(units, levels, clusters)
    
    assert result.name == "Green Space Index"
    assert result.benchmark == 2.0
    # LIVING unit at level 1 (gap=1) + COMMUNITY unit at level 0 (gap=0 to itself) = avg 0.5
    assert result.total_value == 0.5
    assert len(result.value_per_level) == 1  # Only level 1 has LIVING (level 0 COMMUNITY is also residential)
    assert len(result.value_per_cluster) == 1  # Only cluster 1 has residential (LIVING + COMMUNITY)
    assert result.action == "Add more green spaces"


def test_get_green_space_index_metric_filters_residential():
    """Test that only residential units are considered."""
    with patch("domain.green_space_index.METRICS", {
        "Green Space Index": {"benchmark": 2.0, "action": "Test"}
    }), patch("domain.green_space_index.RULEBOOK", {
        "program_types": {
            "Living": {"is_green": False},
            "Working": {"is_green": False},
            "Community": {"is_green": True}
        }
    }):
        units = [
            Unit(
                cluster_id="1",
                speckle_type="unit",
                geometry=None,
                name=ProgramType.WORKING,  # Not residential
                area=100.0,
                level=1
            ),
            Unit(
                cluster_id="1",
                speckle_type="unit",
                geometry=None,
                name=ProgramType.COMMUNITY,  # Green space
                area=50.0,
                level=0
            ),
        ]
        levels = [1]
        clusters = ["1"]
        
        result = get_green_space_index_metric(units, levels, clusters)
        
        # COMMUNITY is considered residential, so we have 1 residential unit
        # But COMMUNITY is also a green space, so gap to itself is 0
        assert result.value_per_level == {}
        assert result.value_per_cluster == {'1': 0.0}  # COMMUNITY at level 0 has gap 0 to itself
        assert result.total_value == 0.0  # Only COMMUNITY which has gap 0
