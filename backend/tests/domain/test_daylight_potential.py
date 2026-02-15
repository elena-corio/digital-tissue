from unittest.mock import patch
import pytest
from domain.daylight_potential import (
    calculate_daylight_potential,
    calculate_daylight_potential_per_level,
    calculate_daylight_potential_per_cluster,
    get_daylight_potential_metric
)
from domain.model.enum import MaterialType, ProgramType
from domain.model.model import Facade, Unit


@pytest.fixture
def mock_facades():
    """Create mock facade data for testing."""
    return [
        Facade(
            cluster_id="1",
            speckle_type="facade",
            geometry=None,
            material=MaterialType.GLASS,
            area=20.0,
            thickness=0.1,
            level=1
        ),
        Facade(
            cluster_id="1",
            speckle_type="facade",
            geometry=None,
            material=MaterialType.CONCRETE,
            area=50.0,
            thickness=0.3,
            level=1
        ),
        Facade(
            cluster_id="2",
            speckle_type="facade",
            geometry=None,
            material=MaterialType.GLASS,
            area=15.0,
            thickness=0.1,
            level=2
        ),
    ]


@pytest.fixture
def mock_units():
    """Create mock unit data for testing."""
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
            cluster_id="2",
            speckle_type="unit",
            geometry=None,
            name=ProgramType.WORKING,
            area=80.0,
            level=2
        ),
    ]


def test_calculate_daylight_potential(mock_facades, mock_units):
    """Test basic daylight potential calculation."""
    result = calculate_daylight_potential(mock_facades, mock_units)
    
    # Windows area: 20 (glass from level 1) + 15 (glass from level 2) = 35
    # Total unit area: 100 + 80 = 180
    # Expected: 35 / 180 = 0.194444...
    expected = 35.0 / 180.0
    assert result == pytest.approx(expected, rel=1e-6)


def test_calculate_daylight_potential_zero_unit_area(mock_facades):
    """Test that zero unit area returns 0."""
    result = calculate_daylight_potential(mock_facades, [])
    assert result == 0.0


def test_calculate_daylight_potential_no_windows(mock_units):
    """Test with no glass facades."""
    facades = [
        Facade(
            cluster_id="1",
            speckle_type="facade",
            geometry=None,
            material=MaterialType.CONCRETE,
            area=50.0,
            thickness=0.3,
            level=1
        ),
    ]
    result = calculate_daylight_potential(facades, mock_units)
    assert result == 0.0


def test_calculate_daylight_potential_per_level(mock_facades, mock_units):
    """Test daylight potential calculation per level."""
    levels = [1, 2]
    result = calculate_daylight_potential_per_level(mock_facades, mock_units, levels)
    
    # Level 1: Windows area = 20, Unit area = 100, ratio = 0.2
    # Level 2: Windows area = 15, Unit area = 80, ratio = 0.1875
    assert len(result) == 2
    assert result[1] == pytest.approx(20.0 / 100.0, rel=1e-6)
    assert result[2] == pytest.approx(15.0 / 80.0, rel=1e-6)


def test_calculate_daylight_potential_per_cluster(mock_facades, mock_units):
    """Test daylight potential calculation per cluster."""
    clusters = ["1", "2"]
    result = calculate_daylight_potential_per_cluster(mock_facades, mock_units, clusters)
    
    # Cluster 1: Windows area = 20, Unit area = 100, ratio = 0.2
    # Cluster 2: Windows area = 15, Unit area = 80, ratio = 0.1875
    assert len(result) == 2
    assert result["1"] == pytest.approx(20.0 / 100.0, rel=1e-6)
    assert result["2"] == pytest.approx(15.0 / 80.0, rel=1e-6)


@patch("domain.daylight_potential.METRICS", {
    "Daylight Potential": {
        "benchmark": 0.15,
        "action": "Increase window area"
    }
})
def test_get_daylight_potential_metric(mock_facades, mock_units):
    """Test the complete metric result generation."""
    levels = [1, 2]
    clusters = ["1", "2"]
    
    result = get_daylight_potential_metric(mock_facades, mock_units, levels, clusters)
    
    assert result.name == "Daylight Potential"
    assert result.benchmark == 0.15
    assert result.total_value == pytest.approx(35.0 / 180.0, rel=1e-6)
    assert len(result.value_per_level) == 2
    assert len(result.value_per_cluster) == 2
    assert result.action == "Increase window area"


def test_calculate_daylight_potential_per_level_empty_level(mock_facades, mock_units):
    """Test behavior when a level has no data."""
    levels = [1, 2, 3]  # Level 3 doesn't exist
    result = calculate_daylight_potential_per_level(mock_facades, mock_units, levels)
    
    assert len(result) == 2  # Only levels 1 and 2, level 3 is skipped
    assert result[1] == pytest.approx(20.0 / 100.0, rel=1e-6)
    assert result[2] == pytest.approx(15.0 / 80.0, rel=1e-6)
    assert 3 not in result  # Level 3 is not in the result


def test_calculate_daylight_potential_only_glass_facades(mock_units):
    """Test calculation when all facades are glass."""
    all_glass_facades = [
        Facade(
            cluster_id="1",
            speckle_type="facade",
            geometry=None,
            material=MaterialType.GLASS,
            area=30.0,
            thickness=0.1,
            level=1
        ),
        Facade(
            cluster_id="1",
            speckle_type="facade",
            geometry=None,
            material=MaterialType.GLASS,
            area=40.0,
            thickness=0.1,
            level=1
        ),
    ]
    result = calculate_daylight_potential(all_glass_facades, mock_units)
    
    # Windows area: 30 + 40 = 70
    # Total unit area: 100 + 80 = 180
    expected = 70.0 / 180.0
    assert result == pytest.approx(expected, rel=1e-6)


def test_calculate_daylight_potential_per_cluster_empty_cluster(mock_facades, mock_units):
    """Test behavior when a cluster has no data."""
    clusters = ["1", "2", "3"]  # Cluster 3 doesn't exist
    result = calculate_daylight_potential_per_cluster(mock_facades, mock_units, clusters)
    
    assert len(result) == 2  # Only clusters 1 and 2, cluster 3 is skipped
    assert result["1"] == pytest.approx(20.0 / 100.0, rel=1e-6)
    assert result["2"] == pytest.approx(15.0 / 80.0, rel=1e-6)
    assert "3" not in result  # Cluster 3 is not in the result
