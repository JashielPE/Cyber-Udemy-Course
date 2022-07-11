import random


def gen_key():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cletter = list(letters)
    key = {}

    for c in letters:
        key[c] = cletter.pop(random.randint(0, len(cletter) - 1))
    return key

def encryp_message(key, mes):
    encryp= ''
    for c in mes:
        if c in key:
            encryp+=key[c]
        else:
            encryp=c
    return encryp

def decryp_message(key,mes):
    decrp_mes=''
    decrypt_key=dict([(value, key) for key, value in key.items()])
    for c in mes:
        if c in decrypt_key:
            decrp_mes+=decrypt_key[c]
        else:
            decrp_mes+=c
    return  decrp_mes

key=gen_key()
mes= 'BAMBINIWIS'
# print(key)
encripted=encryp_message(key, mes)

print(decryp_message(key,encripted))


