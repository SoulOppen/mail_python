class Body:
    def __init__(self):
        self.__body=""
    def get_body(self):
        return self.__body
    def add_to_body(self,text):
        self.__body+=text
