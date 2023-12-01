def	get_gift_type():
    '''
	Ask for a valid gift type from the user, has to be Cash, Gift or Both
	Arguments:
        None
	Returns: 
        a valid gift type(cash, gift, both)
    '''
    gift_type = input("Enter gift type (Cash, Gift, Both): ").lower()
    while True:
        if gift_type in ["cash", "both", "gift"]:
            return gift_type.capitalize()
        else:
            gift_type = input("Enter gift type (Cash, Gift, Both): ").lower()

def check_for_more_gifts():
    '''
	Asks if there are more gifts to add. If yes then returns True else False
	Arguments:
        None
	Returns: 
        Y - True (if there are more gifts)
        N - False (if no more gifts)
    '''
    gift = input("Another Gift? (Y/N): ").lower()
    while True:
        if gift in ['y', 'n'] : 
           return gift
        else:
            gift = input("Another Gift? (Y/N): ")
            
# main function
my_file = open('weddingGifts.txt', 'a')
def main():
    print("Gift Registry\n")
    more_gifts = check_for_more_gifts()
    while more_gifts != 'n':
        name = input("Who is the gift from: ")
        gift_type = get_gift_type()

        if gift_type == 'Gift':
            amount = 0
            gift_description = input("Enter description of gift: ")
        elif gift_type == 'Cash':
            amount = int(input("Enter amount of cash gift: "))
            gift_description = ''
        else:
            amount = int(input("Enter amount of cash gift: "))
            gift_description = input("Enter description of gift: ")
        more_gifts = check_for_more_gifts()  # Update more_gifts within the loop
        my_file.write(f"{name} \t {gift_type} \t {amount:.1f} \t {gift_description}\n")
    print("File successfully written")

    my_file.close()
if __name__ == '__main__':
    main()