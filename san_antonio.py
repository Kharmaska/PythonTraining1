quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]
user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')

# Show random quote
def get_random_quote(my_list):
	item = my_list[0]
	return item

print (get_random_quote(my_list))


if user_answer == "B":
    pass
elif user_answer == "C":
    print("C pas la bonne réponse ! Et G pas d’humour, je C...")
else:
	pass
    # show another quote

def show_random_quote():
	pass