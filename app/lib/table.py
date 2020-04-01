from sqlalchemy.sql import select

class Table:
    def __init__(self, table = None):
        self.table = table 
    def create_insert_stmt(self, *arg, **kwargs):
        return self.table.insert().values(*arg, **kwargs)
    def create_select_all_stmt(self):
        return select([self.table])
