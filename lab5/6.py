import re

file=open("row.txt", "r", encoding="utf8")
text= file.read()

x = re.sub('[,.\s]',':', text)
print(x)
