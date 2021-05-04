class EmailFormatError(Exception):
    error_message = "Email format is invalid"
    def __init__(self):
        super().__init__(EmailFormatError.error_message)

class PasswordError(Exception):
    error_message = "Password is too short"
    def __init__(self):
        super().__init__(EmailFormatError.error_message)

class DuplicationError(Exception):
    error_message = "Duplicated user info: "
    def __init__(self, whaterror):
        self.whaterror = whaterror
        super().__init__(EmailFormatError.error_message+whaterror)
