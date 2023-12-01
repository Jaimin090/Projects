is_valid = False
while not is_valid:

    password = input("Enter the password: ") # if pswrd length >= 8

    if len(password) >= 8:
        # is length ok
        has_lowercase = False
        has_uppercase = False
        has_digit = False
        #check if pswrd has all the necessary compopnents
        #lopp ]through all characters

        for ch in password:
            #if character is lowercase set has_lowercase to true
            if ch.islower:
                has_lowercase = True
                #if character is uppercase set has_uppercase to true
            if ch.isupper:
                has_uppercase = True
                # if character is a digit has_digit to true
            if ch.isdigit():
                has_digit = True
        #is_valid = has_lowercase AND has_uppercase and has_digit
        is_valid = has_lowercase and has_uppercase and has_digit
    if is_valid:
        print ("Valid password")
    else:
        print ("invalid password")