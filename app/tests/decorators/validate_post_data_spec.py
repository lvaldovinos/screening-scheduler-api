import unittest
import colander
import mock
from flask import g
from app.lib.validator import Validator
from app.decorators.validate_post_data import validate_post_data
from app import create_app
from config import Config

class ValidatePostDataTestCase(unittest.TestCase):
    def setUp(self):
        self.schema_mock = mock.MagicMock(spec=colander.MappingSchema)
        self.controller_mock = mock.Mock()
        self.app = create_app(Config())
    @mock.patch.object(Validator, 'validate', autospec=True)
    def test_validate_post_data(self, validate_mock):
        with self.app.test_request_context(json={}):
            decorator = validate_post_data(schema=self.schema_mock)
            wrapper = decorator(self.controller_mock)
            wrapper()
            validate_mock.assert_called_once()
            self.controller_mock.assert_called_once()
            self.assertNotEqual(g.validated_data, None)
    @mock.patch('app.decorators.validate_post_data.Validator.isvalid', new_callable=mock.PropertyMock)
    @mock.patch('app.decorators.validate_post_data.jsonify')
    @mock.patch('app.decorators.validate_post_data.make_response')
    def test_respond_400(self, make_response_mock, jsonify_mock, isvalid_mock):
        isvalid_mock.return_value = False
        jsonify_mock.return_value = 'test'
        with self.app.test_request_context():
            decorator = validate_post_data(schema=self.schema_mock)
            wrapper = decorator(self.controller_mock)
            wrapper()
            self.controller_mock.assert_not_called()
            jsonify_mock.assert_called_once()
            make_response_mock.assert_called_once_with('test', 400)

if __name__ == '__main__':
    unittest.main()
