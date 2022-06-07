class PersonDB:
    def get_connection(self):
        import sqlite3
        connection = sqlite3.connect('person.db')
        return connection

    def get_cursor(self):
        import sqlite3
        connection = sqlite3.connect('person.db')
        cursor = connection.cursor()
        return cursor


class ShopDB:
    def get_connection(self):
        import sqlite3
        connection = sqlite3.connect('market.db')
        return connection

    def get_cursor(self):
        import sqlite3
        connection = sqlite3.connect('market.db')
        cursor = connection.cursor()
        return cursor