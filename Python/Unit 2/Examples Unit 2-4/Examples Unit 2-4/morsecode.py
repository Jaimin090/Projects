# solution
morseCode = {'A':'.-', 'B': '-...', 'C':'-.-.', 'D':'=..', 'E':'.',
             'F':'..=.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
             'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O': '---', 'P':'.--.',
             'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
             'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}
message = input ('Enter the message stop to quit:')
while message != 'stop':
    # loop through all the characters in the message
    for ch in message:
        # look up corresponding morse code based on the character
        if ch == ' ':
            print (' ', end = '')
        else:
            morse = morseCode.get(ch.upper(), 'ERROR')
            print (morse, end= '')
    # advance to a newline
    print ()
    message = input ('Enter the message stop to quit:')


        
    

 

