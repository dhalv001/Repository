#This program takes in a sequence of DNA that contains introns and exons. It
#returns a sequence of ONLY the coding regions of the DNA and it returns the percentage
#of coding DNA.
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
#The instructions state that exon 1 starts at CHARACTER 1 and ends at CHARACTER 63
#Slicing starts at 0, so I need to subtract the character positions by 1 to use with slicing.
exon1 = my_dna[0:63]
#The instructions state that exon 2 starts at CHARAcTER 91 and goes to the end of the sequence.
#The same -1 slicing rules apply AND recall that, to go to end of sequence, leave the end slice blank. 
exon2 = my_dna[90: ]
coding_regions = exon1 + exon2
my_dna_length = len(my_dna)
coding_length = len(coding_regions)
percent_coding = 100 * coding_length / my_dna_length
#This rounds the percentage of coding DNA to 2 decimal places.
percent_coding = round(percent_coding, 2)
print("The provided DNA sequence is: ")
print(my_dna)
print("Exon 1 is: ")
print(exon1)
print("Exon 2 is: ")
print(exon2)
print("The coding regions of the DNA sequence are: ")
print(coding_regions)
print("The percentage of coding DNA is: " + str(percent_coding) + "%.")
