class CustomError(BaseException):
    def __init__(self, message):
        self.message = message

    def __str__(self) -> str:
        return f'Error: {self.message}'
    

class NotExistsError(CustomError):
    pass