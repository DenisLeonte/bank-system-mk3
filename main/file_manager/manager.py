import csv
import user.user


class user_file:
    __path = ""

    def __init(self):
        f = open(self.__path, "x")
        print("File initialized successfully")

    def __set_path(self, path):
        print("Path set up successfully")
        self.__path = path

    def __search_user(self, user):
        with open(self.__path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if user.__get_name() == row[1] and user.__get_encrypted_password() == row[2]:
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

    def __check_file_integrity(self):
        with open(self.__path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            lines = 0
            for row in csv_reader:
                if self.__check_row_integrity(row):
                    lines += 1
                else:
                    print("Fatal error at line " + str(lines))
                    break
    def __find_registered_users(self):
        users = 0
        with open(self.__path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                users += 1
        return users

    def __add_user(self,user):
        user.__set_id(int(self.__find_registered_users()) + 1)
        tx = str(user.__get_id()) + "," + user.__get_name() + "," + user.__get_encrypted_password() + "\n"
