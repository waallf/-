n, l = [int(a) for a in input().strip().split()]
chars = [[] for _ in range(l)]
words = []
for _ in range(n):
    tmp_word = input()
    words.append(tmp_word)
    for i, x in enumerate(chars):
        x.append(tmp_word[i])
words.sort()
for i, _ in enumerate(chars):
    chars[i].sort()
gen_words_index = [0 for i in range(l)]

'''
for i in reversed(range(l)):
    if gen_words_index[i] < len(chars[i])-1:
        gen_words_index[i] += 1
        continue
    else:
        if i != 0:
            gen_words_index[i] = 0
'''


i = l - 1
all_index = 0
while i >= 0 and all_index < n:
    curr_word = ''.join([chars[i][gen_words_index[i]] for i in range(l)])
    if curr_word != words[all_index]:
        print(curr_word)
        exit()
    all_index += 1
    if gen_words_index[i] < len(chars[i])-1:
        gen_words_index[i] += 1
    else:
        if i != 0:
            gen_words_index[i] = 0
            i -= 1

print('-')
