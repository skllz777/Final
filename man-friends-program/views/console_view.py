from views.baseview import BaseView


class ConsoleView(BaseView):

    @staticmethod
    def print_msg(text: str):
        print(text)

    @staticmethod
    def input_func(text: str = ""):
        return input(text)

    def set_program_title(self, title: str):
        print(title)

    def choose_input(self, actions: dir, functions: dir, text: str, parameters: dir = None):
        action = None
        while action not in actions and action != 'q':
            print(text + " " + " ".join([f'{i} - {actions[i]}' for i in actions]) + ' q - выход')
            action = input()
            if action not in actions and action != 'q':
                print('Введены неверные данные')
        if action != 'q':
            if not parameters:
                functions[action]()
            else:
                functions[action](parameters[action])
        else:
            return False
        return True