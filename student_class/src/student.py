class Student:

    # constructor method - if you needs to pass data to the class.
    # self needs to be the first parameter in ALL methods in a class!
    # self needs to be the first parameter in ALL methods in a class!
    # self needs to be the first parameter in ALL methods in a class!
    def __init__(self, name, cohort):
        #instance variables - all needs to be prefixed by "self."
        self.name = name
        self.cohort = cohort


    # methods: functions in classes
    def talk(self):
        return "I can talk!"

    
    def say_favourite_language(self, language):
        return f"I love {language}"
