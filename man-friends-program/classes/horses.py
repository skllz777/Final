from aux_modules.horsesbreedcheck import HorsesBreedCheck
from classes.pack_animals import PackAnimal


class Horse(PackAnimal):
    def __init__(self, name: str, birthday: str, breed: str, learned_commands: str):
        super().__init__(name, birthday, learned_commands)
        HorsesBreedCheck().is_horse_breed(breed)
        self.__breed = breed
        self.class_name = "лошадь"
        self.learned_commands = learned_commands

    @property
    def breed(self):
        return self.__breed