import random

# Tvým úkolem bude vytvořit program, který by simuloval hru Bulls and Cows. Hra funguje následovně:

# Počítač vygeneruje tajné 4místné číslo. Každá číslice tohoto čísla musí být jiná.
# Počítač vždy vyzve uživatele, aby hádal toto číslo.
# Počítač vyhodnotí tip uživatele a vrátí počty shod.
# Pokud uživatel uhádne správné číslo i správnou pozici, jedná se o "bulls". Pokud je pozice jiná, ale číslice je správná, jedná se o "cows".



def main():
    result = 0
    pocet_tipu = 0

    hello_user()
    num_gen = generate_number()

    while result < 4:
        num_tip = user_tip()
        result = value_tip(num_gen, num_tip)
        pocet_tipu += 1
    print("Correct, you've guessed the right number in %s guesses!" % (pocet_tipu))



# P1 pozdrav hráče
def hello_user():
    return print("Hi there!\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")


# P2 Generování náhodného čísla, čtyřmístné číslo, nesmí být stejná čísla
def generate_number():
    """
    Fce. vygeneruje nahodne ctyrmistne cislo, kazde cislo musi byt unikatni
    """
    i = 0
    num = [0,1,2,3,4,5,6,7,8,9]
    num_gen = ""
    while i < 4:
        ran_num = random.choice(num)
        if i == 0 and ran_num == 0:
            continue
        else:
            num_gen += str(ran_num)
            num.pop(num.index(ran_num))
            i += 1

    return num_gen


# P3 Zadání čísla
def user_tip():
    """
    Fce. vezme jako vstup uzivatele string
    """
    num_tip = input("Enter a number: ")
    while num_tip.isdigit() == False:
        num_tip = input("Enter a number: ")
    return num_tip



# P4 Vyhodnocení zadání
def value_tip(num_gen, num_tip):
    """
    Input:
        * string - num_gen
        * string - num_tip
    Output:
        *
    """

    shoda_cisla = 0
    shoda_pozice_cisla = 0
    list = ["_", "_", "_", "_"]

    for index_tip, value_tip in enumerate(num_tip):
        for index_gen, value_gen in enumerate(num_gen):
            if index_tip == index_gen and value_tip == value_gen:
                shoda_pozice_cisla += 1
                shoda_cisla += 1
                list[index_gen] = int(value_gen)

            elif value_tip == value_gen:
                shoda_cisla += 1
    print(list)
    text_result(shoda_cisla, shoda_pozice_cisla)

    return shoda_pozice_cisla


# P5 Vypíše výsledek
def text_result(shoda_cisla, shoda_pozice_cisla):
    if shoda_pozice_cisla > 1:
        bull = "bulls"
    else:
        bull = "bull"

    if shoda_cisla > 1:
        cow = "cows"
    else:
        cow = "cow"

    print("%s %s, %s %s" % (shoda_pozice_cisla, bull, shoda_cisla, cow))



main()