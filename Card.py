class Card():
    def __init__(self, value = -1, image = "back.png", status = False):
        self.__value = value
        self.__image = image
        self.__status = status
    
    def getValue(self):
        return self.__value
    
    def getImage(self):
        if self.__status:
            return self.__image
        else:
            return "back.png"
    
    # True is face up, False is face down
    def flip(self):
        self.__status = not self.__status
