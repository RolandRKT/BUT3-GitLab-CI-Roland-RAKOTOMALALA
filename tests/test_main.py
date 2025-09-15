"""_summary_
"""

from greeting.main import greet
from greeting.utils import add


def test_greet():
    """_summary_
    """
    assert greet("World") == "Hello, World!"


def test_add():
    """_summary_
    """
    assert add(5, 7) == 12


test_add()


test_greet()
