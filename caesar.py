def alphabet_position(letter):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    position = alpha.index(letter.lower())
    return(position)

def rotate_character(char,rot):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char.isalpha():
        rotated_index = alphabet_position(char)+rot
        if rotated_index < 26:
            if char.isupper():
                encrypted = ALPHA[rotated_index]
            else:
                encrypted = alpha[rotated_index]
        elif char.isupper():
            encrypted = ALPHA[rotated_index%26]
        else:
            encrypted = alpha[rotated_index%26]
    else:
        encrypted = char
    return(encrypted)

def encrypt(text,rot):
    encrypted_text=''
    for i in range(len(text)):
        encrypted = rotate_character(text[i],rot)
        encrypted_text += encrypted
    return(encrypted_text)
