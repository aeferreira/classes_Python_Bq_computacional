def readFASTA(filename):
    """This function reads a FASTA format file and
    returns a pair of strings with the header and the sequence
    """
    with open(filename) as a:
        lines = a.read().splitlines()
    
    # remove empty lines
    lines = [line for line in lines if len(line) > 0]

    # split header and sequence
    # the header might be absent
    if lines[0].startswith('>'):
        return lines[0], ''.join(lines[1:])
    else:
        return '', ''.join(lines)

h, s = readFASTA("gre3.txt")

print(f'Header:\n{h}')
print(f'Sequence:\n{s}')