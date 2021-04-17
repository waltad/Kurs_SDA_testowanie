from unittest.mock import patch, MagicMock

from sample_5_mocks.sample_patch import RemovalService


class TestRemovalService:

    def test_rm(self):
        removal_service = RemovalService()

        mock = MagicMock()
        with patch('sample_5_mocks.sample_patch.os', mock):
            removal_service.rm('test_path')
            # assert mock.remove.call_count == 1
            mock.remove.assert_called_once_with('test_path')
