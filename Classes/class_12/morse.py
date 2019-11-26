str2morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                   '(':'-.--.', ')':'-.--.-', ' ':'/'}

# Create the reverse dict
morse2str = {}
for letter, morse in str2morse.items():
    morse2str[morse] = letter

def decode_morse(my_morse):
    letters = my_morse.split(' ')
    decoded = ""
    for letter in letters:
        decoded += morse2str[letter]
    return decoded

def encode_string(my_string):
    morse_string = ""
    possible_symbols = list(str2morse.keys())

    for letter in my_string:
        letter = letter.upper()
        # This symbol doesn't exist in morse
        if letter not in possible_symbols:
            # Ignore it
            continue
        # It's not a space and it has a translation in morse
        else:
            # Add the morse translated letter
            translated = str2morse[letter]
            morse_string += translated

        morse_string += ' '

    morse_string = morse_string.strip()
    return morse_string



encoded_string = encode_string("Hello world I love python")
print(encoded_string)

decoded_string = decode_morse(encoded_string)

print(decoded_string)



