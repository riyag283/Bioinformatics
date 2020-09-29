def skew(genome):
    n = len(genome)
    skew = [0]*n
    for i in range(1, n):
        skew[i] = skew[i-1]
        if genome[i-1] == 'G':
            skew[i] = skew[i-1] + 1
        elif genome[i-1] == 'C':
            skew[i] = skew[i-1] - 1
    return skew

genome = input('Enter Genome: ')
print(skew(genome))

'''
Enter Genome: CATTCCAGTACTTCATGATGGCGTGAAGA
[0, -1, -1, -1, -1, -2, -3, -3, -2, -2, -2, -3, -3, -3, -4, -4, -4, -3, -3, -3, -2, -1, -2, -1, -1, 0, 0, 0, 1]
'''
