import math

class Algorithms:

    @staticmethod
    def bsgs(p,g,y):
        s = math.ceil(math.sqrt(p)) 
        bs = []
        gs = []
        for i in range(s+1):
            bs.append((y*g**(i) % p, i))
            gs.append((g**(s*i) % p,i))
        print(bs)
        print(gs)
        matches=[]
        for i,_bs in enumerate(bs):
            for j,_gs in enumerate(gs):
                if _bs[0] == _gs[0]:
                    matches.append((i,j, _bs))
        return matches
                       

def apply_bsgs(p,g,y):
    print("Apply BSGS p:"+str(p)+", g:"+str(g)+", y:"+str(y))
    matches = Algorithms.bsgs(p,g,y)
    for match in matches:
        print(str(match[1])+" * "+str(match[2][0])+" - "+str(match[0])+" = "+str(match[1]*match[2][0]-match[0]))

def main():
    apply_bsgs(29,3,12)
    apply_bsgs(71,13,19)
    apply_bsgs(143,7,50)
    apply_bsgs(19,10,2)

if __name__ == "__main__":
    main()