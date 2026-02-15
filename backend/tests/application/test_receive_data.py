from unittest.mock import patch, MagicMock
from adapters.speckle.receive_data import receive_data

"""
This test checks that operations.receive is called with the correct arguments 
and returns a Model object with units, open spaces, and facades.
"""

def test_receive_data_returns_received():
    mock_version = MagicMock()
    mock_version.referenced_object = "mock_object_id"
    mock_transport = MagicMock()
    
    # Create mock data structure with collections
    mock_units_collection = MagicMock()
    mock_units_collection.name = "UNITS"
    mock_units_collection.elements = []
    
    mock_open_spaces_collection = MagicMock()
    mock_open_spaces_collection.name = "OPEN_SPACES"
    mock_open_spaces_collection.elements = []
    
    mock_facades_collection = MagicMock()
    mock_facades_collection.name = "FACADES"
    mock_facades_collection.elements = []
    
    # Create mock data with elements attribute
    mock_result = MagicMock()
    mock_result.elements = [mock_units_collection, mock_open_spaces_collection, mock_facades_collection]

    with patch("adapters.speckle.receive_data.operations.receive", return_value=mock_result) as mock_receive:
        result = receive_data(mock_version, mock_transport)
        mock_receive.assert_called_once_with("mock_object_id", mock_transport)
        # Result should be a Model object with collections
        assert result is not None
        assert hasattr(result, 'units')
        assert hasattr(result, 'open_spaces')
        assert hasattr(result, 'facades')