from ParkingLotModels.BaseModel import BaseModel
class Vehicle(BaseModel):
    def __int__(self):
        self.__vehicleNumber = None
        self.__vehicleType = None

    def getVehicleNmber(self):
        return self.__vehicleNumber

    def setVehicleNumber(self, value):
        self.__vehicleNumber = value

    def getVehicleType(self):
        return self.__vehicleType

    def setVehicleType(self, value):
        self.__vehicleType = value
