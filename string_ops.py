def main():
    #string_results('Let us start attending Stanford University Lectures')
    #print_integers(1, 16)
    st = 'Create a list of the first letters of every word in this string'
    print(list_comprehensions(st))


def list_comprehensions(st):
    lst = st.split()
    lst2 = [word[0] for word in lst]
    lst3 = [print(word) for word in lst if len(word)%2 == 0]

    return lst3





def string_results(str1):
    count =1
    char =0
    start=0
    list1 = str1.split()
    for word in str1:
        char =char + 1
        if word == ' ':
            count= count+1
    print(char,count)
    print([x for x in list1 if  'S' and 's' in x])

def print_integers(m,n):
    for i in range(m,n):
        if i % 3 == 0 and i %5 == 0:
            print('FizzBuzz')

        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 ==0:
            print('Buzz')
        else:
            print(i)

























if __name__ == '__main__':
    main()