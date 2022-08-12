import random


def main():
    forca = importa()
    mostra = []
    for i in range(len(forca)):
        mostra.append("#")
    c = 5
    resta = len(forca)
    vida = False
    usadas = []
    while True:
        for i in mostra:
            print(i, end="")
        print(" ")
        while True:
            tentativa = input(f"Letras usadas {usadas}\nDigite uma letra: ")
            tentativa = tiracaracterespecial(tentativa)
            if (
                usadas.count(tentativa.lower()) == 0
                and len(tentativa) == 1
                and tentativa.isalpha() == True
            ):
                tentativa = tentativa.lower()
                break
            else:
                print("Entrada inválida")
        usadas.append(tentativa)
        for i in range(len(forca)):
            if tentativa == forca[i]:
                print(f"a palavra tem '{tentativa}' na posição {i} ")
                mostra[i] = tentativa
                resta -= 1
                vida = True
        print(f"Falta acertar {resta} letra(s).")
        if vida != True:
            c -= 1
            vida = False
            print(f"Perdeu uma vida restam {c}")
        else:
            vida = False
        if c == 0:
            perdeu(forca)
            break
        elif resta == 0:
            ganhou()
            break


def importa():
    palavras = []
    with open("palavras.txt") as file:
        for line in file:
            palavras.append(line.rstrip())
    random.shuffle(palavras)
    a = palavras[0].lower()
    return a


def perdeu(a):
    print(f"Palavra : {a}")
    print("Que pena vôce perdeu!")




def ganhou():
    print("Parabéns! Você acertou!")


def tiracaracterespecial(a):
    especial = {
        "ç": "c",
        "ã": "a",
        "á": "a",
        "à": "a",
        "â": "a",
        "è": "e",
        "é": "e",
        "ê": "e",
        "í": "i",
        "ì": "i",
        "î": "i",
        "õ": "o",
        "ô": "o",
        "ó": "o",
        "ò": "o",
        "ú": "u",
        "ù": "u",
        "û": "u",
        "ñ": "n",
    }
    if a in especial:
        a = especial[a]
    return a


main()
