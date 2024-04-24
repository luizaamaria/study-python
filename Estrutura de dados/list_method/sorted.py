linguagens = ['python', 'php', 'js', 'java', 'c']

#sorted = função

ling1 = sorted(linguagens, key=lambda x: len(x))
print(ling1)

ling2 = sorted(linguagens, key=lambda x: len(x), reverse=True)
print(ling2)