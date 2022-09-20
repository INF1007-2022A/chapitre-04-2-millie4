#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	liste_prenoms = name.split("-")
	premier_prenom_min = liste_prenoms[0].lower()
	premier_prenom = premier_prenom_min.capitalize()
	return f"Bonjour {premier_prenom}"

def get_random_sentence(animals, adjectives, fruits):
	#random.randrange(start, stop[, step])
	nbr_animaux = len(animals)
	animal = animals[random.randrange(nbr_animaux)]

	nbr_adj = len(adjectives)
	adjectif = adjectives[random.randrange(nbr_adj)]

	nbr_fruits = len(fruits)
	fruit = fruits[random.randrange(nbr_fruits)]

	return f"Aujourd’hui, j’ai vu un {animal} s’emparer d’un panier {adjectif} plein de {fruit}."

def encrypt(text, shift):
	result = ""
	for c in text:
		if c.isalpha() :
			c = c.upper() #mettre les lettres en maj
			encrypted_index = ord(c)+shift #décaler l'index
			#au cas ou l'index dépasse les codes ascii pour A à Z
			if encrypted_index > ord("Z") : encrypted_index -= 26
			elif encrypted_index < ord("A"): encrypted_index += 26
			result += chr(encrypted_index)
		else: result += c
	return result

def decrypt(encrypted_text, shift):
	return encrypt(encrypted_text, - shift)


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon", "chat", "pingouin", "ours polaire", "raton laveur", "castor")
	adjectives = ("rouge", "officiel", "lourd", "gigantesque", "artisanal", "douteux")
	fruits = ("pommes", "kiwis", "mangues", "raisins")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
