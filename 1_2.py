abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
monograms = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'

text = ''
with open('text.txt', 'r', encoding="utf-8") as f:
    text = f.read()
    text = "".join(c for c in text if c == ' ' or c == 'n' or c.isalpha()).lower()
    print(text)
    offset = int(input('Offset: '))
    message = ''
    c = 0

for sym in text:
    if sym.isalpha():
        message += abc[(abc.find(sym) + offset) % 33]
    else:
        message += sym
print("Encrypted original text: ", message)

frequencies = {}
for k in abc:
    frequencies[k] = 0

for sym in message:
    if sym != ' ':
        frequencies[sym] += 1

crypt_monograms = ''
for offset, value in frequencies.items():
    i = 0
    while i < len(crypt_monograms) and value <= frequencies[crypt_monograms[i]]:
        i += 1
    crypt_monograms = crypt_monograms[:i] + offset + crypt_monograms[i:]
    
decrypt_message1 = ''
for sym in message:
    if sym == ' ':
        decrypt_message1 += sym
    else:
        decrypt_message1 += monograms[crypt_monograms.find(sym)]
print("Monograms decrypt: ", decrypt_message1)

bigrams = {}
for i in range(len(text)-1):
    if text[i] == ' ' or text[i+1] == ' ':
        continue
    if text[i:i+2] not in bigrams.keys():
        bigrams[text[i:i+2]] = 1
    else:
        bigrams[text[i:i+2]] += 1

crypt_bigrams = {}
for i in range(len(message)-1):
    if message[i] == ' ' or message[i+1] == ' ':
        continue
    if message[i:i+2] not in crypt_bigrams.keys():
        crypt_bigrams[message[i:i+2]] = 1
    else:
        crypt_bigrams[message[i:i+2]] += 1

bigrams10 = []
for i in range(10):
    maxx = 0
    bigram = ''
    for offset, value in bigrams.items():
        if value > maxx:
            bigram = offset
            maxx = value
    bigrams10.append(bigram)
    bigrams.pop(bigram)

crypt_bigrams10 = []
for i in range(10):
    maxx = 0
    bigram = ''
    for offset, value in crypt_bigrams.items():
        if value > maxx:
            bigram = offset
            maxx = value
    crypt_bigrams10.append(bigram)
    crypt_bigrams.pop(bigram)
    
def move_two_letters(s, a, b):
    if a > b:
        r = a
        a = b
        b = r
    s1 = s[:a]
    s2 = s[a+1:b]
    s3 = s[b+1:]
    return s1 + s[b] + s2 + s[a] + s3

moved_letters = []
for i in range(len(bigrams10)):
    let1 = crypt_monograms.find(crypt_bigrams10[i][0])
    let2 = monograms.find(bigrams10[i][0])
    if let1 != let2 and crypt_bigrams10[i][0] not in moved_letters:
        crypt_monograms = move_two_letters(crypt_monograms, let1, let2)
        moved_letters.append(crypt_monograms[let1])
        moved_letters.append(crypt_monograms[let2])

    let1 = crypt_monograms.find(crypt_bigrams10[i][1])
    let2 = monograms.find(bigrams10[i][1])
    if let1 != let2 and crypt_bigrams10[i][1] not in moved_letters:
        crypt_monograms = move_two_letters(crypt_monograms, let1, let2)
        moved_letters.append(crypt_monograms[let1])
        moved_letters.append(crypt_monograms[let2])

crypt_monograms.find('б'), monograms.find('о')

decrypt_message2 = ''
for sym in message:
    if sym == ' ':
        decrypt_message2 += sym
    else:
        decrypt_message2 += monograms[crypt_monograms.find(sym)]
print("Bigrams decrypt: ", decrypt_message2)