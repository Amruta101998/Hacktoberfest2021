from cryptography.fernet import Fernet

def getMyKey():
    abc = open("PasswordKey.key",'rb')
    return abc.read()

def encryptMessage(message_normal):
    key = getMyKey()
    k = Fernet(key)
    encrypted_Message = k.encrypt(message_normal)
    return encrypted_Message

def decryptMessage(message_secret):
    key = getMyKey()
    k = Fernet(key)
    decrypted_Message = k.decrypt(message_secret)
    return decrypted_Message

encryptMessage(b" HEY PYTHON LEARNER")

decryptMessage(b'gAAAAABhbBReu34y2Z5wPDu_2GHtdtSdXl3iLvwYtOk8F5pIc9HToKfJmGLWXbCYiwhWTFE77_f3J_S0_plkssSoSOzS6pdOEfEWoOSTg7BNao5S_49NgJc=')