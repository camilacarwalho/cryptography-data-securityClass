import numpy as np

def recebeModo():
    while True:
        option = input("1 - Criptografar ; 2 - Descriptografar ")
        option = option.lower()
        if option == '1' or option == 1 or option == '2' or option == 2:
            return option
        print("Escolha entre 1 ou 2")


def KSA(key):
    tam_key = len(key)
    S = list(range(256))
    j = 0
    for i in range (256):
        j = (j + S[i]+key[i%tam_key]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S, n):
    i = 0
    j = 0
    key=[]
    while n > 0:
        n-= 1
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key.append(K)
    return key

def preparandoArray(s):
    return [ord(c) for c in s]

def rc4(modo):
    if modo == '1' or modo == 1:
        key = input("Key:")
        message = input("Plaintext:")
        key = preparandoArray(key)

        S = KSA(key)

        keystream = np.array(PRGA(S, len(message)))

        print("keystream: ", keystream)

        message = np.array([ord(c) for c in message])

        cipher = keystream ^ message

        print(cipher.astype(np.uint8).data.hex())

def main():

    modo = recebeModo()
    rc4(modo)

main()
