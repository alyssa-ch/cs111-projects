# Your name: Alyssa Choi, Crystal Luo
# Your username: ac111, cl103
# CS111 Fall 2020 PS07 Task 3
# similarities.py
# Submission date: 13 October 2020

#---------------# # Provided Code #
#---------------#

def matchingBase(base):
    """
    Given a base ('A', 'T', 'G', or 'C') this function returns the
    matching base ('T' for 'A', 'C' for 'G', and vice versa).
    """
    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'A'
    elif base == 'G':
        return 'C'
    elif base == 'C':
        return 'G'
    else:
        raise ValueError("{} is not a valid DNA base!".format(repr(base)))


#-----------#
# Your Code #
#-----------#

def countBases(sequence, base):
    """
    countBases takes two arguments: the sequence of bases to inspect,
    and the base to look for. It returns how many copies of that base exist
    within the given sequence (an integer).
    """
    # TODO: Write me
    if len(sequence) == 0:
        return 0
    else:
        if base == sequence[0]:
            return 1 + countBases(sequence[1:], base)
        else:
            return countBases(sequence[1:], base)


def symmetricStrand(sequence):
    """
    symmetricStrand accepts just one argument: the sequence to create
    a complimentary strand for. It returns a string of the same length
    representing the complimentary strand, where each 'A' has been swapped for
    a 'T', each 'T' for an 'A', each 'G' for a 'C', and each 'C' for a 'G'.
    """
    # TODO: Write me
    if len(sequence) ==0:
        return ""
    else: 
        if sequence[0] == "A":
            return "T" + symmetricStrand(sequence[1:])
        elif sequence[0] == "T":
            return "A" + symmetricStrand(sequence[1:])
        elif sequence[0] == "G":
            return "C" + symmetricStrand(sequence[1:])
        elif sequence[0] == "C":
            return "G" + symmetricStrand(sequence[1:])


def onlyTA(sequence):
    """
    onlyTA accepts one argument: the sequence to process. It returns a
    new string where each 'G' and 'C' base has been removed, leaving only
    the 'A' and 'T' bases.
    """
    # TODO: Write me
    if len(sequence) == 0:
        return ""
    else:
        if sequence[0] == "A":
            return "A" + onlyTA(sequence[1:])
        if sequence[0] == "T":
            return "T" + onlyTA(sequence[1:])
        elif sequence[0] == "G":
            return "" + onlyTA(sequence[1:])
        elif sequence[0] == "C":
            return "" + onlyTA(sequence[1:])
        


def unmatchedCount(sequence1, sequence2):
    """
    unmatchedCount takes two arguments representing two sequences of DNA
    (which will always have the same length). Its job is to return the number
    of positions where the two sequences are mismatched, meaning that the base
    from one sequence is not the correct matching base for the base from the
    other sequence.
    """
    # TODO: Write me
    if len(sequence1) == 0 or len(sequence2) == 0:
        return 0
    else:
        if matchingBase(sequence1[0]) == "T" and matchingBase(sequence2[0]) == "A":
            return 0 + unmatchedCount(sequence1[1:], sequence2[1:])
        elif sequence1[0] == "T" and sequence2[0] == "A":
            return 0 + unmatchedCount(sequence1[1:], sequence2[1:])
        elif sequence1[0] == "C" and sequence2[0] == "G":
            return 0 + unmatchedCount(sequence1[1:], sequence2[1:])
        elif sequence1[0] == "G" and sequence2[0] == "C":
            return 0 + unmatchedCount(sequence1[1:], sequence2[1:])
        else:
            return 1 + unmatchedCount(sequence1[1:], sequence2[1:])


def cutOut(sequence, target):
    """
    cutOut takes two arguments: a string representing a sequence of DNA bases,
    and a (usually shorter) target sequence. It should find all places in the
    first sequence where the target sequence exists and remove those, returning
    what remains of the first sequence.
    """
    # TODO: Write me
    if len(target) > len(sequence):
        return sequence
    else: 
        if sequence.startswith(target):
            return cutOut(sequence[len(target):], target)
        else:
            return sequence[0] + cutOut(sequence[1:], target)

#--------------#
# Testing Code #
#--------------#

if __name__ == "__main__":
    print("Start of testing...")
    print("countBases")
    print(countBases("GATTACA", "A"), "== 3?")
    print(countBases("TATATA", "T"), "== 3?")
    print(countBases("TATATA", "G"), "== 0?")
    print(countBases("T", "T"), "== 1?")
    print(countBases("", "T"), "== 0?")
    print()

    print("symmetricStrand")
    print(symmetricStrand("GACT"), "== 'CTGA'?")
    print(symmetricStrand("ATC"), "== 'TAG'?")
    print(symmetricStrand("CATAGAG"), "== 'GTATCTC'?")
    print()

    print("onlyTA")
    print(onlyTA("ATGCACTA"), "== 'ATATA'?")
    print(onlyTA("AT"), "== 'AT'?")
    print(onlyTA("GCG"), "== ''?")
    print(onlyTA("GAGCTCG"), "== 'AT'?")
    print()

    print("unmatchedCount")
    print(unmatchedCount("AAA", "TTT"), "== 0?")
    print(unmatchedCount("AAA", "TTC"), "== 1?")
    print(unmatchedCount("AAA", "GGG"), "== 3?")
    print(unmatchedCount("GATTACA", "CTAATGT"), "== 0?")
    print(unmatchedCount("GATTACA", "CGATTGT"), "== 2?")

    print("cutOut")
    print(cutOut("GATTACA", "ATTA"), "== 'GCA'?")
    print(cutOut("TAGAGCGAT", "AG"), "== 'TCGAT'?")
    print(cutOut("ATTGCCAG", "C"), "== 'ATTGAG'?")
    print(cutOut("TATATATAT", "TAT"), "== 'AAT'?")
    print()
    print("...end of testing.")
