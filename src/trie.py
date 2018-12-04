import pickle

class Trie():
	# Construtor
	def __init__(self, char='RAIZ', value=-1, level=0):
		self.id = id
		self.char = char
		self.value = value
		self.children = {}
		self.level = level

	def __str__(self):
		s = "_"*self.level + self.char + " >>> " + str(self.value)
		for char in sorted(self.children):
			s += "\n" + str(self.children[char])
		return s


def insereTrie(raiz, pokemon, n_pok):
	node = raiz
	lastId = None
	
	# Procura um pedaço ja existente
	for id, char in enumerate(pokemon):
		if char in node.children:
			node = node.children[char]
		else:
			lastId = id
			break

	# Nao encontrou o nodo necessario, entao preenche o resto da palavra
	if lastId != None:
		for id, char in enumerate(pokemon[lastId:-1]):
			node.children[char] = Trie(char, -1, lastId+id)
			node = node.children[char]

		node.children[pokemon[-1]] = Trie(pokemon[-1], n_pok, len(pokemon)-1)
	else:
		node.value = n_pok

		
def buscaTrie(raiz, pokemon):
	node = raiz
	achou = True
	
	for id, char in enumerate(pokemon):
		if char in node.children:
			node = node.children[char]
		else:
			achou = False
			break

	if achou and node.value != -1:
		return node.value
	else:
		print("Elemento inexistente")
		return -1


def excluiTrie(raiz, pokemon, i=0):
	node = raiz
	achou = True

	for id, char in enumerate(pokemon):
		if char in node.children:
			node = node.children[char]
		else:
			achou = False
			break

	if achou and node.value != -1:
		node.value = -1
	else:
		print("Elemento inexistente")

		

def runTrie(list_objs_pokemon, flag):
	
	if flag:
		raiz = Trie()

		for i in range(len(list_objs_pokemon)):		# Cria uma Trie
			insereTrie(raiz, list_objs_pokemon[i].name.strip(), list_objs_pokemon[i].id)

		with open('data/trie.bin', 'wb') as file:
			pickle.dump(raiz, file)
		file.close()
	else:
		with open('data/trie.bin', 'rb') as file:
			raiz = pickle.load(file)
		file.close()


	return raiz
