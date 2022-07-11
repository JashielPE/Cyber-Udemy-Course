class KeyStream:
    def __init__(self, key=1):
        self.x = key

    def gen_key(self):
        self.x = (1103515245 * self.x + 12345) % 2**31
        return self.x

    def get_key_bytes(self):
        return self.gen_key() % 256



