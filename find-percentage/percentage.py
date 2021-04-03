#!/bin/python
if __name__ == '__main__':
    avg_total = 0.00 
    avg = 0.00 
    n = int(input())
    student_marks = {}
    average = []
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for s in student_marks[query_name]:
        avg_total += float(s)

    avg = avg_total / len(student_marks[query_name]) 
    print ("{:.2f}".format(avg))


