import sys
import math

class Algorithms():

    def __init__(self): 
        self.n_euclidean = 0
        self.n_extended_euclidean = 0

    def euclidean_division(self, a, b):
        return a//b, a%b

    def trial_division(self,n):
        factors = []
        first_possible_factor = 2
        while n  > 1:
            if n % first_possible_factor == 0:
                factors.append(first_possible_factor)
                n /= first_possible_factor
            else:
                first_possible_factor += 1
        return factors

    def euclidean(self, a, b):
        self.n_euclidean += 1
        if a == 0:
            return b
        return self.euclidean(b % a, a)

    def euclideanExtended(self, a, b):
        self.n_extended_euclidean += 1  
        if a == 0 :   
            return b,0,1
        gcd,s1,t1 = self.euclideanExtended(b%a, a)    
        s = t1 - (b//a) * s1  
        t = s1  
        return gcd,s,t 

def find_smallest_after_than(alg, n=10010):
    is_prime = False
    while not is_prime:
        if  len(alg.trial_division(n)) == 1:
            is_prime = True
        else:
            n +=1
    return n

def main():
    alg = Algorithms()
    print("Euclidean Division-------------------------------")
    q, r = alg.euclidean_division(103, 11)
    print("q: "+str(q)+', '+"r: "+str(r))
    print("Trial Division-----------------------------------")
    factors = alg.trial_division(100)
    print(factors.__str__())
    print("Euclidean----------------------------------------")
    gcd = alg.euclidean(6, 18)
    print("gcd: "+str(gcd)+", number of steps: "+str(alg.n_euclidean))
    print("Extended Euclidean-------------------------------")
    gcd,s,t = alg.euclideanExtended(6,18)
    print("gcd: "+str(gcd)+", s: "+str(s)+", t: "+str(t)+ ", number of steps: "+str(alg.n_extended_euclidean))
    print("Next prime after 10010---------------------------")
    prime = find_smallest_after_than(alg)
    print("next_prime: "+ str(prime))
    print("a^-1 mod b---------------------------------------")
    a = 28736540321
    b = 487669403177
    gcd, s, t = alg.euclideanExtended(a, b)
    print("a^-1 mod b: "+str(s))
    a = 12586269025
    b = 20365011074
    gcd, s, t = alg.euclideanExtended(a, b)
    print("a^-1 mod b: "+str(s))

if __name__ == "__main__":
    main()