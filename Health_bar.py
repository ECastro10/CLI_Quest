class Health_bar:

    def __init__(self, person):
        self.hp_bar = ["////////////////////"]


    def update_hp_bar(self, person):
        """
        INPUT: a person object
        USAGE: to update said person's hp_bar
        OUTPUT: none
        """

        tick_value = (person.maxhp // 20)
        current_ticks = (person.hp // tick_value)
        tick_string = (current_ticks * "|") + ((20 - current_ticks) * " ")
        self.hp_bar = [tick_string]
