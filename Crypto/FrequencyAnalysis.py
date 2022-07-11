cipher = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""

class Attack:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.freq = {}

    def frequency(self, cipher):
        for c in self.alphabet:
            self.freq[c] = 0

        cnt_letters=0
        for k in cipher:
            if k in self.freq:
                self.freq[k]+=1
                cnt_letters+=1

        for c in self.freq:
            self.freq[c] = round(self.freq[c]/cnt_letters,4)

    def print_freq(self):
        newline=1
        for c in self.freq:
            print('{} : {}'.format(c, self.freq[c]), end= ' ')
            if newline%3 == 0:
                print()
            newline+=1


attack = Attack()
attack.frequency(cipher)
attack.print_freq()