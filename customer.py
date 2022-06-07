import connections
import database
import shopping


class Customer:
    connection = connections.PersonDB().get_connection()
    cursor = connections.PersonDB().get_cursor()

    table_name = database.PersonDB().table_name
    end = False

    def main_menu(self):
        while True:
            print('\nCONTINUE ...\n')
            print('[1] -> SIGN IN')
            print('[2] -> SIGN UP')
            print('\n[0] -> BACK\n')

            choice = input("[?] -> ")
            try:
                choice = int(choice)
            except ValueError:
                print("\nINVALID")
                continue

            if choice == 1:
                self.sign_in()
            elif choice == 2:
                self.sign_up()
            elif choice == 0:
                return False
            else:
                print("\nINVALID")

    def sign_in(self):
        person_name = str(input("INPUT YOUR NAME: ").upper())
        person_password = str(input("INPUT YOUR PASSWORD: "))
        person_type = 'CUSTOMER'

        item = self.cursor.execute("SELECT NAME, PASSWORD, TYPE FROM {}".format(self.table_name)).fetchall()
        for i in range(0, len(item)):
            if person_name == item[i][0] and person_password == item[i][1] and person_type == item[i][2]:
                self.end = True
                shopping.Shopping().main_menu()
            elif (person_name == item[i][0] or person_password == item[i][1]) and person_type == item[i][2]:
                print("\nWRONG CUSTOMER NAME OR PASSWORD\n")
                self.end = True
        if not self.end:
            print("\nSIGN UP FIRSTLY\n")

    def sign_up(self):
        person_name = str(input("\nINPUT YOUR NAME: ").upper())
        person_password = str(input("INPUT YOUR PASSWORD: "))
        person_type = 'CUSTOMER'

        self.connection.execute("INSERT INTO {} VALUES (?, ?, ?)".format(self.table_name),
                                (person_name, person_password, person_type))
        self.connection.commit()

        print("\nNOW YOU CAN SIGN IN\n")