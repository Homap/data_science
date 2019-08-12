def revcomp(dna, reverse=True, complement=True):
    """ Takes a sequence of DNA and converts it to its
    reverse compliment, if only compliment is intended
    set reverse to False """
    bases = 'ATGCatgcWSRYMKwsrymkHBVDhbvdNnTACGTACGWSYRKMWSYRKMDVBHDVBHNN'
    complement_dict = {} # build a dictionary that contains each base with its complement.
    for i in range(30):
        complement_dict[bases[i]] = bases[i+30]
    if reverse: # if reverse is True, default is true
        dna = reversed(dna)
        result_as_list = None # define an empty list
    if complement: # if complement is true, default is true
        result_as_list = [complement_dict[base] for base in dna]
    else:
        result_as_list = [base for base in dna]
    return ''.join(result_as_list)