import unittest
import mock
import sqlalchemy
from app.lib.connection import Connection
from app.lib.table import Table

class TableTestCase(unittest.TestCase):
    def setUp(self):
        self.table_mock = mock.MagicMock(spec=sqlalchemy.schema.Table)
        self.insert_mock = mock.MagicMock(spec=sqlalchemy.sql.expression.Insert)
        self.table_mock.insert.return_value = self.insert_mock
        self.table = Table(self.table_mock)
        print('setUp')
    def test_create_insert_stmt(self):
        stmt = self.table.create_insert_stmt(test= 'test', test2= 'test2')
        self.table_mock.insert.assert_called_once()
        self.insert_mock.values.assert_called_with(test= 'test', test2= 'test2')

if __name__ == '__main__':
    unittest.main()
