from ParkingLotModels.BaseModel import BaseModel
class Payment(BaseModel):
    def __init__(self):
        self.__amount = 0
        self.__paymentMode = None
        self.__paymentStatus = None
        self.__refId = None
        self.__bill = None
        self.__time = None

    def getAmount(self):
        return self.__amount
    def setAmount(self,value):
        self.__amount = value

    def getPaymentMode(self):
        return  self.__paymentMode

    def setPaymentMode(self,value):
        self.__paymentMode = value

    def getPaymentStatus(self):
        return  self.__paymentStatus

    def setPaymentStatus(self,value):
        self.__paymentStatus = value

    def getRefId(self):
        return  self.__refId

    def setRefId(self,value):
        self.__refId = value

    def getBill(self):
        return  self.__bill

    def setBill(self,value):
        self.__bill = value

    def getTime(self):
        return  self.__time

    def setTime(self,value):
        self.__time  = value
