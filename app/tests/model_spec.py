import unittest
import mock
from app.lib.model import Model
from app.lib.table import Table
from app.lib.connection import Connection

class ModelUnitTest(unittest.TestCase):
    def setUp(self):
        self.table_mock = mock.MagicMock(spec=Table)
        self.connection_mock = mock.MagicMock(spec=Connection)
        self.model = Model(table=self.table_mock, connection=self.connection_mock)
    def test_insert(self):
        self.model.insert(data={})
        self.connection_mock.connect.assert_called_once()
        self.table_mock.create_insert_stmt.assert_called_once()
    def test_create_static(self):
        self.connection_mock.get_table.return_value = self.table_mock
        model = Model.create(connection=self.connection_mock, table_name='test')
        self.connection_mock.get_table.assert_called_once_with('test')
        self.assertEqual(isinstance(model, Model), True)

if __name__ == '__main__':
    unittest.main()
