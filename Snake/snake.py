

class Snake:
    
    def __init__(self, pos= (0, 0)):
        # x and y coord on grid
        self.__position = pos
        self.__direction = (0, 0)
        self.tail = []
        self.tail.append(pos)
    
    def move(self):
        self.tail.insert(0, self.__position)
        self.__position = tuple(map(sum, zip(self.__position
                                            ,self.__direction)))
        self.tail.pop()
    
    def grow(self):
        # this 
        self.tail.append(self.__position)
        
    def changePos(self, pos):
        self.__position = pos
        

    def setDirection(self, direction):
    # Snake should not be able to cd opposite to movement dir
        if (tuple(map(lambda x: x*-1, direction))) != self.__direction:
            self.__direction = direction
        
    def locate(self):
        return self.__position
    
        

