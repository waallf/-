n, l = [int(a) for a in input().strip().split()]
chars = [[] for _ in range(l)]
words = []
for _ in range(n):
    tmp_word = input()
    words.append(tmp_word)
    for i, x in enumerate(chars):
        x.append(tmp_word[i])
words = list(set(words))
words.sort()
n = len(words)
for i, _ in enumerate(chars):
    chars[i] = list(set(chars[i]))
    chars[i].sort()
gen_words_index = [0 for i in range(l)]

i = l - 1
all_index = 0
# print(words)
# print(chars)

while all_index < n:
    curr_word = ''.join([chars[i][gen_words_index[i]] for i in range(l)])
    ### print('curr', i, gen_words_index)
    ### print(curr_word, words[all_index])
    if curr_word != words[all_index]:
        print(curr_word)
        exit()
    all_index += 1
    while i >= 0 and gen_words_index[i] >= len(chars[i]) - 1:
        i -= 1
    if i < 0:
        break
    gen_words_index[i] += 1
    i += 1
    while i <= l - 1:
        gen_words_index[i] = 0
        i += 1
    i = l - 1

print('-')
