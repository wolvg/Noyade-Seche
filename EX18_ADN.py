def ADN(seq):
    Y = "est coupable."
    N = "n\'est pas coupable."


    if "CATA" in seq:
        seq1 = seq.replace("CATA","1111")
        if "ATGC" in seq1:
            return Y
        else:
            return N
    else:
        return N

A = "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCADN"
B = "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN"
C = "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCADN"
D = "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"

M = ADN(A)
print("Le Colonel Moutarde",M)

R = ADN(B)
print("Mlle Rose",R)

P = ADN(C)
print("Mme Pervenche",P)

L = ADN(D)
print("M. Leblanc",L)