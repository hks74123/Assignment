
# custom error class to show erro on negative input
class limit_customerror(Exception):
    def __init__(self, number, message="Your number should be positive"):
        self.number = number
        self.message = message
        super().__init__(self.message)

number=int(input(""))
if(number<0):
    raise limit_customerror(number)
else:
    print(number)