#Eratosthenes' shieve
def Era(n):
    l = [2]
    for i in range(3,n+1):
        flag = True
        for j in l:
            if i%j==0:flag = False
        if flag:l.append(i)
    return l

def main(n):
    l = Era(n)
    flag = False
    for q in l:
        for w in l:
            for e in l:
                if q+w+e == n and q!=w and q!=e and w!=e: flag = True
                if flag:
                    x = q
                    y = w
                    z = e
                    break;
            if flag: break
        if flag: break
    return [x,y,z]

n = int(input("Give an odd integer N: "))
print(main(n))
        
                
