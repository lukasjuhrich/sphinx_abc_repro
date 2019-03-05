from abc import ABCMeta, abstractmethod

class Foo(metaclass=ABCMeta):
    """A class!"""

    @classmethod
    @abstractmethod
    def abstract_cm(cls):
        """This is an abstract cm!"""
        pass


    @property
    @abstractmethod
    def value(self):
        """This is an abstract property."""
        pass
