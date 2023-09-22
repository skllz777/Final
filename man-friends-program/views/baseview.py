from abc import ABC, abstractmethod


class BaseView(ABC):
    @abstractmethod
    def set_program_title(self, title: str):
        pass

    @abstractmethod
    def choose_input(self, actions: dir, functions: dir, text: str, parameters: dir = None):
        pass