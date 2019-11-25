import random

def main():
    result = 0
    turn = 0

    hello_user()
    number = generate_number()

    while result < 4:
        num_tip = user_tip()
        result = value_tip(number, num_tip)
        turn += 1
    print("Correct, you've guessed the right number in %s guesses!" % (turn))


# P1 pozdrav hráče
def hello_user():
    return print("Hi there!\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")


# P2 Generování náhodného čísla, čtyřmístné číslo, nesmí být stejná čísla
def generate_number():
    i = 0
    number = []

    while i < 4:
        ran_num = random.choice(range(10))
        if ran_num not in number:
            number.append(ran_num)

            i += 1

    return number


# P3 Zadání čísla
def user_tip():
    swith = True

    while swith:
        num_tip = input('Zadejte čtyřmístné číslo: ')
        if num_tip.isdigit() == False:
            print('Nezadali jste číselný vstup!')

        elif len(num_tip) != 4:
            print("Nezadali jste čtyřmístné číslo !")

        else:
            return num_tip


# P4 Vyhodnocení zadání
def value_tip(number, num_tip):
    shoda_cisla = 0
    shoda_pozice_cisla = 0

    for index_tip, value_tip in enumerate(num_tip):
        for index_gen, value_gen in enumerate(number):
            if index_tip == index_gen and int(value_tip) == value_gen:
                shoda_pozice_cisla += 1
                shoda_cisla += 1

            elif int(value_tip) == value_gen:
                shoda_cisla += 1

    text_result(shoda_cisla, shoda_pozice_cisla)

    return shoda_pozice_cisla


# P5 Vypíše výsledek
def text_result(shoda_cisla, shoda_pozice_cisla):
    bull = 'bull'
    cow = 'cows'

    if shoda_pozice_cisla > 1:
        bull = "bulls"

    elif shoda_cisla > 1:
        cow = "cows"


    print("%s %s, %s %s" % (shoda_pozice_cisla, bull, shoda_cisla, cow))


main()
