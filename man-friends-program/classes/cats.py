from aux_modules.catsbreedcheck import CatsBreedCheck
from classes.pets import Pet


class Cat(Pet):
    def __init__(self, name: str, birthday: str, breed: str, learned_commands: str):
        super().__init__(name, birthday, learned_commands)
        CatsBreedCheck().is_cat_breed(breed)
        self.__breed = breed
        self.class_name = "кошка"
        self.learned_commands = learned_commands

    @property
    def breed(self):
        return self.__breed