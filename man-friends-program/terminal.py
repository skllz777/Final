import traceback

from classes.animalregistryapp import AnimalRegistryApp
from views.console_view import ConsoleView


def main():
    ar_app = AnimalRegistryApp("man-friends.csv", ConsoleView)
    input_mode = True
    while input_mode:
        try:
            input_mode = ar_app.start()
        except IOError:
            traceback.print_exc()
            input_mode = False
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()