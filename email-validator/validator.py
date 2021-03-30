#!/bin/python 

import re 

# This makes the magic happen
pattern = "[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$" 

def fun(s):
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
