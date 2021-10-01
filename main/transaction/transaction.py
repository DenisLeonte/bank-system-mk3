from datetime import datetime

class transaction:
    __sender = ""
    __destinatary = ""
    __notes = ""
    __ammount = 0.0
    __day = 0
    __month = 0
    __year = 0


    def __get_today_date(self):
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        date = date.split("/")
        self.__day = int(date[0])
        self.__month = int(date[1])
        self.__year = int(date[2])

    def set_sender(self,sender):
        self.__sender = sender

    def set_destinatary(self,destinatary):
        self.__destinatary = destinatary

    def set_ammount(self,ammount):
        self.__ammount = float(ammount)

    def bake(self):
        self.__get_today_date()
        return self.__sender + "," + self.__destinatary + "," + str(self.__ammount) + "," \
               + str(self.__day) + "," + str(self.__month) + "," + str(self.__year) + "\n"
