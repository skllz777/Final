class DogsBreedCheck:

    def is_dog_breed(self, dog_breed_name: str):
        if dog_breed_name not in self.__dogs_breeds:
            raise ValueError("Неверная порода собаки")

    __dogs_breeds = """австралийская короткохвостая пастушья собака
австралийская овчарка
австралийская пастушья собака
австралийский келпи
австралийский терьер
австралийский шелковистый терьер
австрийская гончая
австрийский брудастый бракк
австрийский пинчер
азавак
азорская пастушья собака
аиди
акита-ину
алан
алано
алапахский бульдог
алопекис
альпийская таксообразная гончая
аляскинский кли-кай
аляскинский маламут
американская акита
американская эскимосская собака
американский бандог
американский булли
американский бульдог
американский водяной спаниель
американский голый терьер
американский кокер-спаниель
американский мастиф
американский питбультерьер
американский стаффордширский терьер
американский фоксхаунд
анатолийская овчарка
английская енотовая гончая
английская овчарка
английский бульдог
английский водяной спаниель
английский кокер-спаниель
английский мастиф
английский пойнтер
английский сеттер
английский спрингер-спаниель
английский той-терьер
английский фоксхаунд
англо-французская малая гончая
андалузский поденко
аппенцеллер зенненхунд
аргентинский дог
арденнский бувье
артезиано-нормандский бассет
артуазская гончая
арьежская гончая
афганская борзая
африканис
аффенпинчер
баварская горная гончая
бакхмуль
барбет (порода собак)
басенджи
баскская овчарка
бассет-хаунд
бедлингтон-терьер
белая швейцарская овчарка
бельгийская овчарка
бельгийский гриффон
бергамская овчарка
бернская гончая
бернский зенненхунд
бивер-йоркширский терьер
бигль
бишон-фризе
бладхаунд
блю-лейси
бобтейл
бойкин-спаниель
болгарская гончая
болгарская овчарка
болгарский барак
болоньез
большой вандейский бассет-гриффон
большой вандейский гриффон
большой мюнстерлендер
большой швейцарский зенненхунд
бордер-колли
бордер-терьер
бордоский дог
бородатый колли
босерон
бостон-терьер
бразильский терьер
бразильский фила
брак дюпюи
бретонский эпаньоль
бриар (порода собак)
брохольмер
брюссельский гриффон
буковинская овчарка
бульдог кампейро
бульдог катахулы
бульмастиф
бультерьер
бурбонский бракк
бурбуль
бурят-монгольский волкодав
валенсийский ратер
вандейский бассет-гриффон
веймаранер
вельш-корги
вельш-спрингер-спаниель
вельштерьер
венгерская борзая
венгерская выжла
венгерская жесткошёрстная выжла
вертельная собака
вест-хайленд-уайт-терьер
веттерхун
волчья собака сарлоса
вольпино итальяно
восточноевропейская овчарка
восточносибирская лайка
гаванский бишон
гамильтонстёваре
гампр
гладкошёрстный фокстерьер
глен оф имаал терьер
голландская овчарка
голландский смоусхонд
голубой гасконский бассет
голубой гасконский гриффон
голубой пикардийский спаниель
гончая шиллера
грейхаунд
гренландская собака
греческая овчарка
гриффон кортальса
грюнендаль (порода собак)
далматин
датско-шведская фермерская собака
денди-динмонт-терьер
джек-рассел-терьер
дзёмон-сиба
дирхаунд
длинношёрстный колли
доберман
дорги
дратхаар
древер
древесная енотовая гончая
дункер (порода собак)
евразиер
жесткошёрстный фокстерьер
западносибирская лайка
золотистый ретривер
ирландский водяной спаниель
ирландский волкодав
ирландский красно-белый сеттер
ирландский красный сеттер
ирландский мягкошёрстный пшеничный терьер
ирландский терьер
исландская собака
испанская водяная собака
испанская гончая
испанский гальго
испанский мастиф
итальянская гончая
итальянский бракк
итальянский спиноне
йоркширский терьер
ка-де-бо
кавалер-кинг-чарльз-спаниель
кавказская овчарка
каи (порода собак)
кан де паллейро
канадская эскимосская собака
канарский дог
кане-корсо
као де кастро-лаборейро
каракачанская собака
карело-финская лайка
карельская лайка
карельская медвежья собака
карликовый пинчер
каталонская овчарка
кеесхонд
керн-терьер
керри-блю-терьер
кинг-чарльз-спаниель
кинтамани (порода собак)
кисю (порода собак)
китайская хохлатая собака
китайский чунцин
кламбер-спаниель
коикерхондье
комондор
континентальный бульдог
континентальный той-спаниель
корейский чиндо
короткошёрстный колли
котон-де-тулеар
крашская овчарка""".split("\n")