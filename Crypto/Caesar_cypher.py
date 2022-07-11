class Ceaser_cipher:
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = {}
    def __init__(self, message, n_key):
        self.message= message
        self.n_key = n_key

    @property
    def gen_key(self):
        cnt=0
        for c in self.letters:
            self.key[c]= self.letters[(cnt+self.n_key) % len(self.letters)]
            cnt+=1
        return self.key

    def encrypt(self):
        cypher= ''
        for c in self.message:
            if c in self.gen_key:
                cypher+= self.gen_key[c]
            else:
                cypher+=c
        return cypher


#Funtion to decrtip a message based on Caesar cypher
def dec_mess(key, message):
    deckey= {}
    for c in key:
        deckey[key[c]]=c
    dec_mesa=''
    for m in message:
        if m in deckey:
            dec_mesa += deckey[m]
        else:
            dec_mesa += m
    return  dec_mesa


mes_enc= 'HOLI CRAYOLI'
message1= Ceaser_cipher(mes_enc,3)
encryp=message1.encrypt()
print(encryp)
#print(dec_mess(message1.key, encryp))

"""From this part, the idea is to show the vulnerability of the ceasar cypher.
In a weird situation I know that the message is cypher through ceasar cypher, so I will generate different
key (a shift of the alphabet)"""

for i in range(26):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key= {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt + i) % len(letters)]
        cnt += 1

    print(dec_mess(key, encryp))



