from pathlib import Path

mks = sorted(Path('.').joinpath('docs').glob('*.md'))

for p in mks:
    print('processing', p)
    content = p.read_text()
    print(content.count('``` python\n'))
    content = content.replace('``` python\n', '``` python3\n')
    with p.open('w') as f:
        f.write(content)