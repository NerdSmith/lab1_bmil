import string


class Alphabet:
    def __init__(self):
        self.all_chars = []
        self.all_chars += list(string.ascii_letters)
        self.all_chars += list(string.digits)
        self.all_chars += list(string.punctuation)

    def get_n_symbols(self, n):
        if n > len(self.all_chars) or n <= 0:
            return None
        return self.all_chars[:n]


if __name__ == '__main__':
    a = Alphabet()
    print(a.get_n_symbols(10))
