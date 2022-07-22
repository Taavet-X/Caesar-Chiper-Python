chars = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

def encode(text, shift):
    text = text.upper() 
    encodedText = ""
    #for each character in the text
    for char in text: 
        #gets the position of the char in the list        
        charIndex = chars.index(char) 
        #then adds a value that that position
        newIndex = charIndex + shift 
        #applies mod to avoid going out of bounds
        newIndex = newIndex % len(chars) 
        #adds the new char to the result text
        encodedText += chars[newIndex]
    return encodedText

def decode(encodedText, shift):
    encodedText = encodedText.upper() #All letters into cap ones
    decodedText = ""
    #for each character in the text
    for char in encodedText:
        #gets the position of the char in the list
        charIndex = chars.index(char)
        #then adds a value that that position, this time
        #the value is the diference between the amount 
        #of chars in the list in the list and the shift
        newIndex = charIndex + len(chars) - shift
        newIndex = newIndex % len(chars)
        decodedText += chars[newIndex]
    return decodedText

print(encode("Hello World", 7))
print(decode("OLSSVGCVYSK", 7))
  
