import shutil

a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)




message = 'this if is you not are a reading very this good then way you to have hide done a it message wrong'
words = message.split()
for x in range(0, len(words), 2):
    print(words[x])



f = open('test.txt')
s = f.read()
f.close()
f = open('output.txt', 'w')
f.write(s)
f.close
shutil.copy('test.txt', 'output.txt')
