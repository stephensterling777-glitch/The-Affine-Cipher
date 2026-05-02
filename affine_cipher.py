#Cryptography 2: The Affine Cipher
#Stephen Sterling
import string
import math
character_list=string.ascii_lowercase

#the input asks for a message that will be either encrypted or decrypted
message = input('What is your message? ')
message=message.lower() #this can be changed for different character list
#asks user for keys
alpha = input('What is the multiplicative key? ')
alpha = int(alpha) % len(character_list)
beta = input('What is the additive key? ')
#make sure alpha is valid
def validation(alpha):
    if math.gcd(alpha, len(character_list)) == 1:
        return True
    else:
        return False
#makes sure key is within group bounds
beta = int(beta) % len(character_list)

alpha_valid = validation(alpha)

#create a list of numbers that are invertible under modular multiplication
invertible_list = []
for i in range(len(character_list)):
    if math.gcd(i, len(character_list)) == 1:
        invertible_list.append(i)


def encrypt_message(message, alpha, beta):
    encrypted_message = ''
    for i in range(len(message)):
        if message[i] in character_list:
            location = character_list.find(message[i])
            encrypted_message += character_list[(location*alpha +beta)% len(character_list)]
        else:
            encrypted_message += message[i]
    return encrypted_message

def decrypt_message(message, alpha, beta):
    decrypted_message = ''
    #here we call the invertible list to find out which number is the inverse of alpha
    for j in invertible_list:
        if (j*alpha % len(character_list)) == 1:
            key = j
    for i in range(len(message)):
        if message[i] in character_list:
            location = character_list.find(message[i])
            decrypted_message += character_list[((location-beta)*key)% len(character_list)]
        else:
            decrypted_message += message[i]
    return decrypted_message
mode = input('Encrypt of decrypt? (e/d)').strip().lower()
if alpha_valid == True:
    if mode == 'e':
        print(encrypt_message(message, alpha, beta))
    elif mode == 'd':
        print(decrypt_message(message, alpha, beta))
    else:
        print('Invalid mode input')
else:
    #we send a message in case the user choses invalid alpha
    print('The multiplicative key that you chose is invalid.')
    print('Please chose a key such that gcd('+str(len(character_list))+',key)=1.')
    


