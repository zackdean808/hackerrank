#!/bin/python 

import re 

pattern = "[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}" 

def fun(s):
    # return True if s is a valid email, else return False
    #lf = lambda x: re.match(pattern, s)
    if re.match(pattern, s):
        return True
    elif not re.match(pattern, s):
        return False
    else:
        sys.exit(1)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
