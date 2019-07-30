from pathlib import Path

mks = sorted(Path().joinpath('docs').glob('*.md'))

print('--------- Backing up files --------------')
backup = Path() / 'backup'
backup.mkdir(exist_ok=True)
for p in mks:
    dest = backup / p.name
    print(f'- copying {p} to {dest}')
    content = p.read_text()
    #print(content.count('``` python\n'))
    #content = content.replace('``` python\n', '``` python3\n')
    with dest.open('w') as f:
        f.write(content)

print('---------- Processing files ------------')
for p in mks:
    dest = backup / p.name
    print(f'- processing {p}')
    content = p.read_text()
    print(content.count('``` python\n'))
    content = content.replace('``` python\n', '``` python3\n')
    with dest.open('w') as f:
        f.write(content)