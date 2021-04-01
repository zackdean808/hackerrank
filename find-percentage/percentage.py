#!/bin/python

def generateAverage(sm, qName):
    avg = 0.00 
    
    return avg 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    average = []
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    

