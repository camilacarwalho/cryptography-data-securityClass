def recebeModo():


    while True:
        option = input("1 - Criptografar ; 2 - Descriptografar ")
        option = option.lower()
        if option == '1' or option == 1 or option == '2' or option == 2:
            return option
        print("Escolha entre 1 ou 2")


def recebeChave():

    while True:
        chave = int(input("Valor da chave: "))
        if 1 <= chave <= 26:
            break
        print("Inválido!")

    return chave

def geraMsgTraduzida(modo, mensagem, chave):

    cripto = ''

    if modo == '1' or modo == 1:
        for i in mensagem:
            if 'A' <= i <= 'Z':
                if ord(i) + chave > ord('Z'):
                    cripto += chr((ord('A') + chave - (ord('Z')+1 - ord(i))))
                else:
                    cripto += chr(ord(i) + chave)


            elif 'a' <= i <= 'z':
                if ord(i) + chave > ord('z'):
                    cripto += chr((ord('a') + chave - (ord('z')+1 - ord(i))))
                else:
                    cripto += chr(ord(i) + chave)
            else:
                cripto += i

    elif modo == '2' or modo == 2:
        for i in mensagem:
            if 'A' <= i <= 'Z':
                if ord(i) - chave < ord('A'):
                    cripto += chr(ord('Z') - (chave - (ord(i)+1 - ord('A'))))

                else:
                    cripto += chr(ord(i) - chave)


            elif 'a' <= i <= 'z':
                if ord(i) - chave < ord('a'):
                    cripto += chr(ord('z') - (chave - (ord(i)+1 - ord('a'))))
                else:
                    cripto += chr(ord(i) - chave)
            else:
                cripto += i

    return cripto

def main():


    modo = recebeModo()
    chave = recebeChave()
    mensagem = input("Digite a mensagem: ")
    print(geraMsgTraduzida(modo, mensagem, chave))

main()