def number_converter(numbers):                #Defining function
    num_converter = {                        #Dictionary containing numbers
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }

    output = ""
    for number in numbers:                          #for loop for accessing each digit from the entered numbers
        output += num_converter.get(number) + "  "
    return output
numbers=input("Phone > ")                            #number to be inputted by the user
print(number_converter(numbers))
