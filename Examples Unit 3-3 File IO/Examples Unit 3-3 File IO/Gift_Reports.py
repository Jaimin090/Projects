# weddingGifts.txt 
my_file= open('weddingGifts.txt', 'r')

def main():
    total = 0
    counter = 0
    for line in my_file:
        elements = line.rstrip().split()
        cash = 0
        counter += 1
        for element in elements:
            # ALternate Way
      # for a in elements:
              # a = elements[2]
              # cash = float(a)
              # total += cash

                # Line 17 completely taken from ChatGPT                                                 
                # '.' in element used to check if the element is a float(exclude int and strings) as to calculate the total
                # element.replace('.', '').isdigit() removes the dot and .isdigit() checks to see if the element has string in it (eg: $) can be removed and still the code will run
                # Error: could not convert string to float: '$50.0' (error if there was a $ sign before 50.0 in txt file, 
                # for this problem we could again use .replace for '$' to '' to include $50.0 in cash recieved)
            if '.' in element and element.replace('.', '').isdigit():   
                cash = float(element)
        total += cash
    my_file.close()
    print(f"Received {counter} items including cash totalling ${total:,.2f}")
if __name__ == '__main__':
    main()
   # (for me)if "gift" in line or "GIFT" in line:(nxt part) or .upper()