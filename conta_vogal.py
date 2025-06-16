vowels = 'aeiou'

letter = {
  'a' : 0,
  'e' : 0,
  'i' : 0,
  'o' : 0,
  'u' : 0
}

text = input('Enter the text: ')

for char in text:
  if char in vowels:
    letter[char] += 1

print(letter)