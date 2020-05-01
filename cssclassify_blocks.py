from pathlib import Path
import re

mks = sorted(Path().joinpath('docs').glob('*.md'))

print('--------- Backing up files --------------')
backup = Path() / 'backup'
backup.mkdir(exist_ok=True)
for p in mks:
    dest = backup / p.name
    print(f'- copying {p} to {dest}')
    content = p.read_text(encoding='utf8')
    with dest.open('w' , encoding='utf8') as f:
        f.write(content)

p3block = re.compile(r'(<div class="python_box">\s*)?(``` python3)([^`]*)(```)(\s*</div>)?', flags=re.DOTALL)

def rep_string(matchobj):
    parts = ['<div class="python_box">\n']
    parts.extend([matchobj.group(i) for i in range(2,5)])
    parts.append('\n</div>')
    return ''.join(parts)


print('---------- Processing files ------------')
for p in mks:
    print(f'- processing {p}')
    content = p.read_text(encoding='utf8')

    npy = content.count('``` python\n') + content.count('```python\n')
    content = content.replace('``` python\n', '``` python3\n')
    content = content.replace('```python\n', '``` python3\n')
    print(f'{npy} ocorrences of ``` python replaced by python3')
    
    print(f'Adding <div class="python_box">:')
    content, n = re.subn(p3block, rep_string, content)
    print(f'{n} substitutions were made')
    
    with p.open('w' , encoding='utf8') as f:
        f.write(content)