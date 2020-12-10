from copy import copy

# value of r (for a K_r,r)
r = 5

def gen(k):
    # Generates an algebraic cycle with the following rule:
    #   consecutive elements differ by k (mod r)

    i = 0
    ls = []

    while not (i in ls):
        ls.append(i)
        i = (i + k) % (r)

    return ls


def compose(c1, c2, p=False):
    # Composes the algebraic cycles c1 then c2 (given as lists)
    # !!! Stops upon formation of a cycle !!!
    # arg p determines whether or not to print the process
    
    out = []
    i = c1[0]
    while not (i in out):
        out.append(i)
        next1 = c1[(c1.index(i)+1) % r]
        next2 = c2[(c2.index(next1)+1) % r]
        i = next2
        #print(i)

    if p:
        print("COMPOSING")
        print(c1, "then")
        print(c2, "equals:")
        print(out)


    return out


def main():


    # print("\n#####","r =", r, "#####\n")

    # # Set of all nontrivial matchings that can be expressed as an algebraic r-cycle
    # # (so as to form a perfect pair with the trivial matching, represented by the identity permutation on Sr)
    # ms = []
    # for n in range(1,r):
    #     m = gen(n)
    #     if len(m) == r:
    #         ms.append(m)

    # print("%i MATCHING CANDIDATES:" %len(ms))
    # for m in ms: print(m)
    # print()


    # # To store compositions of all pairs (x, y^-1) from list ms
    # cs = []
    # for i in range(len(ms)):
    #     for j in range(i+1, len(ms)):
    #         m1, m2 = copy(ms[i]), copy(ms[j])
    #         m2.reverse()
    #         cs.append(compose(m1, m2))

    # print("ALL COMPOSITIONS OF PAIRS FROM ABOVE:")
    # for c in cs: print(c)



    # Very important for the for loop:
    global r

    for ri in range(100):
        perf = True
        r = ri
        # print("\n#####","r =", r, "#####\n")


        # stores all matchings of length r
        ms = []
        for n in range(1,r):
            m = gen(n)
            if len(m) == r:
                ms.append(m)

        if len(ms) < (r-1):
            continue

        
        # To store compositions of all pairs (x, y^-1) from list ms
        cs = []
        for i in range(len(ms)):
            for j in range(i+1, len(ms)):
                m1, m2 = copy(ms[i]), copy(ms[j])
                m2.reverse()
                cs.append(compose(m1, m2))
        
        for c in cs:
            if len(c) < r:
                perf = False

        # if made it this far, K_r,r has a perfect 1-factorization!
        if perf: print(r)





    return

if __name__ == '__main__':
    main()