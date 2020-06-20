def main():
    #myfunc(10,20,30, fruit='orange', food='eggs', animal='dog')
    #print(myfunc1('America'))
    #print(myfunc2(8,5))
    #print(animal_crackers('Levelheaded Llama'))
    #print(animal_crackers('Crazy Kangaroo'))
    #print(return_20(2,3))
    #print(old_macdonald('macdonald'))
    #return_reverse_string('We are ready')
    #print(almost_there(104))
    #print(has_33([1,3,1]))
    #print(paper_doll('Mississippi'))
    #print(blackjack(9,9,11))
    #print(summer_69([4,5,6,7,8,9,9]))
    #print(spy_game([1,7,2,0,4,5,0]))
    i = int(input('Enter the number: '))
    count = 0

    for i in range(i):
        # print(i)
        b = count_primes(i)
        if b:
            count = count + 1
        else:
            continue
    print('the count is = ', count - 1)

def count_primes(m):
    if m == 1:
        return False
    if m == 2:
        return True
    for i in range(2, m):
        #print(i)
        if m % i == 0:
            return False
    return True



    if m == 1:
        return True
    for i in range(2,int(m)):
        if m % i == 0:
            return True
    return False

def spy_game(lst1):
    lst2=[]
    for num in lst1:
        if num == 0 or num == 7:
            lst2.append(num)
    if lst2 == [0,0,7]:
        return True
    else:
        return False


def summer_69(lst):
    i1=0
    i2=0
    num=0
    sum=0
    count = 0
    count1 = 0
    for k in lst:
        if count<2 and count1<2:
            if k==6:
                i1=lst.index(k)
                count = count +1
                a = True
                print(a)
                continue
            if k==9:
                i2=lst.index(k)
                count1 = count1 + 1
                b = True
                print(b)
                continue
            else:
                num=num+k

    if 6 in lst or 9 in lst:
        if a == True or b == True:
            for l in range(i1+1,i2):
                num = num - lst[l]
            #print(num)


    return num


def blackjack(a,b,c):
    while 1<=a<=11 and 1<=b<=11 and 1<=c<=11:
         if a+b+c<=21:
             return a+b+c
         elif a+b+c>21 and a==11 or b==11 or c==11:
             return (a+b+c)-10
         elif a+b+c>21:
            return 'BUST'

def paper_doll(str):
    str1=''
    for i in range(len(str)):
        str1 = str1 + (str[i]*3)
    return str1

def has_33(lst):
    for i in range(len(lst)):
        if lst[i] == lst[i+1] and lst[i]==3 and lst[i+1]==3:
            b= True
            break
        else:
            b= False
    return b



def almost_there(int1)    :
    if 90<+int1<=110 or 190<=int1<=210:
        return True
    else:
        return False

def return_20(a,b):
    if a+b==20 or a==20 or b==20:
        return True
    else:
        return False

def old_macdonald(name):
    print(name[0], name[3])
    str1=''
    for i in range(len(name)):

        if i==0 or i==3:
            str1= str1 + name[i].upper()
        else:
            str1= str1 + name[i]
    return str1

def return_reverse_string(str1):
    lst = str1.split()
    x = 0

    for i in range(len(lst)):
        x= len(lst)-(i+1)
        print(lst[x], end = ' ')



def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[1],kwargs['food']))

def myfunc1(str1):

    str2 =''

    for i in range(len(str1)):
        if i%2==0:
            str2 = str2 + str1[i].upper()
            #print(str2)
            #print(i)
        else:
            str2 = str2 + str1[i].lower()
            #print(str2)
            #print(i)
    return str2

def myfunc2(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return a
        else:
            return b
    elif a%2 !=0 or b%2 !=0:
        if a>b:
            return a
        else:
            return b


def animal_crackers(words):
    lst=words.split()
    print(lst[0], lst[1])
    for word in lst:
        #print(lst)

        if lst[0][0] == lst[1][0]:
            return True
        else:
            return False







if __name__ == '__main__':
    main()