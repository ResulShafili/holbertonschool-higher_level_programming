#!/usr/bin/python3
import abc from ABC
"""
this program defines sound of animals
"""

class Animal(ABC):
    """
    this is anaimal class
    """
    @abstractmethod
    def sound():
        """
        this is abstarct sound metheod
        """
        pass

class Dog(Animal):
    """this is class dog which is inherited from Animal class"""
    def sound():
        """this is mehtod sound for dog class"""
        return "Bark"

class Cat(Animal):
    """this is class cat which is inherited from Animal class"""
    def sound():
        """this is mehtod sound for cat class"""
        return "Meow"
