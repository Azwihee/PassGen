from os import system
import socket

from threading import Thread

from pystyle import Colorate, Center, Write, Anime, Colors, System, Col
banner = r"""
                        xXXXXXXXXXXx
                      xX            Xx
                     X                X
                    X      XxXXxX      X
                   X        x  x       X
                   X         XX         X
          XX       X  /~~\        /~~\  X       XX
        XX  X      X |  o  \    /  o  | X      X  XX
      XX     X     X  \____/    \____/  X     X     XX
 XXXXX     XX      \         /\        ,/      XX     XXXXX
X        XX%;;@      \      /  \     ,/      @%%;XX        X
X       X  @%%;;@     X              X     @%%;;@  X       X
X      X     @%%;;@   X  ;  ;  ;  ;  X   @%%;;@     X      X
 X    X        @%%;;@                  @%%;;@        X    X
  X   X          @%%;;@              @%%;;@          X   X
   X  X            @%%;;@          @%%;;@            X  X
    XX X             @%%;;@      @%%;;@             X XX
      XXX              @%%;;@  @%%;;@              XXX
                         @%%;;%%;;@
                           @%%;;@
                         @%%;;@..@@
                          @@@  @@@
"""[1:]



ascii = """\n\n
  _____               _____            
 |  __ \             / ____|           
 | |__) |_ _ ___ ___| |  __  ___ _ __  
 |  ___/ _` / __/ __| | |_ |/ _ \ '_ \ 
 | |  | (_| \__ \__ \ |__| |  __/ | | |
 |_|   \__,_|___/___/\_____|\___|_| |_|                                                
\n\n"""


def main():
 System.Title("PassGen - by Azwihee")
System.Size(170, 55)
Anime.Fade(Center.Center(banner), Colors.green_to_black, Colorate.Vertical, interval=0.01, enter=True)

def tui():
 System.Clear()
print(Colorate.Horizontal(Colors.green_to_red, Center.XCenter(ascii)))

import string
import random


## characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = int(input("Entrez la longueur du mot de passe: "))

	## number of character types
	alphabets_count = int(input("Entrez le nombre de lettres de l'alphabet dans le mot de passe: "))
	digits_count = int(input("Entrez le nombre de chiffres dans le mot de passe: "))
	special_characters_count = int(input("Entrez le nombre de caractères spéciaux dans le mot de passe: "))

	characters_count = alphabets_count + digits_count + special_characters_count

	## check the total length with characters sum count
	## print not valid if the sum is greater than length
	if characters_count > length:
		print("Le nombre total de caractères est supérieur à la longueur du mot de passe")
		return


	## initializing the password
	password = []
	
	## picking random alphabets
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))


	## picking random digits
	for i in range(digits_count):
		password.append(random.choice(digits))


	## picking random alphabets
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))


	## if the total characters count is less than the password length
	## add random characters to make it equal to the length
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))


	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))



## invoking the function
generate_random_password()
from pystyle import Colors, Colorate
print(Colorate.Horizontal(Colors.yellow_to_red, "Voici ton mot de passe ;)Merci pour ton IP aussi", 1))

from pystyle import Colors, Colorate
print(Colorate.Horizontal(Colors.yellow_to_red, "Nan j'rigole mon bichon", 1))

input('Presse Entreé pour fermer')

if __name__ == '__main__':
    main()