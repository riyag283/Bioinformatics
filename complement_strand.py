def complement_strand(sequence):
    strand = ''
    for each in sequence:
        if each == 'A':
            strand += 'T'
        elif each == 'T':
            strand += 'A'
        elif each == 'C':
            strand += 'G'
        elif each == 'G':
            strand += 'C'
    return strand[::-1]

strand1 = input('Enter strand to get its reverse complement: ')
print(complement_strand(strand1))
