from ParkingLotModels.BaseModel import BaseModel
class ParkingSpot(BaseModel):
    def __init__(self):
        self.__number = 0
        self.__vehicleType = []
        self.__spotStatus = None
        self.__vehicle = None

    def getNumber(self):
        return self.__number

    def setNumber(self, value):
        self.__number = value

    def getVehicleType(self):
        return self.__vehicleType

    def setVehicleType(self, value):
        self.__vehicleType = value

    def getSpotStatus(self):
        return self.__spotStatus

    def setSpotStatus(self, value):
        self.__spotStatus = value

    def getVehicle(self):
        return self.__vehicle

    def setVehicle(self, value):
        self.__vehicle = value
