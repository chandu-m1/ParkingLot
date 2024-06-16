from ParkingLotModels.BaseModel import BaseModel
class Bill(BaseModel):
    def __init__(self):
        super().__init__()
        self.__exitTime = None
        self.__ticket = None
        self.__operator = None
        self.__amount = 0
        self.__gate = None

    def getExitTime(self):
        return self.__exitTime

    def setExitTime(self, value):
        self.__exitTime = value

    def getTicket(self):
        return self.__ticket

    def setTicket(self, value):
        self.__ticket = value

    def getOperator(self):
        return self.__operator

    def setOperator(self, value):
        self.__operator = value

    def getAmount(self):
        return self.__amount

    def setAmount(self, value):
        self.__amount = value

    def getGate(self):
        return self.__gate

    def setGate(self, value):
        self.__gate = value
