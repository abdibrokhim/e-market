import connection


class Database:
    connection_person = connection.PersonDB().get_connection()
    cursor_person = connection.PersonDB().get_cursor()

    connection_market = connection.ShopDB().get_connection()
    cursor_market = connection.ShopDB().get_cursor()

    table_name_person = 'PERSON'
    table_name_market = 'FOOD'

    def create_person_database(self):
        self.cursor_person.execute('''CREATE TABLE {}
            (NAME CHAR(25), 
            PASSWORD VARCHAR(25), 
            TYPE CHAR(25));'''.format(self.table_name_person))
        self.cursor_person.close()

    def create_market_database(self):
        self.cursor_market.execute('''CREATE TABLE {}
            (NAME CHAR(25), 
            SUPPLY INTEGER, 
            PRICE INTEGER, 
            CATEGORY CHAR(25));'''.format(self.table_name_market))
        self.cursor_market.close()