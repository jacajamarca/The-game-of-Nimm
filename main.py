turno = 1
stones = 20
def main():
    global stones
    print(f"There are {stones} stones left.")
    while stones >= 1:
        turno_jugador()
        stones = stones - user_input
        validar_stones()
        define_ganador()
    print("")
    print(ganador)   
       
def define_ganador():
    global ganador

    if turno % 2 == 0:
        ganador = str("Player 2 wins!")
    else:
        ganador = str("Player 1 wins!")

def validar_stones():
    global stones
    if stones >=1:
        print(f"There are {stones} stones left.")
    else:
        pass
        #print("Game over")


def turno_jugador():
    global turno, user_input   
    if turno % 2 != 0:
        user_input = int(input("Player 1 would you like to remove 1 or 2 stones? "))
        validar_input()
        print("")
    else:
        user_input = int(input("Player 2 would you like to remove 1 or 2 stones? "))
        validar_input()
        print("")
    turno += 1   

def validar_input():
    global user_input
    if (user_input == 1 or user_input ==2):
        pass
    else:
        while user_input != 1 and user_input != 2:
            user_input = int(input("Please enter 1 or 2: "))
        pass

if __name__ == '__main__':
    main()