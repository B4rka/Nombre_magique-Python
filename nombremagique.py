import random


def demander_nombre(nb_min = 0, nb_max = 0):
    nb_asked = 0
    while nb_asked == 0:
        nb_str = input(f"Choisissez un nombre magique (entre {nb_min} et {nb_max}) ")
        try:
            nb_asked = int(nb_str)
        except:
            print("Vous devez choisir un nombre")
        else:
            if nb_asked > nb_max or nb_asked < nb_min:
                print(f"ERREUR, le nombre doit être entre {nb_min} et {nb_max} ")
                nb_asked = 0

    return nb_asked


PLAY_AGAIN = 1
NB_VIES = 5
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(1, 10)

vies = NB_VIES
nombre = 0
while PLAY_AGAIN == 1:
    while nombre != NOMBRE_MAGIQUE and vies > 0:
        print(f'Il vous reste {vies} vies.')
        nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
        if nombre == NOMBRE_MAGIQUE:
            print()
            print('Bravo ! Vous avez gagné !')
            print()
        elif nombre > NOMBRE_MAGIQUE:
            print('Le nombre magique est plus petit')
            print()
            vies -= 1
        elif nombre < NOMBRE_MAGIQUE:
            print('Le nombre magique est plus grand')
            print()
            vies -= 1

    if vies == 0:
        print()
        print(f'Vous avez perdu. Le nombre magique était : {NOMBRE_MAGIQUE}')

    play_str = input("Recommencer la partie ? 1 (Oui) / 0 (Non) ")
    print()

    error = 2
    while error != 0 or 1:
        if int(play_str) == 1:
            vies = NB_VIES
            nombre = 0
            PLAY_AGAIN = int(play_str)
            NOMBRE_MAGIQUE = random.randint(1, 10)
            error = int(play_str)
            break
        elif int(play_str) == 0:
            PLAY_AGAIN = 0
            print()
            print("Merci d'avoir joué !")
            error = int(play_str)
            break
        else:
            print("Veuillez choisir soit 1 (Oui) ou 0 (Non) ")
            print()
            play_str = input("Recommencer la partie ? 1 (Oui) / 0 (Non) ")
            print()
