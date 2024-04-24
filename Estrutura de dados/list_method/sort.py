linguagens = ['python', 'php', 'js', 'java', 'c']
ling = linguagens.sort()
print(ling)

linguagens = ['python', 'php', 'js', 'java', 'c']
ling1 = linguagens.sort(reverse=True)
print(ling1)

linguagens = ['python', 'php', 'js', 'java', 'c']
ling2 =linguagens.sort(key=lambda x: len(x))
print(ling2)

linguagens = ['python', 'php', 'js', 'java', 'c']
ling3 = linguagens.sort(key=lambda x: len(x), reverse=True)
print(ling3)