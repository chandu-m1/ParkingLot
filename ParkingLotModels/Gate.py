class Gate:
    def __init__(self):
        self.__gateNumber = 0
        self.__operator = None
        self.__gateStatus = None
        self.__gateType = None

    def getGateNumber(self):
        return self.__gateNumber
    def setGateNumber(self,value):
        self.__gateNumber = value
    def getOperator(self):
        return self.__operator
    def setOperator(self,value):
        self.__operator = value
    def getGateStatus(self):
        return self.__gateStatus
    def setGateStatus(self,value):
        self.__gateStatus = value
    def getGateType(self):
        return self.__gateType
    def setGateType(self,value):
        self.__gateType = value