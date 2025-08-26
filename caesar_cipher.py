def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet+alphabet
    return doubleAlphabet
    
# val = getDoubleAlphabet('AWS')
# print("getDoubleAlphabet()", val) # Function debug


def getMessage():
    stringToEncript = input("Please enter a message to encript: ")
    return stringToEncript
    
# myMsg = getMessage()
# print("getMessage()", myMsg) # Function debug

def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
    
# print('chipperKey()', chipperKey())

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = "" # Variable untuk menampung hasil enkripsi
    uppercaseMessage = "" # Variable untuk menampung kata yang akan di enkripsi dibuat besar
    uppercaseMessage = message.upper() # Mengisi variable uppercaseMessage menggunakan inputan message di convert jadi besar
    
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter) # Mencari indeks berapa karakter input di key enkripsi
        newPosition = position + int(cipherKey) # Indeks key yang ditemukan, akan ditambakan dengan input shifting
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition] # Tambhkan karakter hasil enkripsi baru ke proses enkripsi sebelumnya
        else:
            encryptedMessage = encryptedMessage + currentCharacter # Jika kata tidak ditemukan dalam key, maka balikkan karakter aslinya
    return encryptedMessage
    
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Bahan untuk key enkripsi. Salt
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet) # ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ Untuk shifting agar z juga bisa di shift ke kanan
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage() # Menerima iputan dari user
    print(myMessage)
    myCipherKey = getCipherKey() # Menerima inputan dari user mau shifting berapa karakter. Ex: shift 3, maka 'a' -> 'd'
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2) # Function untuk lakukan shifting. Arguments: Kata yang mau di encript, berapa banyak shiftignya, key untuk enkripsi
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2) # Function untuk decript
    print(f'Decypted Message: {myDecryptedMessage}')


runCaesarCipherProgram()