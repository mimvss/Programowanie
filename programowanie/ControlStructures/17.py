###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    if char.isalpha():
        original_code = ord(char)

        # add one to the character's code 
        if char == 'Z':
            new_code = ord('A')
        elif char == 'z':
            new_code = ord('a')
        else:
            new_code = original_code + 1

        # replace new character code with its
        # corresponding character (use chr())
        new_char = chr(new_code)

        # add encrypted character to encrypted text
        encrypted_text += new_char

    else:
        # keep non-letters unchanged
        encrypted_text += char

print(plain_text)
print(encrypted_text)
