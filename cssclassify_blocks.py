from pathlib import Path
import re

mks = sorted(Path().joinpath('docs').glob('*.md'))

print('--------- Backing up files --------------')
backup = Path() / 'backup'
backup.mkdir(exist_ok=True)
for p in mks:
    dest = backup / p.name
    #print(f'- copying {p} to {dest}')
    content = p.read_text()
#     with dest.open('w') as f:
#        f.write(content)

p3block = re.compile(r'(``` python3)([^`]*)(```)', flags=re.DOTALL)

print('---------- Processing files ------------')
for p in mks:
    if p.name != 'files.md':
        continue
    print(f'- processing {p}')
    content = p.read_text()

    npy = content.count('``` python\n') + content.count('```python\n')
    print(f'{npy} ocorrences of ``` python')
    content = content.replace('``` python\n', '``` python3\n')
    content = content.replace('```python\n', '``` python3\n')
    
    print(f'Ocorrences of ``` python3 in {p}:')
    for m in re.finditer(p3block, content):
        print(m.group(1))
        print('----------------------')

    
    #with p.open('w') as f:
        #f.write(content)