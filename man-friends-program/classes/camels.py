from aux_modules.camelsbreedcheck import CamelsBreedCheck
from classes.pack_animals import PackAnimal


class Camel(PackAnimal):

    def __init__(self, name: str, birthday: str, breed: str, learned_commands: str):
        super().__init__(name, birthday, learned_commands)
        CamelsBreedCheck().is_camel_breed(breed)
        self.__breed = breed
        self.class_name = "верблюд"
        self.learned_commands = learned_commands

    @property
    def breed(self):
        return self.__breed