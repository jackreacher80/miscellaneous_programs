import sys
import math

def main():
    coefficient_a= int(input('Please enter coefficient-a: '))
    coefficient_b = int(input('Please enter coefficient-b: '))
    coefficient_c = int(input('Please enter coefficient-c: '))

    print("The roots of the equation will be- " , calculate_roots(coefficient_a, coefficient_b, coefficient_c))


def calculate_roots(a,b,c):

    root1 = ((b*(-1)) + math.sqrt(((b**2)-(4*a*c))))/(2*a)
    root2 = ((b*(-1)) - math.sqrt(((b**2)-(4*a*c))))/(2*a)
    return root1, root2

if __name__ == '__main__':
    main()