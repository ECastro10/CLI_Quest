from Character import Character
from Move import move_list
import random as r


def gen_stats(person):
    '''
    INPUT: takes person objects stat attributes which equal 0
    USAGE: to randomly generate stats within limits
    OUTPUT: none
    '''

    person.maxhp = r.randint(14, 18)
    person.hp = person.maxhp
    person.atk = r.randint(9, 11)
    person.dfn = r.randint(9, 12)
    person.spd = r.randint(5, 10)
    person.lck = r.randint(1, 5)
    stat_total = stat_sum(person)
    if stat_total != 45:
        gen_stats(person)


def stat_sum(person):
    '''
    INPUT: takes the person object and adds up all the stat attributes
    USAGE: to find the stat sum in order to balance out the stat distribution
    OUTPUT: none, just returns stat_total
    '''

    stat_total = (person.maxhp + person.atk + person.dfn + person.spd + person.lck)
    return stat_total


def print_stats(person):
    '''
    INPUT: person objects and its attributes
    USAGE: to print out the objects name and attributes
    OUTPUT: prints out name and stats
    '''

    print('\nName: {}\n\
Level: {}\n\
Health: {}\n\
Attack: {}\n\
Defense: {}\n\
Speed: {}\n\
Luck: {}\n'.format(person.name, person.level, person.maxhp, person.atk, person.dfn, person.spd, person.lck))


def print_name_and_hp(person):
    """
    INPUT: person objects and attributes
    USAGE: to print out the object name, HP, and a health bar
    OUTPUT: just the print statements, no return
    """

    print(person.name, person.hp_bar, "{}/{}".format(person.hp, person.maxhp) )


def attack(attacker, attackee):
    '''
    INPUT: takes in two objects as arguments
    USAGE: to basically take hp away from another player
    OUTPUT: none
    '''

    move_no = 0

    for i in attacker.moves:
        print('{} {}\n'.format(move_no, i))
        move_no += 1

    move_choice = int(input('Which move would you like to use?> '))

    use_move(attacker, attackee, attacker.moves[move_choice])


def use_move(attacker, attackee, move):
    '''
    INPUT: takes in two objects and a move object
    USAGE: this function uses the move object and it affects the objects meant to be affected by the move object
    OUTPUT: the after effects of the move utilized and a miss statement if the move objects fails (on purpose)
    '''

    if move.power == '--':
        print('not an attacking move')

    else:

        chances = 100 - (move.accuracy * 100)

        if r.randint(1, 100) < chances:
            print('{} Missed!'.format(move))

        else:
            modifier = 1
            damage = (((2 * attacker.level + 10) / 250) * (attacker.atk / attackee.dfn) * move.power + 2) * modifier
            damage = int(round(damage, 0))
            attackee.hp -= damage
            update_hp_bar(attackee)
            if attackee.hp < 0:
                attackee.hp = 0
                update_hp_bar(attackee)
            print('{} Hit!'.format(move))
            print(move, "did {} damage to".format(damage), attackee)


def print_move_stats(move):
    '''
    INPUT: move object
    USAGE: to print the move object dict in a nutshell except formatted for user friendly display
    OUTPUT: move objects attributes in a user friendly manner
    '''

    print('{}\nPower: {}\nAccuracy: {}\nCritical Rate: {}'.format(move.name,
                                                                  move.power, (str(round(move.accuracy * 100))) +
                                                                  '%', str(round(move.critrate * 100)) + '%'))


def update_hp_bar(person):
    """
    INPUT: self
    USAGE: to update hp_bar
    OUTPUT: none
    """

    current_ticks = round(person.hp/person.maxhp * 20)
    tick_string = (current_ticks * ">") + ((20 - current_ticks) * " ")
    person.hp_bar = [tick_string]


def who_goes_first(player1, player2):
    """
    INPUT: two Character objects
    USAGE: to determine who goes first based on speed
    OUTPUT: the name of the character that goes first
    """
    # This block determines who goes first based on speed attribute
    if player1.spd > player2.spd:
        return player1.name
    elif player1.spd == player2.spd:
        random_selector = r.choice([player1.name, player2.name])
        return random_selector
    else:
        return player2.name


def simple_opponent_turn(comp, player):
    """
    INPUT: two character objects
    USAGE: simple, attack-slash, opponent type
    OUTPUT: returns True
    """

    print("\n" + comp.name + "'s turn")
    use_move(comp, player, comp.moves[1])
    print("\n")
    return True


def player_turn(player, opponent):
    """
    INPUT: two character objects
    USAGE: the menuing for the user
    OUTPUT: returns True
    """

    print('Your Turn\n(a)ttack, (d)efend, (i)tem, (r)un')
    choice_input = input(' > ')

    if choice_input == 'a':
        attack(player, opponent)

    elif choice_input == 'd':
        print('Defend feature soon')

    elif choice_input == 'i':
        print('item feature soon')

    elif choice_input == 'r':
        print('No running away yet')

    return True

def battle_sequence(ally, foe):
    '''
    INPUT: two player objects (an ally and a foe)
    USAGE: to navigate through a battle sequence between the two player objects
    OUTPUT: whatever is necessary within the sequence
    '''

    print('\nEntering Battle Mode')

    while foe.hp != 0 or ally.hp != 0:

        ally_played = False
        foe_played = False

        if who_goes_first(ally, foe) == ally.name:
            played = player_turn(ally, foe)
            print_name_and_hp(ally)
            print_name_and_hp(foe)
        else:
            simple_opponent_turn(foe, ally)
            print_name_and_hp(ally)
            print_name_and_hp(foe)



    if ally.hp > 0:
        print('{} has been knocked out'.format(foe.name))
    else:
        print("You have been knocked out MF!")


def encounter_menu():
    pass


def user_input():
    '''
    INPUT: Any input information needed
    USAGE: To take in user input during any point in time
    OUTPUT: returns what the user has input
    '''

    u_input = input('>> ')
    return u_input


def main():
    '''
    INPUT: none
    USAGE: runs the game
    OUTPUT: whatever the game dictates
    '''
    # First, get user name to generate the user's character, then print stats
    print('What is your name?')
    player1 = Character(user_input())
    gen_stats(player1)
    player1.moves = move_list
    print('Here are your stats:')
    print_stats(player1)

    # Generate first opponenet and stats
    foe1 = Character('Felix')
    gen_stats(foe1)
    foe1.moves = move_list
    print("Here are your opponent's stats")
    print_stats(foe1)

    battle_sequence(player1, foe1)
    print("Thank you for playing!")

main()
