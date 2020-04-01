from sqlalchemy import Table, Column, String, Integer

def create_calendars_table_definition(metadata):
    return Table('calendars', metadata,
        Column('id', Integer, primary_key=True),
        Column('interviewer_fullname', String(80)),
        Column('interviewer_email', String(100)),
        Column('public_name', String(20)),
    )
