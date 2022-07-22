chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

word = "Test"
word = word.upper()
shift = 7
newWord = ""
for char in word:
    charIndex = chars.index(char)
    newIndex = charIndex + shift
    newIndex = newIndex % len(chars)
    newWord += chars[newIndex]
print(newWord)
  