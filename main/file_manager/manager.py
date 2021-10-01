import csv
import sys
sys.path.insert(0, 'C:\\Users\\denis\\PycharmProjects\\bank-systemV3\\main\\user')
from user import user
sys.path.insert(0, 'C:\\Users\\denis\\PycharmProjects\\bank-systemV3\\main\\transaction')
from transaction import transaction

class user_file:
    __path = ""

    def init(self):
        f = open(self.__path, "x")
        f.close()
        print("File initialized successfully")

    def set_path(self, path):
        print("Path set up successfully")
        self.__path = path

    def search_user(self, user):
        with open(self.__path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if user.get_name() == row[1] and user.get_encrypted_password() == row[2]:
                    print("User found")
                    return True
        print("User not found")
        return False

    def __check_row_integrity(self, row):
        try:
            int(row[0])
            return True
        except:
            print("Problem with the ID of the user")
            return False

    def check_file_integrity(self):
        with open(self.__path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            lines = 0
            for row in csv_reader:
                if self.__check_row_integrity(row):
                    lines += 1
                else:
                    print("Fatal error at line " + str(lines))
                    return False
            print("File is OK")
            return True

    def find_registered_users(self):
        users = 0
        with open(self.__path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                users += 1
        return users

    def add_user(self, user):
        user.set_id(int(self.find_registered_users()) + 1)
        tx = str(user.get_id()) + "," + user.get_name() + "," + user.get_encrypted_password() + "\n"
        with open(self.__path, 'a') as f:
            f.write(tx)

    def find_user(self, name):
        User = user()
        with open(self.__path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if row[1] == name:
                    User.create_from_row(row)
                    return User
        print("No user found")
        return User


class transaction_file:
    __path = ""

    def init(self):
        f = open(self.__path,"x")
        f.close()
        print("File initalized successfully")

    def set_path(self,user):
        self.__path ="transactions//" + user.get_name() + "_" + str(user.get_id()) + ".txt"

    def get_path(self):
        return self.__path

    def add_transaction(self,transaction):
        tx = transaction.bake()
        with open(self.__path, 'a') as f:
            f.write(tx)

    def __check_row_integrity(self, row):
        try:
            float(row[2])
            int(row[3])
            int(row[4])
            int(row[5])
            return True
        except:
            print("Problem with the transaction file")
            return False

    def check_file_integrity(self):
        with open(self.__path,"r") as csv_file:
            lines = 0
            reader = csv.reader(csv_file,delimiter=",")
            for row in reader:
                if self.__check_row_integrity(row):
                    lines+=1
                else:
                    print("Fatal error at line " + lines)
                    break
