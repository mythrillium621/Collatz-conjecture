
c0 = int(input("Type a number\n"))
count = 0

while c0 != 1:
    print(c0)
    count += 1
    
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3*c0+1

print(c0,"\nCollatz conjecture steps: ", count, "\n")