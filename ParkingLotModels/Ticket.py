from ParkingLotModels.BaseModel import BaseModel
class Ticket(BaseModel):
    def __init__(self):
        self.__parkingSpot = None
        self.__entryTime = None
        self.__vehicle = None
        self.__gate = None
        self.__operator = None

    def getParkingStatus(self):
        return self.__parkingSpot

    def setParkingStatus(self, value):
        self.__parkingSpot = value

    def getEntryTime(self):
        return self.__entryTime

    def setEntryTime(self, value):
        self.__entryTime = value

    def getVehicle(self):
        return self.__vehicle

    def setVehicle(self, value):
        self.__vehicle = value

    def getGate(self):
        return self.__gate

    def setGate(self, value):
        self.__gate = value

    def getOperator(self):
        return self.__operator

    def setOperator(self, value):
        self.__operator = value
