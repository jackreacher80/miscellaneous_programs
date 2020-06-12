def main():
    number = input('Please enter the number of your choice: ')
    l = len(number)

    dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine'}
    #num_of_digits(len,number)

    if l == 1:
        single_digit(int(number),dict)
    elif l == 2:
        double_digit(int(number), dict)






#def num_of_digits(len,num):
    switcher = {
        #1: single_digit(str(num)),
        #2: double_digit(str(num)),
        #3: triple_digit(str(num))
    }

def single_digit(num,dict):
    #dict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    for key in dict:
        if key == num:
            print(dict[num])


def double_digit(num, dict):
    str1= str(num)
    dict1 = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 8: 'eighteen',
            19: 'nineteen'}
    dict2 = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninty'}

    for key in dict1:
        if key == num:
            print(dict1[num])
            #return dict1[num]

    for i in range(2):
        if num % 10 == 0:
            break
        str1= str(num)
        #print(num)
        str3 = ''
        str4 = ''
        if i == 0:
            for key in dict2:
                if key == int(str1[i]) * 10:
                    str3 = str3 + dict2[key]
                    print(str3, end ="")

        else:
            for key in dict:
                if key == int(str1[i]):
                    str4 = str4 + ' ' + dict[key]
                    print(str4)












#def triple_digit(num):

















if __name__ == '__main__':
    main()