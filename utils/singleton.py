
class Singleton(object):
    
    __instance = None
    __initialized = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance
    
    # To ensure __init__() is only called once per singleton,
    # run this at the beginning of __init__ in derived class,
    # and return if output is true.
    def __init__(self) -> None:
        if self.__initialized == True:
            return True
        else:
            self.__initialized = True
        return False