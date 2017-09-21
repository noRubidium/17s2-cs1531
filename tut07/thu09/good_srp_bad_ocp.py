from abc import abstractmethod

"""
Good SRP: Responsibilities seperated into two classes
Bad OCP: Close for extention, require for modification
"""

class ReportReader(object):
    
    """
    @param: db contains database connection details
    @param: type is a flag to denote type of database to use
    """
    def read_db(self, db, type):
        if type == "MySQL":
            print("Reading db MySQL Now")
            return "...report...data"
        elif type == "SQLite":
            print("Reading db SQLite Now")
            return "...report...data"
        elif type == "CSV":
            print("Reading db CSV Now")
            return "...report...data"
        elif type == "SQLAlchemy":
            print("Reading db SQLAlchemy Now")
            return "...report...data"
        else: print("DB type not recognised")


class ReportFormatter(object):

    def format_report(self, data, type):
        if type == "PDF":
            print("Writing data into PDF format")
        elif type == "HTML":
            print("Writing data into HTML format")
        elif type == "Word":
            print("Writing data into Word format")
        elif type == "TXT":
            print("Writing data into TXT format")
        else: print("Format type not recognised")

