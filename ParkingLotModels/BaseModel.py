class BaseModel:
    def __init__(self):
        self.__id = 0
        self.__createdAt = None
        self.__lastUpdatedAt = None

    def getId(self):
        return self.__id

    def setId(self, value):
        self.__id = value

    def getCreatedAt(self):
        return self.__createdAt

    def setCreatedAt(self, value):
        self.__createdAt = value

    def getLastUpdatedAt(self):
        return self.__lastUpdatedAt

    def setLastUpdatedAt(self, value):
        self.__lastUpdatedAt = value
