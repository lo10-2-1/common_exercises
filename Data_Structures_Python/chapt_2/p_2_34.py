from string import ascii_lowercase

def list_of_frequences(string: str):
    '''Counts frequencies of each alphabet character in the string. 
    Input - string, output - list of frequencies (numbers)
    '''
    frequency_list = []
    quantity = 0
    for letter in ascii_lowercase:
        for i in range(len(string)):
            if  letter == string[i]:
                quantity += 1
        frequency_list.append(quantity)
        quantity = 0
    return frequency_list

main_string = input()
frequencies = []
frequencies = list_of_frequences(main_string)
print(frequencies)