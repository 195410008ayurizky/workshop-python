import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
#output: 
['foot', 'fell', 'fastest']
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
#output: 
'cat in the hat'