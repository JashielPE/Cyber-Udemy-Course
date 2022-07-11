import random

def generate_key(n):
    return bytes([random.randrange(0,256) for _ in range(n)])

def xor_bytes(key, message):
    len_cmes = min(len(message), len(key))
    return bytes([key[i] ^ message[i] for i in range(len_cmes)])

# Do it by the enemy
message = 'DO ATTACK'
message= message.encode()
key_stream = generate_key(len(message))
cipher= xor_bytes(key_stream, message)

#Do it by ourseelves (the hacker)
mes_HC = 'NO ATTACK'
mes_HC = mes_HC.encode()
#I will create a key to obtain my message
key_stream = xor_bytes(cipher, mes_HC)
print(key_stream)
print(xor_bytes(key_stream,cipher))

