seq = 'ADKHLILTAVGGCWFHVAFWEVEKAGAHKWE'

for i, aminoacido in enumerate(seq):
    if aminoacido in 'KL':
        print(i, ':', aminoacido)