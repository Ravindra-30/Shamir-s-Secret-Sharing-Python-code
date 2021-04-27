def y_x(x, p, key):
    a1=112
    return((a1*x+key)%p)

def lagrange(x0,x1,y0,y1,p):
    return round((-x1*y0/(x0-x1)+(-x0*y1/(x1-x0)))%p)

def re_construct(share1,share2,p):
    x0=share1[0]
    x1=share2[0]
    secret=[]
    for i in range(1,len(share1)):
        secret.append(lagrange(x0,x1,share1[i],share2[i],p))
    return secret
    
def generate_shares(secret,c):
    p=131
    share1=[1]
    share2=[2]
    share3=[3]
    share4=[4]
    for i in secret:
        share1.append(y_x(share1[0],p,i))
        share2.append(y_x(share2[0],p,i))
        share3.append(y_x(share3[0],p,i))
        share4.append(y_x(share4[0],p,i))
    print(f"share1:{share1}")
    shares1=""
    for i in range(1,len(share1)):
        shares1+=chr(share1[i])
    print(f"share1:{shares1}")
    print(f"share2:{share2}")
    shares2=""
    for i in range(1,len(share1)):
        shares2+=chr(share2[i])
    print(f"share2:{shares2}")
    print(f"share3:{share3}")
    shares3=""
    for i in range(1,len(share3)):
        shares3+=chr(share3[i])
    print(f"share3:{shares3}")
    print(f"share4:{share4}")
    shares4=""
    for i in range(1,len(share4)):
        shares4+=chr(share4[i])
    print(f"share4:{shares4}")
    dec_secret=re_construct(share1,share4,p)
    secret1=""
    for i in dec_secret:
        secret1+=chr(i)
    print(f"decrypted secret :{dec_secret}")
    print(f"decrypted secret :{secret1}")

if __name__=="__main__":
    secret=input("enter the secret:")
    ascii_values=[]
    for character in secret:
        ascii_values.append(ord(character))
    print(ascii_values)
	#253 is basically a random number chosen such that it is greator than all the the keys above
    generate_shares(ascii_values,127)