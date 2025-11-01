class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return f"{self.first_name}"

    def get_last_name(self):
        return f"{self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
