class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand()% 256


def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i] for i in range(len(message))])


def crack(key_stream, cipher):
    lenght = min(len(key_stream), len(cipher))
    return bytes([key_stream[i] ^ cipher[i] for i in range(lenght)])


# This is the message that Eve gives Alice
message = "This is my long message that Eve tricks Alice into using".encode()

# This is Alice
key = KeyStream(10)
cipher = encrypt(key, message)

# This is Eve getting the key stream
eves_key_stream = get_key(message, cipher)

# This is Bob
key = KeyStream(10)
message = encrypt(key, cipher)

# This is Alice sending a new message
message = "Hey Bob. Let's take over the world domination.".encode()
key = KeyStream(10)
cipher = encrypt(key, message)

# This is Eve extracting the message
eves_decryption = crack(eves_key_stream, cipher)
print(eves_decryption)