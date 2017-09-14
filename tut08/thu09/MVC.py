import sqlite3

class LibraryController(object):
    def search_author(self, title):
        pass

    def search_by_author(self, author):
        data = LibraryModel.get_detail(author)
        return LibraryView.display_book(author, data)


class LibraryView(object):

    @staticmethod
    def display_author(data):
        pass

    @staticmethod
    def display_book(author, data):
        print('Book with author %s are: ' % author)
        for row in data:
            print (' '.join(list(map(str, row))))
        print()

class LibraryModel(object):
    @staticmethod
    def get_author(title):
        pass

    @staticmethod
    def get_detail(author):
        results = []
        with sqlite3.connect('library.db') as connection:
            cursorObj = connection.cursor()
            rows = cursorObj.execute('SELECT * FROM BOOK WHERE author = ?', (author, ))
            connection.commit()
            for row in rows:
                results.append(row)
            cursorObj.close()
        return results


library = LibraryController()
library.search_by_author('Martin')
