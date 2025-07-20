card_number = '4111-1111-4555-1142' # Variable to enter our card_number

def main(): # Defining our main function for our output
    card_translation = str.maketrans({'-': '', ' ': ''})    # Defining our translation table in order to get rid of dashes and spaces
    translated_card_number = card_number.translate(card_translation)    # Translating our `card_number` into a clean string of numbers

    if verify_card_number(translated_card_number):  # Execute our verification function with the main parameter being `translated_card_number`
        print('VALID!')
    else:
        print('INVALID!')



def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]    # Retrieve a reversed version of our card by starting from the end and going back
    odd_digits = card_number_reversed[::2]  # Retrieve only odd digits by beginning at index 0 and selecting every other digit

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]

    # Find the sum of all odd digits, by converting `digit` (a string) into integers
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    # Find the sum of all even digits, by converting `digit` (a string) into integers and multiplying them by two
    for digit in even_digits:
        number = int(digit) * 2
        # If the product of doubling is larger than ten, add together the tens (floor division) and units (modulo)
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number    

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

main()