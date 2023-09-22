class CamelsBreedCheck:

    def is_camel_breed(self, camel_breed_name: str):
        if camel_breed_name not in self.__camels_breeds:
            raise ValueError("Неверная порода верблюда")

    __camels_breeds = """одногорбый верблюд
дромедар
дромадер
арабиан
двугорбый верблюд
бактриан
дикий верблюд""".split("\n")