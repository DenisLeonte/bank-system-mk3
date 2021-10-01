from hashlib import sha256


class user:
    __id = -1
    __name = ""
    __password = ""
    __encrypted_password = ""

    def set_name(self, name):
        self.__name = name

    def set_id(self,id):
        self.__id = id

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_password(self, password):
        self.__password = password

    def encrypt_password(self):
        try:
            sha = sha256(self.__password.encode())
            self.__encrypted_password = sha.hexdigest()
            return True
        except:
            print("Fatal error. Failed to encrypt the password. Further operations impossible")
            return False

    def get_encrypted_password(self):
        return self.__encrypted_password

    def create_from_row(self,row):
        self.__id = row[0]
        self.__name = row[1]
        self.__encrypted_password = row[2]
