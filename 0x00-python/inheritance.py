class Animal:

    def __init__(self, birthType="Unknown",
                 appearance="Unknown",
                 blooded="Unkown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthdType(self):
        return self.__birthType

    @birthType.setter
    def birthdType(self, birthType):
        self.__birthType = birthType

     @property
    def appearnace(self):
        return self.__appearnace

    @appearnace.setter
    def appearnce(self, appearnace):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded
    
    
    def __str__(self):
        return "A {} is {} it is {} it is {}".format(
            type(self).__name__, self.birthType, self.appearance,
        self.blooded) 
        
    '''Inheritance'''
    class Mammal(Animal):
        def __init__(self, birthType = "born a live",
                     appearance = "hair and fur",
                     blooded = "Warm blooded",
                     nurseYoung = True):
            
            Animal.__init__(self, birthType, appearance, blooded)
            
            self.__nurseYoung = nurseYoung
            
        @property
        def nurseYoung(self):
            return self.__nurseYoung
        
        @nurseYoung.setter
        def nurseYiung(self, nurseYoung):
            self.__nurseYoung = nurseYoung 
            
        def __str__(self):
            return super().__str__() + "and it is {} they nurse their young".format(self.nurseYoung)
    
    
    class Reptiles(Animal):
        
        def __init__(self, birthType = "born in an egg or born a live",
                     appearance = "dry scale",
                     blooded = "cold blooded blooded"):
            
            Animal.__init__(self, birthType, appearance,
                            blooded)
            
    '''Function overloading'''
    
    
               
            
    
