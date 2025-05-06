def find_words(letters, word_list):
    for word in word_list:
        found = True
        for char in word:
            if letters.count(char) < word.count(char):
                found = False
                break
        if found:
            print(word)

text = "aappbloegfdshfujsasiffjfak"
list1 = ['apple', 'orange']

find_words(text, list1)