"""_summary_
"""

from greeting.main import greet
from greeting.utils import add, sub


def test_greet():
    """_summary_
    """
    assert greet("World") == "Hello, World!"


def test_add():
    """_summary_
    """
    assert add(5, 7) == 12


def test_sub():
    """_summary_
    """
    assert sub(5, 7) == -2


test_add()


test_greet()


test_sub()
