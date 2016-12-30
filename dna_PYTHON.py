def read_seq(inputfile):
    '''Reads and returns input sequence with special/unwanted characters removed'''
    with open(inputfile,"r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq



def dna_translate(seq): # assume we will pass seq = read_seq(DNA.txt) as parameter of this function
    '''#seq is codon triplet long sequence ACATACA... Triplets:- "ATA", "CAA" etc
    Takes nucleotide long sequence and return protein sequence made from triplets of nucleotides
    Total 20 Amino acids are made from nucleotide codon triplets. Further proteins are composed of these amino acids sequence
    the follwing table has been defined for converting nucleotide triplet codon to amino acid '''

    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    #codon is nucleotide triplet composed of A, G , T, C
    protein =""
    #check if sequence is divisible by 3
    if len(seq) % 3 == 0 :
        # loop over sequences
        for i in range(0,len(seq),3):
             #extract a single codon by checking codon for triplet matching
            codon = seq[i:i+3]
            # look up the codon and store the result
            protein +=table[codon]

    return protein

#test case -1

inputfile = "DNA.txt" #sequence of long DNA nucleotides in th form of triplets saved in DNA.txt file

dna_file =read_seq(inputfile) #removing special/unwanted characters from DNA.txt file

#following slicing of dna_file[20:938] is done because dna nucleotide sequence starts from 21 and ends at 938 as mentioned in NCBI website

dna_to_protein =(dna_translate(dna_file[20:935]))#transforming given DNA nucleotides sequence to the amino acid sequence (proteins) using table(table.txt)
                                #  defined in the function dna_translate,
print(dna_to_protein)

print("\n")
print("compare two sequences,,almost same..\n")
inputfile = "protein.txt"       # this protein file is solution of the above transformed dna sequence (DNA.txt) to amino acid(i.e.protein) sequence using dna_translate()
protein_file =read_seq(inputfile)
print(protein_file)

print(protein_file==dna_to_protein) # return True as translated dna nucleotide sequence DNA.txt matches exactly with protein_file(solutuon file)
print(protein_file==dna_translate(dna_file[20:938])[:-1])
