import numpy as np


def KSA(key):
    tam_key = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[
            i % tam_key]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S, n):
    i = 0
    j = 0
    key = []
    while n > 0:
        n -= 1  #
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key.append(K)
    return key


def criandoArray(s):
    return [ord(c) for c in s]


def deArrayParaString(array):
    text = ""
    for c in range(len(array)):
        text += array[c]
    return text


def cifrar(message, keystream):
    message = np.array([ord(c) for c in message])
    cipher = keystream ^ message
    print("\nResult: ", cipher)
    return cipher


def iniciarKeystream(key, message):
    S = KSA(key)
    keystream = np.array(PRGA(S, len(message)))
    print("\nKEYSTREAM: ", keystream)
    return keystream


def decifrar(cipher, keystream):
    decrypterUni = keystream ^ cipher
    decrypter = [chr(c) for c in decrypterUni]
    return deArrayParaString(decrypter)


def rc4(key, plaintext):
    keyArray = criandoArray(key)
    keystream = iniciarKeystream(keyArray, plaintext)
    cipher = cifrar(plaintext, keystream)
    cipherHex = (cipher.astype(np.uint8).data.hex())
    print("\nHEX: ", cipherHex)
    decifrar = ""
    while decifrar != key:
        option = input("\nDeseja descriptografar? [s/n]")
        if option == 's':
            decifrar = input("\nKEY:")
            print("\nResultado:", decifrar(cipher, keystream))

        elif option == 'n':
            print('------------FIM------------')
            exit()
        else: print("Inválido!")




def main():
      while True:
        print('------------RC4------------')
        key = input("Chave:")
        plaintext = input("Texto:")
        rc4(key, plaintext)

main()



