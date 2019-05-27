
import numpy as np # biblioteca Python para realizar cálculos em Arrays


def KSA(key): #função que cria a lista S com valores de 0 a 255
    tam_key = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[
            i % tam_key]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S, n): #função que gera keystream
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


def criandoArray(s): #função que transforma s em array
    return [ord(c) for c in s]


def deArrayParaString(array): #função que retorna o array como string
    text = ""
    for c in range(len(array)):
        text += array[c]
    return text


def cifrar(message, keystream): #função de cifragem
    message = np.array([ord(c) for c in message])
    cipher = keystream ^ message
    print("\nResult: ", cipher)
    return cipher


def iniciarKeystream(key, message): #função que us a keystream gerada em PRGA e converte em array
    S = KSA(key)
    keystream = np.array(PRGA(S, len(message)))
    print("\nKEYSTREAM: ", keystream)
    return keystream


def decrypt(cipher, keystream): #função que pega a keystream gerada e decifra para o texto original
    decrypterUni = keystream ^ cipher
    decrypter = [chr(c) for c in decrypterUni]
    return deArrayParaString(decrypter)


def rc4(key, plaintext): #função que serve como controlador para o algoritmo rc4
    keyArray = criandoArray(key)
    keystream = iniciarKeystream(keyArray, plaintext)
    cipher = cifrar(plaintext, keystream)
    cipherHex = (cipher.astype(np.uint8).data.hex())
    print("\nHEX: ", cipherHex)
    decifrar = ""
    while decifrar != key:
        option = input("\nDeseja descriptografar? [s/n]")
        if option == 's':
            decifrar = input("\nChave:")
            print("\nResultado:", decrypt(cipher, keystream))
            exit()
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



