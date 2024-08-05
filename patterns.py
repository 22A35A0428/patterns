n=5
# square 
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()

# triangle 1
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()

# triangle 2
for i in range(n):
    for j in range(i,n):
        print('*',end='')
    print()

# inverse triangle 1
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    print()

#  inverse triangle 2
for i in range(n):
    for j in range(i+1,n):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()

# pyramiid 
for i in range(n):
    for j in range(i+1,n):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print()

#  inverse pyramid 
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n-1):
        print('*',end='')
    for j in range(i,n):
        print('*',end='')
    print()


# Dimond 
for i in range(n-1):
    for j in range(i+1,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n-1):
        print('*',end='')
    for j in range(i,n):
        print('*',end='')
    print()


# right  part Dimond 
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(n-1):
    for j in range(i+1,n):
        print('*',end='')
    print()

# left part Dimond 
for i in range(n):
    for j in range(i+1,n):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(n-1):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i+1,n):
        print('*',end='')
    print()
