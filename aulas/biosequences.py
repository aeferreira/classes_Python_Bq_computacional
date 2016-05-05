def readFASTA(filename):
    """This function reads a FASTA format file and
    returns a pair of strings
    with the header and the sequence
    """
    with open(filename) as a:
        lines = [line.strip() for line in a]
    lines = [line for line in lines if len(line) > 0]
    
    if lines[0].startswith('>'):
        return lines[0], ''.join(lines[1:])
    else:
        return '', ''.join(lines)

basesDNA = 'ATGC'
basesRNA = 'AUGC'

aa_residues   = "ACDEFGHIKLMNPQRSTVWY"

complement = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}
complementRNA = { 'A':'U', 'U':'A', 'G':'C', 'C':'G'}

gencode = {
     'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S',
     'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y',
     'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L',
     'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P',
     'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
     'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I',
     'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T',
     'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K',
     'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
     'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A',
     'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D',
     'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G',
     'GGG': 'G', 'TAA': 'STOP', 'TAG': 'STOP', 'TGA': 'STOP'}


aa_masses = {'A': 71.0788, 
             'C': 103.1448, 
             'E': 129.1155, 
             'D': 115.0886, 
             'G': 57.0519, 
             'F': 147.1766, 
             'I': 113.1594, 
             'H': 137.1411, 
             'K': 128.1741, 
             'M': 131.1926, 
             'L': 113.1594, 
             'N': 114.1038, 
             'Q': 128.1307, 
             'P': 97.11667, 
             'S': 87.0782, 
             'R': 156.1875, 
             'T': 101.1051, 
             'W': 186.2132, 
             'V': 99.1326, 
             'Y': 163.176
             }

aa_classes = {
    'small'       : 'PCAGVTDSN',
    'tiny'        : 'AGCS',
    'aliphatic'   : 'ILV',
    'aromatic'    : 'FYWH',
    'positive'    : 'KHR',
    'negative'    : 'DE',
    'charged'     : 'KHRDE',
    'hydrophobic' : 'CAGIVLTMHYWF',
    'polar'       : "CSTNDYWHKQRDE",
    'proline'     : 'P'
}