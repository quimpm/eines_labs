import math

class Algorithms:

    @staticmethod    
    def calculate_fi(p,q):
        return (p-1)*(q-1)

    @staticmethod
    def fermat_factoring(n):
        k = math.ceil(math.sqrt(n))
        h = k**2 - n
        sh = math.sqrt(h)
        while sh != int(sh):
            k = k + 1
            h = k**2 - n
            sh = math.sqrt(h)
        return k+sh, k-sh

    @staticmethod
    def get_private_key(e, fi):
        _,s,_  = Algorithms.euclideanExtended(e, fi)
        return s

    @staticmethod
    def euclideanExtended(a, b):
        if a == 0 :   
            return b,0,1
        gcd,s1,t1 = Algorithms.euclideanExtended(b%a, a)    
        s = t1 - (b//a) * s1  
        t = s1  
        return gcd,s,t 

    @staticmethod
    def decrypt(c, n, d):
        return c**(d) % n

# S'ha agafat l'exemple de l'enunciat del 19-20 ja que n era massa gran
def main(n=17947, e=3929):
    p,q = Algorithms.fermat_factoring(n)
    print("p:"+str(p)+", q:"+str(q))
    fi = Algorithms.calculate_fi(p,q)
    print("fi:"+str(fi))
    e = 11787
    d = Algorithms.get_private_key(e, fi)
    print("d:"+str(d))
    c = 6808
    m = Algorithms.decrypt(c,n,d)
    print("m:"+str(m))
    c = 4867
    m = Algorithms.decrypt(c,n,d)
    print("m:"+str(m))

if __name__ == "__main__":
    main()