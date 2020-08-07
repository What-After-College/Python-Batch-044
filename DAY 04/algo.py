def lcm(n1, n2):
    if(n1>n2):
        small=n2
    else:
        small=n1
    for i in range(1,small+1):
        if(n1%i==0 and n2%i==0):
            hcf=i

    lcm = (n1*n2)/hcf
    return lcm

def hcf(n1, n2):
    if(n1>n2):
        small=n2
    else:
        small=n1
    for i in range(1,small+1):
        if(n1%i==0 and n2%i==0):
            hcf=i
    return hcf


def isprime(n):
    factor=0
    for i in range(2,n):
        if(n%i==0):
            factor+=1
            break
    if(factor>0):
        return False
    else:
        return True


if __name__ == '__main__':
    print("hello world")

    
