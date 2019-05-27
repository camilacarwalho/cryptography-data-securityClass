import numpy as np
def KSA(key):
    tam_key = len(key)
    S = list(range(256))
    j = 0
    for i in range (256):
        j = (j + S[i]+key[i%tam_key])%256
        S[i],S[j] = S[j], S[i]
    return S

def PRGA(S, n):
    i = 0
    j = 0
    key=[]
    while n>0:
        n-=1
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i],S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key.append(K)
    return key

def preparing_key_array(s):
    return [ord(c) for c in s]

key = input("Digite a chave:")
message = input("Digite a mensagem")
key = preparing_key_array(key)


S = KSA(key)

keystream = np.array(PRGA(S, len(message)))

print("keystream: ", keystream)

message = np.array([ord(c) for c in message])

cipher = keystream ^ message #XOR

print(cipher.astype(np.uint8).data.hex())