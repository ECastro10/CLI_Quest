class Ally:


    def __init__(self, name):
        self.name = name
        self.moves = []
        self.hp = 0
        self.atk = 0
        self.dfn = 0
        self.spd = 0
        self.lck = 0
        self.level = 1

    def __str__(self):
        return '%s' % (self.name)

    def __repr__(self):
        return '%s' % (self.name)