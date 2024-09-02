class Calculator:
    def sum(self, number1, number2):
        return number1 + number2
    

    def subtract(self, number1, number2):
        return number1 - number2
    
    def multiply(self, number1, number2):
        return number1 * number2
    
    def divide(self, number1, number2):
        if number2 == 0:
            raise ValueError('You cannot divide by zero')
        return number1 / number2