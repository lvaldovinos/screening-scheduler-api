import colander

class Calendar(colander.MappingSchema):
    interviewer_fullname = colander.SchemaNode(colander.String())
    interviewer_email = colander.SchemaNode(colander.String())
    public_name = colander.SchemaNode(colander.String())
