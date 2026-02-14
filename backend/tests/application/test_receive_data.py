from unittest.mock import patch, MagicMock
from adapters.speckle.receive_data import receive_data

"""
This test checks that operations.receive is called with the correct arguments 
and that receive_data returns the expected result.
"""

def test_receive_data_returns_received():
    mock_version = MagicMock()
    mock_version.referenced_object = "mock_object_id"
    mock_transport = MagicMock()
    mock_result = {"some": "data"}

    with patch("adapters.speckle.receive_data.operations.receive", return_value=mock_result) as mock_receive:
        result = receive_data(mock_version, mock_transport)
        mock_receive.assert_called_once_with("mock_object_id", mock_transport)
        assert result == mock_result