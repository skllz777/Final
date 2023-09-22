from classes.parentclass import ParentClass


class PackAnimal(ParentClass):
    input_fields = ParentClass.input_fields + ["Порода", "Выученные команды"]

    def __init__(self, name: str, birthday: str, learned_commands: str):
        super().__init__(name, birthday)
        self.__learned_commands = learned_commands