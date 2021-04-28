#!/bin/python 

def print_formatted(number):
    for i in range(1, number + 1):
        dec = i
        octal = oct(i)[2:]
        hexadec = hex(i)[2:]
        binary = bin(i)[2:]
        print (dec,"\t",octal,"\t",hexadec,"\t",binary)
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
