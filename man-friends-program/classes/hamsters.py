from aux_modules.hamstersbreedcheck import HamstersBreedCheck
from classes.pets import Pet


class Hamster(Pet):
    def __init__(self, name: str, birthday: str, breed: str, learned_commands: str):
        super().__init__(name, birthday, learned_commands)
        HamstersBreedCheck().is_hamster_breed(breed)
        self.__breed = breed
        self.class_name = "хомяк"
        self.learned_commands = learned_commands

    @property
    def breed(self):
        return self.__breed