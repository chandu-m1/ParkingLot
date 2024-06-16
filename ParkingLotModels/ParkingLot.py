class ParkingLot:
    def __init__(self):
        self.__parkingFloors = []
        self.__gates = []
        self.__capacity = 0

    def getParkingFloors(self):
        return self.__parkingFloors
    def setParkingFloors(self, value):
        self.__parkingFloors = value
    def getGates(self):
        return self.__gates
    def setGates(self,value):
        self.__gates = value
    def getCapacity(self):
        return self.__capacity
    def setCapacity(self,value):
        self.__capacity = value
