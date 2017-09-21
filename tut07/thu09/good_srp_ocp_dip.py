from abc import abstractmethod

"""
Good SRP: Responsibilities seperated into two classes
Good OCP: Open for extending more types of DbReader and ReportFormatter, close for modification
Good DIP:
"""


class DbReader(object):
    """
    @param: db contains database connection details
    """
    @abstractmethod
    def read_db(self, db):
        pass

class MySQLReader(DbReader):

    def read_db(self, db):
        print("Reading db MySQL Now")
        return "..report data.."

class SQLiteReader(DbReader):

    def read_db(self, db):
        print("Reading db SQLite Now")
        return "..report data.."

class CSVReader(DbReader):

    def read_db(self, db):
        print("Reading db CSV Now")
        return "..report data.."

class SQLAlchemyReader(DbReader):

    def read_db(self, db):
        print("Reading db SQLAlchemy Now")
        return "..report data.."

class ReportFormatter(object):

    """
    @param: data contains report data to be formatted
    """
    
    @abstractmethod
    def format_report(self, data):
        pass

class PDFFormatter(ReportFormatter):

    def format_report(self, data):
        print("Writting data into PDF format")


class HTMLFormatter(ReportFormatter):

    def format_report(self, data):
        print("Writting data into HTML format")


class WordFormatter(ReportFormatter):

    def format_report(self, data):
        print("Writting data into Word format")


class TXTFormatter(ReportFormatter):
    
    def format_report(self, data):
        print("Writting data into TXT format")



"""
class Reporter Class completely decoupled from the reader and formatter classes
The specific reader and formatter are injected when an instance of the Reported class
is created by the client
"""

class Report():
    def __init__(self,reader,formatter):
        self._reader = reader
        self._formatter = formatter

    def create_report(self):
        data = self._reader.read_db("MySQL connection details")
        self._formatter.format_report(data)

report_client = Report(CSVReader(),HTMLFormatter())
report_client.create_report()


