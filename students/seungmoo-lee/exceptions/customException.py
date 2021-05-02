
class ValidError(Exception):    # 사용자 정의 Exception
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value
