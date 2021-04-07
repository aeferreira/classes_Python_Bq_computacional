from pathlib import Path
import re

import nbformat as nbf

fname = 'more_on_lists_dicts'
mks = sorted(Path().joinpath('docs').glob('*.md'))

fname = Path().joinpath('docs',f'{fname}.md')
print(f'--------- Reading {fname} --------------')
content = fname.read_text(encoding='utf8')

code_cells = []

p3block = re.compile(r'(<div class="python_box">\s*)?(``` python3)([^`]*)(```)(\s*</div>)?', flags=re.DOTALL)

def rep_cell(m):
    codeloc = m.index('``` python3') + 1
    code = m[codeloc]
    code = code.splitlines()
    if code[0] == '':
        code = code[1:]
    return '\n'.join(code)


print('---------- Processing file ------------')

matches = re.findall(p3block, content)
code_cells = [rep_cell(m) for m in matches]

for c in code_cells[:5]:
    print('-'*30)
    print(c)
    print('-'*30)

nb = nbf.v4.new_notebook()

nb['cells'] = [nbf.v4.new_code_cell(c) for c in code_cells]

nbf.write(nb, 'test.ipynb')
    
