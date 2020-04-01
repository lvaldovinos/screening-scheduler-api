import mock
import unittest
import colander
from app.lib.validator import Validator

class ValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self.data = {}
        self.schema_mock = mock.MagicMock(spec=colander.MappingSchema)
        self.validator = Validator(self.schema_mock)
    def test_validate(self):
        self.validator.validate(self.data)
        self.schema_mock.deserialize.assert_called_once_with(self.data)
        self.assertTrue(self.validator.isvalid)
    def test_validate_invalid(self):
        schema_mock = mock.MagicMock(spec=colander.SchemaNode)
        self.schema_mock.deserialize.side_effect = mock.MagicMock(side_effect=colander.Invalid(schema_mock))
        self.validator.validate(self.data)
        self.assertFalse(self.validator.isvalid)

if __name__ == '__main__':
    unittest.main()
