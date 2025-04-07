class me :
    def __init__ (self):
        self.__id=111
        self.__name="megha"

    def display(self):
      print("id : ",self.__id)
      print("name :",self.__name)


M=me()
M.display()

M.__id=22222
M.__name="reetu"
M.display()

