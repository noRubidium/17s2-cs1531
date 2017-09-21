from abc import abstractmethod
"""
Bad SRP: All responsibilities together
Bad OCP: Close for extention, require for modification
"""

class DBReader(object):
    @abstractmethod
    def read_db(self, db):
        pass
class MySQLReader(DBReader):
    def read_db(self, db):
        print("Reading db MySQL Now")
...
        elif type == "SQLite":
            print("Reading db SQLite Now")
        elif type == "CSV":
            print("Reading db CSV Now")
        elif type == "SQLAlchemy":
            print("Reading db SQLAlchemy Now")
        else: print("DB type not recognised")

db_reader = SQLiteReader()
db_reader.read_db()
