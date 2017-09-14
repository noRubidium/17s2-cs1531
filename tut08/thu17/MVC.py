import sqlite3

class Controller:
    def search_book(self, title):
        pass

    def search_author(self, author):
        model = LibraryModel()
        data = model.get_author(author)
        view = LibraryView()
        view.display_author(data, author)

# interacting with the user (present the user with info)
class LibraryView:
    def display_author(self, data, author):
        print('The books written by %s are:' % author)
        for row in data:
            print(row)
        print()

    def display_book(self):
        pass

# file_handler = open('library', 'w')
# file_handler.close()


# interacting with the databse
class LibraryModel:
    def get_author(self, author):

        return self.__db_op('SELECT * FROM book WHERE author = ?', (author,))

    def get_book(self, title):
        return self.__db_op('SELECT * FROM book WHERE title = ?', (title,))

    def __db_op(self, query, payload):
        results = []
        with sqlite3.connect('library.db') as connection:
            cursorObj = connection.cursor()
            rows = cursorObj.execute(query, payload)
            connection.commit()
            for row in rows:
                results.append(row)
            cursorObj.close()
        return results
controller = Controller()
controller.search_author("Martin")
controller.search_author("Tom")
controller.search_book("Agile Design Principles")
controller.search_book("The Lord of the Rings")
controller.search_book("Pride and Prejudice")
controller.search_book("The Great Gatsby")
controller.search_book("Introduction to Cooking")
