fact = int(input("Enter the valid factorial :-"))
tempf = fact
i = 2
while (tempf > 0):
    if(tempf % i == 0):
        tempf = tempf/i
        if(tempf == 1):
            print "",fact,"is factorial of",i
            break

        i = i + 1
    else:
        print "",fact,"is not a factorial"
        break;
    
