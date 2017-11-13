from appJar import gui
app = gui()


def matrix(key):




    matrix = [] #inicializa a matriz vazia

    #coloca a chave em maiusculas, e coloca no inicio da matrix
    for e in key.upper():
        if e not in matrix:
            matrix.append(e)
    #caracteres usados na construção da matrix
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    alphabetPlus = "ABCDEFGHIKLMNOPQRSTUVWXYZ1234567890+- "

    #coloca a letras na matrix apos a inserção da chave
    for e in alphabet:
        if e not in matrix:
            matrix.append(e)

    # initialize a new list. Is there any elegant way to do that?
    matrix_group = []
    for e in range(5):
        matrix_group.append('')

    # Divide em grupos de 5, tem que ser alterado para casa tenha numeros e carateres especiais
    for x in range(5):
        matrix_group[x] = matrix[5 * x:5 * (x + 1)]
    return matrix_group






def message_to_digraphs(message_original):
    # tranforma a mensagem passada em parametro num array
    message = []
    for e in message_original:
        message.append(e)

    # Retira os espaços
    for unused in range(len(message)):
        if " " in message:
            message.remove(" ")

    # Se tiver duas letras iguais coloca um "X" no lugar da segunda
    i = 0
    for e in range (int(len(message) / 2)):
        if message[i] == message[i + 1]:
            message.insert(i + 1, 'X')
        i = i + 2

    # Se for uma mensagem com um tramanha impar coloca um "X" no fim
    if len(message) % 2 == 1:
        message.append("X")
    # Grouping
    i = 0
    new = []

    for x in range (int(len(message) / 2 + 1)):
        new.append(message[i:i + 2])
        i = i + 2
    return new

# função para encontrar um determinada letra na matriz
def find_position(key_matrix, letter):
    linha = coluna = 0

    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                linha = i
                coluna = j

    return linha, coluna


#Encriptação
def encrypt(message):
    message = message_to_digraphs(message)
    message.remove(message[len(message) - 1])
    key_matrix = matrix(key)

    cipher = []
    for e in message:
        linha1, coluna1 = find_position(key_matrix, e[0])
        linha2, coluna2 = find_position(key_matrix, e[1])

        if linha1 == linha2:
            if coluna1 == 4: #este if's servem para que quando chega ao fim da coluna ou linha não ultrapasse o limite

                coluna1 = -1
            if coluna2 == 4:
                coluna2 = -1
            cipher.append(key_matrix[linha1][coluna1 + 1])
            cipher.append(key_matrix[linha1][coluna2 + 1])
        elif coluna1 == coluna2:
            if linha1 == 4:
                linha1 = -1;
            if linha2 == 4:
                linha2 = -1;
            cipher.append(key_matrix[linha1 + 1][coluna1])
            cipher.append(key_matrix[linha2 + 1][coluna2])
        else:
            cipher.append(key_matrix[linha1][coluna2])
            cipher.append(key_matrix[linha2][coluna1])
    return cipher


def cipher_to_digraphs(cipher):
    i = 0
    new = []
    for x in range(int(len(cipher) / 2)):
        new.append(cipher[i:i + 2])
        i = i + 2
    return new




def decrypt(cipher):
    cipher = cipher_to_digraphs(cipher)
    key_matrix = matrix(key)
    print(cipher)
    plaintext = []

    for e in cipher:
        linha1, coluna1 = find_position(key_matrix, e[0])
        linha2, coluna2 = find_position(key_matrix, e[1])

        if linha1 == linha2:
            if coluna1 == 4:
                coluna1 = -1
            if coluna2 == 4:
                coluna2 = -1
            plaintext.append(key_matrix[linha1][coluna1 - 1])
            plaintext.append(key_matrix[linha1][coluna2 - 1])

        elif coluna1 == coluna2:
            if linha1 == 4:
                linha1 = -1;
            if linha2 == 4:
                linha2 = -1;
            plaintext.append(key_matrix[linha1 - 1][coluna1])
            plaintext.append(key_matrix[linha2 - 1][coluna2])


        else:
            plaintext.append(key_matrix[linha1][coluna2])
            plaintext.append(key_matrix[linha2][coluna1])



    for unused in range(len(plaintext)):
        if "X" in plaintext:
            plaintext.remove("X")

    output = ""
    for e in plaintext:
        output += e
    print(output.lower())


#app.go()
print ("Playfair Cipher")
order=input("Choose :\n1,Encrypting \n2,Decrypting\n")
if order == "1":
	key= input("Please input the key : ")
	message= input("Please input the message : ").upper()
	print ("Encrypting: \n"+"Message: "+message)
	print ("Break the message into digraphs: ")
	print (message_to_digraphs(message))
	print ("Matrix: ")
	print (matrix(key))
	print ("Cipher: " )
	print (encrypt(message))
elif order == "2":
	key= input("Please input the key : ")
	cipher= input("Please input the cipher text: ")
	#cipher="ILSYQFBWBMLIAFFQ"
	print ("\nDecrypting: \n"+"Cipher: "+cipher)
	print ("Plaintext:")
	decrypt(cipher.upper())
else:
	print ("Error")

