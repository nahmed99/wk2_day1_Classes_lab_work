class Team:

    # constructor method - if you needs to pass data to the class.
    # self needs to be the first parameter in ALL methods in a class!
    # self needs to be the first parameter in ALL methods in a class!
    # self needs to be the first parameter in ALL methods in a class!
    def __init__(self, name, players, coach):
        #instance variables - all needs to be prefixed by "self."
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0


    # methods: functions in classes

    def add_player(self, new_player):
        self.players.append(new_player)

    
    def has_player(self, new_player):

        # both lines below will work...

        #return self.players.count(player) > 0 
        return new_player in self.players


    def play_game(self, result):
        if result == True:
            self.points =+ 3
