def single_root_words(root_word, *other_words):
    same_words = []
    a = root_word.lower()
    b = [s.lower() for s in other_words]
    for i in b:
        if a in b:
            #or b.count(a):
        #or other_words.count(root_word):
            same_words.append(b)
        if b.count(a):
            same_words.append(a)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

