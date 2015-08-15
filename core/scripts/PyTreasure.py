from coreJSON import *
from logic import Treasure
class PyTreasure(Treasure):
	def __init__(self, _name, _value):
		self._name = _name
		self._value = _value
		Treasure.__init__(self, self._name, self._value)
