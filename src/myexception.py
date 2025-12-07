class MyException(Exception):
    def __init__(self, messeg: str):
        self.message = messeg
