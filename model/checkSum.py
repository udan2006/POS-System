class checkSum:
    def __init__(self, value):
        self.value = value
        self.lowercase_letters = 0
        self.uppercase_letters = 0
        self.dots_and_digits = 0
        self.checksum = 0

    def calculate(self):
        for char in self.value:
            if "A" <= char <= "Z":
                self.uppercase_letters += 1
            elif "a" <= char <= "z":
                self.lowercase_letters += 1
            elif char.isdigit() or char == ".":
                self.dots_and_digits += 1

        self.checksum = self.uppercase_letters + self.lowercase_letters + self.dots_and_digits
        return self.checksum
