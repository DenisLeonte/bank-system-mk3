from hashlib import sha256


class user:
    __id = -1
    __name = ""
    __password = ""
    __encrypted_password = ""

    def __set_name(self, name):
        self.__name = name

    def __set_id(self,id):
        self.__id = id

    def __get_id(self):
        return self.__id

    def __get_name(self):
        return self.__name

    def set_password(self, password):
        self.__password = password

    def __encrypt_password(self):
        try:
            sha = sha256(self.__password.encode())
            self.__encrypted_password = sha.hexdigest()
            return True
        except:
            print("Fatal error. Failed to encrypt the password. Further operations impossible")
            return False

    def __get_encrypted_password(self):
        return self.__encrypted_password
