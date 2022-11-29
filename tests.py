import re

s = 'bida17'
c = re.search(r'\d+\.?\d*', s).group()
print(c)



