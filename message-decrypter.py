alphabet = 'zyxwvutsrqponmlkjihgfedcba'
special = '[@_!#$%^&*()<>?/\|}{~:]1234567890'
keySpecial = 'abcdefghijklmnopqrstuvwxyz[@_!#$%^&*()<>?/\|}{~:]'
newMessage = ''

message = input('Please enter a message to decrypt: ').lower()
if len(message) < 2:
    print('Message needs to be at least 2 characters, exiting program')
    exit()

specialInMessage = [c for c in special if c in message]
if specialInMessage:
    print('Invalid character found in message, exiting program')
    exit()
        
key = input('Please enter a key from 1-26: ')
SpecialInMessage = [c for c in keySpecial if c in key]
if SpecialInMessage:
    print('Invalid character found in key, exiting program')
    exit()
key = int(key)
if key < 1 or key > 26:
    print('Invalid character found in key, exiting program')
    exit()

while True:
    for character in message:
      if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
      else:
        newMessage += character

print('Your new message is: ', newMessage)
answer = input('Yes or No?').lower()
if answer == 'yes':
    exit()
if answer == 'no':
      for character in message:
      if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26+1
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
      else:
        newMessage += character
