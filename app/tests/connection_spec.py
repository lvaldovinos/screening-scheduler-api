import unittest
import mock
import sqlalchemy
from app.lib.connection import Connection, ConnectionSingleton

class ConnectionSingletonTestCase(unittest.TestCase):
    def setUp(self):
        self.engine_mock = mock.MagicMock(spec=sqlalchemy.engine.Engine)

    @mock.patch('app.lib.connection.Connection')
    def test_initialize(self, connection_mock):
        conn1 = ConnectionSingleton.initialize(engine=self.engine_mock)
        conn2 = ConnectionSingleton.initialize(engine=self.engine_mock)
        conn3 = ConnectionSingleton.get_instance()
        connection_mock.assert_called_once()
        self.assertEqual(conn1, conn2)
        self.assertEqual(conn1, conn3)

class ConnectionTestCase(unittest.TestCase):
    def setUp(self):
        self.engine_mock = mock.create_autospec(sqlalchemy.engine.Engine)
        self.connection = Connection(engine=self.engine_mock)

    @mock.patch('app.lib.connection.create_calendars_table_definition')
    def test_initialize_tables_dict(self, create_table_mock):
        metadata_mock = mock.MagicMock(spec=sqlalchemy.schema.MetaData)
        self.connection.initialize_tables_dict(metadata_mock)
        create_table_mock.assert_called_once_with(metadata_mock)

    def test_execute(self):
        self.connection.execute('test')
        self.engine_mock.execute.assert_called_with('test')

    def test_connect(self):
        self.connection.connect()
        self.engine_mock.connect.assert_called_once()

    def test_begin(self):
        self.connection.begin()
        self.engine_mock.begin.assert_called_once()
if __name__ == '__main__':
    unittest.main()
