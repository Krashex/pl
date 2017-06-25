#
reverse_word = ""
word = input('Your word ')
index = len(word) - 1
while index > -1:
    reverse_word += word[index]
    index -= 1
print(reverse_word)
input("Press enter")
