from abc import abstractmethod, ABCMeta
"""
Bad SRP: All responsibilities together
Bad OCP: Close for extention, require for modification
"""
N -> 1
1 -> M
class Reader(metaclass=ABCMeta):
    @abstractmethod
    def read_db(self, db):
        pass

class MySQLReader(Reader):
    def read_db(self, db):
        print("Reading db MySQL Now")


class SQLiteReader(Reader):
    def read_db(self, db):
        print("Reading db SQLite Now")

class CSVReader(Reader):
    def read_db(self, db):
        print("Reading db CSV Now")


        elif type == "SQLAlchemy":
            print("Reading db SQLAlchemy Now")
        else:
            print("DB type not recognised")


class Reporter(object):
    def format_report(self, data, type):
        if type == "PDF":
            print("Writing data into PDF format")
        elif type == "HTML":
            print("Writing data into HTML format")
        elif type == "Word":
            print("Writing data into Word format")
        elif type == "TXT":
            print("Writing data into TXT format")
        else:
            print("Format type not recognised")
