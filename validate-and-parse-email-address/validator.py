#!/bin/bash 



def solve(s):
    pattern = "[a-zA-Z]{1,}[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}"
    if re.match(pattern, s):
        return "YES"
    elif not re.match(pattern, s):
        return "NO"
    else:
        sys.exit(1)

if __name__ == '__main__':
    N = int(input())
    for i in range(0, N):
        s = tuple(input())
        result = solve(s)
        print (result)

