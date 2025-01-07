def solution(dna_sequence):
    # Please write your code here
    dna_sequence_min = dna_sequence
    n = len(dna_sequence)
    i = 0
    while i < n:
        if(dna_sequence[i:n] + dna_sequence[0:i]) < dna_sequence_min:
            dna_sequence_min = dna_sequence[i:n] + dna_sequence[0:i]
        i += 1
    return dna_sequence_min

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("ATCA") == "AATC")
    print(solution("CGAGTC") == "AGTCCG")
    print(solution("TCATGGAGTGCTCCTGGAGGCTGAGTCCATCTCCAGTAG") == "AGGCTGAGTCCATCTCCAGTAGTCATGGAGTGCTCCTGG")