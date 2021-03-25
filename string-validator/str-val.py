#!/bin/python 

if __name__ == '__main__':
    string = input()

    isAlnum = any(char.isalnum() for char in string)
    isAlpha = any(char.isalpha() for char in string) 
    isDigit = any(char.isdigit() for char in string)
    isLower = any(char.islower() for char in string)
    isUpper = any(char.isupper() for char in string)
    print (isAlnum)
    print (isAlpha)
    print (isDigit) 
    print (isLower)
    print (isUpper) 
