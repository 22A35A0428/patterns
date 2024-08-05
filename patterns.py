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

# triangle 3
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    print()

# triangle 4
for i in range(n):
    for j in range(i+1,n):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()

# pyramiid 1
for i in range(n):
    for j in range(i+1,n):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print()

# pyramid 2
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n-1):
        print('*',end='')
    for j in range(i,n):
        print('*',end='')
    print()


# Dimond 1
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


# Dimond 2
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(n-1):
    for j in range(i+1,n):
        print('*',end='')
    print()

# Dimond 3
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