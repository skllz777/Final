from aux_modules.donkeysbreedcheck import DonkeysBreedCheck
from classes.pack_animals import PackAnimal


class Donkey(PackAnimal):
    def __init__(self, name: str, birthday: str, breed: str, learned_commands: str):
        super().__init__(name, birthday, learned_commands)
        DonkeysBreedCheck().is_donkey_breed(breed)
        self.__breed = breed
        self.class_name = "осёл"
        self.learned_commands = learned_commands

    @property
    def breed(self):
        return self.__breed