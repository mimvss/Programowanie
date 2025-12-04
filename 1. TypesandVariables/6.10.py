###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title in capital letters', movie.upper())

# print title in small letters
print('Title in small letters', movie.casefold())

# print how many times the vowel "e" appears in the title
print('Vowel e appears', movie.count("e"), 'times')

# print where in the text is the word "Lord"
print('Lord in the text is ', movie.find("Lord"))

# print where in the text is the word "dragon"
print('Dragon in the text is: ', movie.find("Dragon"))
