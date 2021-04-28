#!/bin/python 

def print_formatted(number):
    for i in range(1, number + 1):
        dec = str(i)
        octal = str(oct(i)[2:])
        hexadec = str(hex(i)[2:]).upper()
        binary = str(bin(i)[2:])
        width = len(binary) 
        s = dec + "\t" + octal + "\t" + hexadec + "\t" + binary
        #s = dec.rjust(width) + octal.rjust(width) + hexadec.rjust(width) + binary.rjust(width)
        print (s) 
        #print (dec,"\t",octal,"\t",hexadec,"\t",binary)
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
