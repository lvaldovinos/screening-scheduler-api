import colander

class Validator:
    def __init__(self, schema = None):
        self.__schema = schema
        self.__error = None
    def validate(self, data):
        try:
            self.__schema.deserialize(data)
        except colander.Invalid as error:
            self.__error = error.asdict()
    @property
    def isvalid(self):
        return self.__error is None
