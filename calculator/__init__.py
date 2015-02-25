
class Calculator(object):

    __value=None

    def __init__(self, initial_value=None):
        self.clear()
        if initial_value:
            self.__value=initial_value

    def add(self, input):
        self.__value += float(input)

    def subtract(self, input):
        pass

    def multiply(self, input):
        pass

    def divide(self, input):
        pass

    def clear(self):
        self.__value = float(0.0)

    def value(self):
        return self.__value