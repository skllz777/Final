from aux_modules.dogsbreedcheck import DogsBreedCheck
from classes.pets import Pet


class Dog(Pet):
    def __init__(self, name: str, birthday: str, breed: str, learned_commands: str):
        super().__init__(name, birthday, learned_commands)
        DogsBreedCheck().is_dog_breed(breed)
        self.__breed = breed
        self.class_name = "собака"
        self.learned_commands = learned_commands

    @property
    def breed(self):
        return self.__breed