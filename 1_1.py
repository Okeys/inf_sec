def get_abc(offset, key):
    a = ord('а')
    alph = ''.join([chr(i) for i in range(a,a+32)])
    for sym in key:
        alph = alph.replace(sym, '')
    alph = key + alph
    for i in range(offset):
        alph = alph[-1] + alph[:-1]
    return alph

input_message = input("Text: ")
offset = int(input("Offset: "))
key = input("Key: ")

alph = get_abc(offset, key)
message = ''
for sym in input_message:
    if sym.isalpha():
        message += alph[(ord(sym) - 224)%32]
    else:
        message += sym
print(message)
print(alph)