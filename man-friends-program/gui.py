from kivy.core.window import Window

from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout

from kivymd.uix.textfield import MDTextField

from classes.camels import Camel
from classes.cats import Cat
from classes.dogs import Dog
from classes.donkeys import Donkey
from classes.hamsters import Hamster
from classes.horses import Horse
from classes.parentclass import ParentClass
from aux_modules.counter import Counter
from aux_modules.data import Data
from aux_modules.filemanager import FileManager
from functools import partial
from kivy.clock import Clock
from kivy.config import Config

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', '0')

Window.size = (1280, 720)
Window.title = "Реестр животных"


class AnimalRegistry:
    def __init__(self):
        try:
            self.__file_manager = FileManager("man-friends2.csv")
        except IOError as e:
            raise IOError("Ошибка работы с файлом " + e.filename)

        self._child_classes_ratio = {"верблюд": Camel,
                                     "лошадь": Horse,
                                     "осёл": Donkey,
                                     "кошка": Cat,
                                     "собака": Dog,
                                     "хомяк": Hamster,
                                     }

        self.counter = Counter()

        self._data = Data(list[ParentClass]())
        ParentClass.id_counter_reset()
        self.__file_manager.create_objects_from_clv(self._create_child, self._child_classes_ratio,
                                                    ParentClass)

        self._buttons_names_functions = {'добавить': self._add_new,
                                         'обучить команде': self._teach_command,
                                         'удалить': self._animals_delete_command,
                                         'выход': quit}

    def _add_new(self, *args):
        pass

    def _teach_command(self, event):
        pass

    def _create_child(self, class_name, data: list = None):
        child = class_name(*data)

        with self.counter as cnt:
            cnt.add()

        self._data.append(child)

        self.__file_manager.write_data_to_file(self._data)

    def _teach(self, animals_ids: list, new_command: str):
        error_text = ""
        for i in animals_ids:
            animal = self._data.get_by_param('id', i)
            if new_command in animal.learned_commands:
                error_text += f"{animal.class_name} {animal.name} уже знает команду {new_command}\n"
                continue
            if animal.learned_commands:
                animal.learned_commands += f", {new_command}"
            else:
                animal.learned_commands = f"{new_command}"

        self.__file_manager.write_data_to_file(self._data)
        if error_text:
            raise ValueError(error_text)

    def _animals_delete_command(self, event):
        pass

    def _animals_delete(self, animals_ids):
        print(animals_ids)
        for i in animals_ids:
            animal = self._data.get_by_param('id', i)
            self._data.remove(animal)
        self.__file_manager.write_data_to_file(self._data)


class AnimalMDScreen(MDFloatLayout, AnimalRegistry):
    def __init__(self, *args, **kwargs):
        MDFloatLayout.__init__(self, *args, **kwargs)
        AnimalRegistry.__init__(self)

        self._text_field_values = None
        self._adding_dialog = None
        self._teach_dialog = None
        self._adding_alert = None
        self._delete_dialog = None
        self._teach_alert = None
        self._alert = None

        self._view = MDDataTable(pos_hint={"center_y": 0.5, "center_x": 0.5},
                                 size_hint=(1, 1),
                                 check=True,
                                 background_color_cell="white",
                                 background_color_selected_cell="white",
                                 use_pagination=True, rows_num=10,
                                 column_data=[(i, dp(40)) for i in ParentClass.field_width])
        self._view.row_data = self._get_data()
        self.add_widget(self._view)

        self.__buttons = self.__create_buttons(self._buttons_names_functions)
        self.__box = MDBoxLayout(adaptive_size=True,
                                 pos_hint={"center_y": 0.1},
                                 padding="24dp",
                                 spacing="24dp", )
        for btn in self.__buttons:
            self.__box.add_widget(btn)
        self.add_widget(self.__box)

    @staticmethod
    def __create_buttons(buttons_names_functions: dir, parameters: dir = None):
        buttons = []
        for i in buttons_names_functions:
            btn = MDFlatButton(text=i, font_size="20sp", md_bg_color="#f5f5f5", )
            btn.bind(on_press=partial(buttons_names_functions[i], *parameters) if parameters else partial(
                buttons_names_functions[i]))
            buttons.append(btn)
        return buttons

    def _add_new(self, update):
        text_fields = self.get_text_fields(ParentClass.fields_names_ids)
        text_fields_grid = MDGridLayout(rows=len(text_fields), *text_fields)
        add_button = MDFlatButton(
            text="ДОБАВИТЬ",
            theme_text_color="Custom",
        )
        add_button.bind(on_release=lambda instance: self.__adding(text_fields_grid))
        self._text_field_values = {i: "" for i in ParentClass.fields_names_ids}
        self._adding_dialog = MDDialog(
            title="Новое животное:",
            type="custom",
            content_cls=MDBoxLayout(
                text_fields_grid,
                orientation="vertical",
                spacing="12dp",
                size_hint_y=None,
                height="425dp",
            ),
            buttons=[
                MDFlatButton(
                    text="ЗАКРЫТЬ",
                    theme_text_color="Custom",
                    on_release=lambda instance: self._dialog_close(self._adding_dialog)
                ),
                add_button
            ],
        )
        self._adding_dialog.open()

    @staticmethod
    def get_text_fields(fields: list):
        text_fields = []
        for i in fields:
            if i != "Id":
                text_fields.append(MDTextField(id=fields[i], hint_text=i))
        return text_fields

    @staticmethod
    def _dialog_close(dialog):
        dialog.dismiss(force=True)

    def __get_class_by_name(self, name: str):
        name = name.lower()
        if name in self._child_classes_ratio:
            return self._child_classes_ratio[name]
        raise ValueError("Неверный класс")

    def __adding(self, text_fields_greed):

        data = [getattr(text_fields_greed.ids, i).text for i in
                list(filter(lambda s: s in ParentClass.required_input_fields, text_fields_greed.ids))]

        if not self._adding_alert:
            self._adding_alert = MDDialog(
                title="Error",
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=lambda instance: self._dialog_close(self._adding_alert)
                    ),
                ],
            )
        try:
            self._create_child(self.__get_class_by_name(text_fields_greed.ids.Class.text),
                               data)
        except Exception as e:
            self._adding_alert.title = str(e)
            self._adding_alert.open()
        self._view_update()
        self._dialog_close(self._adding_dialog)

    def _view_update(self):
        self._view.row_data = self._get_data()

    def _get_data(self):
        return [(i.id, i.name, i.birthday, i.class_name, i.breed, i.learned_commands) for i in self._data]

    def _teach(self, animals_ids: list, new_command: str):
        if not self._teach_alert:
            self._teach_alert = MDDialog(
                title="Error",
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=lambda instance: self._dialog_close(self._teach_alert)
                    ),
                ],
            )
        try:
            super()._teach(animals_ids, new_command)
        except Exception as e:
            self._teach_alert.title = str(e)
            self._teach_alert.open()
        self._dialog_close(self._teach_dialog)
        self._view_update()

        Clock.schedule_once(self._deselect_rows)

    def _select_animal_alert(self):
        if not self._alert:
            self._alert = MDDialog(
                title="Error",
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=lambda instance: self._dialog_close(self._alert)
                    ),
                ],
            )
        self._alert.title = "Выберите животных"
        self._alert.open()

    def _teach_command(self, event):
        animals_ids = self._get_checked_animals_ids()
        if not animals_ids:
            self._select_animal_alert()
        else:
            text_field = MDTextField(hint_text="Команда")
            self._teach_dialog = MDDialog(
                title="Какой команде хотите обучить животных?" if len(
                    self._view.get_row_checks()) > 1 else "Какой команде хотите обучить животное?",
                type="custom",
                content_cls=MDBoxLayout(
                    text_field,
                    orientation="vertical",
                    spacing="12dp",
                    size_hint_y=None,
                    height="70dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="ОТМЕНА",
                        theme_text_color="Custom",
                        on_release=lambda instance: self._dialog_close(self._teach_dialog)
                    ),
                    MDFlatButton(
                        text="НАУЧИТЬ",
                        theme_text_color="Custom",
                        on_release=lambda instance: self._teach(animals_ids, text_field.text)
                    ),
                ],
            )
            self._teach_dialog.open()

    def _get_checked_animals_ids(self):
        return [i[0] for i in self._view.get_row_checks()]

    def _animals_delete(self, animals_ids):
        super()._animals_delete(animals_ids)
        self._view_update()
        self._dialog_close(self._delete_dialog)

        Clock.schedule_once(self._deselect_rows)

    def _deselect_rows(self, *args):
        self._view.table_data.select_all("normal")

    def _animals_delete_command(self, event):
        self.animals_ids = self._get_checked_animals_ids()
        if not self.animals_ids:
            self._select_animal_alert()
        else:
            if not self._delete_dialog:
                self._delete_dialog = MDDialog(
                    title="Подтвердите удаление",
                    type="custom",
                    content_cls="",
                    buttons=[
                        MDFlatButton(
                            text="ОТМЕНА",
                            theme_text_color="Custom",
                            on_release=lambda instance: self._dialog_close(self._delete_dialog)
                        ),
                        MDFlatButton(
                            text="УДАЛИТЬ",
                            theme_text_color="Custom",
                            on_release=lambda instance: self._animals_delete(self.animals_ids)
                        ),
                    ],
                )
            self._delete_dialog.open()


class Gui(MDApp):

    def __init__(self):
        super().__init__()

    def build(self):
        return AnimalMDScreen()


if __name__ == "__main__":
    Gui().run()