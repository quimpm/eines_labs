import math
import random

class Algorithms:

    @staticmethod
    def fermats_little_theorem(a,n):
        return (a**(n-1) % n) == 1

    @staticmethod
    def apply_fermat_to_number(n):
        for i in range(1,n):
            if Algorithms.gcd(i,n) == 1 and not Algorithms.fermats_little_theorem(i,n):
                return False
        return True

    @staticmethod
    def gcd(a, b):
        if a == 0:
            return b
        return Algorithms.gcd(b % a, a)

    @staticmethod
    def isPrime(n) : 
        if (n <= 1) : 
            return False
        if (n <= 3) : 
            return True
        if (n % 2 == 0 or n % 3 == 0) : 
            return False
        i = 5
        while(i * i <= n) : 
            if (n % i == 0 or n % (i + 2) == 0) : 
                return False
            i = i + 6
        return True

    @staticmethod
    def isCarmichael(n):
        if not Algorithms.isPrime(n) and Algorithms.apply_fermat_to_number(n):
            return True
        return False
    
    @staticmethod
    def miller_rabin_test(n):
        s, d = Algorithms.find_s_and_d(n) 
        return Algorithms.check_composite(n,d,s)

    @staticmethod
    def find_s_and_d(n):
        s = Algorithms.find_biggest_s_possible(n-1)
        while s > 0:
            d = 0
            while 2**(s) * d <= n-1:
                if 2**(s) * d == n-1:
                    return s, d
                d += 1
            s -= 1
        return s, n

    @staticmethod
    def find_biggest_s_possible(n):
        s = 0
        while 2**s <= n:
            s += 1
        return s-1

    @staticmethod
    def check_composite(n,d,s,k=3):
        while k > 0:
            a = random.randint(2,n-1)
            if a**(d) % n == 1:
                k -= 1
                continue
            r = 0
            if s == 0:
                s = 1
            step2 = True
            while r <= s-1 and step2:
                if a**(2**(r) * d) % n == -1 % n:
                    step2 = False
                r += 1
            if not step2:
                break
            return "Composite"
            k -= 1
        return "Prime"
            

def apply_fermat(n):
    print("Fermat litle theorem for n="+str(n))
    print("Result: "+str(Algorithms.apply_fermat_to_number(n)))

def apply_fermat_to_single_base(n,a):
    print("Fermat litle theorem for n="+str(n)+" a="+str(a))
    print("Result: "+str(Algorithms.fermats_little_theorem(a,n)))

def find_fermat_pseudoprime(a):
    print("Finding the first pseudoprime n for a="+str(a))
    found = False
    n = a
    while not found:
        n += 1
        if Algorithms.gcd(a,n) == 1 and Algorithms.fermats_little_theorem(a,n) and not Algorithms.isPrime(n):
            found = True
    print(str(n))

def get_all_carmichels_lower_than(number):
    print("Getting all carmaichels lower than "+str(number))
    carmichels = []
    for i in range(2, number):
        if Algorithms.isCarmichael(i):
            carmichels.append(i)
    print(str(carmichels))

def check_prime_fermat(n):
    print("Is prime "+str(n)+"? (Using Fermat)")
    print(str(Algorithms.apply_fermat_to_number(n)))

def apply_miller_rabin_test(n):
    print("Is prime "+str(n)+"? (Using Miller-Rabin)")
    print(str(Algorithms.miller_rabin_test(n)))


def main():
    apply_fermat(17)
    apply_fermat_to_single_base(124, 3)
    apply_fermat_to_single_base(124, 5)
    apply_fermat(561)
    find_fermat_pseudoprime(2)
    find_fermat_pseudoprime(3)
    get_all_carmichels_lower_than(10000)
    check_prime_fermat(323)
    check_prime_fermat(90751)
    apply_miller_rabin_test(1000009)
    apply_miller_rabin_test(15772929)
    apply_miller_rabin_test(2**(19)-1)
    apply_miller_rabin_test(2**(31)-1)



if __name__ == "__main__":
    main()