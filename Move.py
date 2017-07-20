class Move:


    def __init__(self, name, power, accuracy, critrate):

        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.critrate = critrate



    def __str__(self):
        return '%s' % (self.name)

    def __repr__(self):
        return '%s' % (self.name)

# Moves to practice with
move01 = Move('Tackle', 35, .95, .05)
move02 = Move('Slash', 40, .90, .05)
# TODO work on non attack move
move03 = Move('Taunt', '--', .95, '--')

move_list = [move01, move02, move03]