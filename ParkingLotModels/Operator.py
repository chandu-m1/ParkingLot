from ParkingLotModels.BaseModel import BaseModel
class Operator(BaseModel):
    def __int__(self):
        self.__name = None
        self.__employeeId = 0

    def getName(self):
        return self.__name
    def setName(self,value):
        self.__name = value

    def getEmployeeId(self):
        return self.__employeeId
    def setEmployeeId(self,value):
        self.__employeeId = value