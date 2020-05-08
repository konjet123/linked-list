from linked_list import __version__
from linked_list.linked_list import LinkedList, Node
import pytest

@pytest.fixture
def sample_object():
    veggies = LinkedList()
    veggies.insert("carrot")
    veggies.insert("tomatos")
    veggies.insert("spinach")
    return veggies

def test_version():
    assert __version__ == '0.1.0'

def test_linked_list_creation():
	ll = LinkedList()
	assert ll.head == None

def test_empty():
    node= Node("carrot")
    assert node.value == "carrot"
    assert node.next == None


def test_node_next(sample_object):
	assert sample_object.head.next.value == "tomatos"
	assert sample_object.head.next.next.value == "carrot"
	

def test_some(sample_object):
	assert sample_object.head.value == "spinach"
	assert sample_object.head.next.value == "tomatos"
	assert sample_object.head.next.next.value == "carrot"


def test_includes(sample_object):
	assert sample_object.includes("tomatos") 
	

def test_not_includes(sample_object):
	assert sample_object.includes("oranges")  == False

def test_linked_list_str(sample_object):
    assert '{ spinach } -> { tomatos } -> { carrot } -> None' == sample_object.__str__()