class DonkeysBreedCheck:

    def is_donkey_breed(self, donkey_breed_name: str):
        if donkey_breed_name not in self.__donkey_breeds:
            raise ValueError("Неверная порода осла")

    __donkey_breeds = """пиренейская
котентен
пуату
провансальская
испанские
каталонский осёл
среднеазиатские
бухарская
мервская
марыйская""".split("\n")