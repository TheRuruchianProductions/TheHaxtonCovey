from coreJSON import *
from logic import Location
from PyTreasureReference import PyTreasureReference
from PyCrisisReference import PyCrisisReference
class PyLocation(Location):
	def __init__(self, _name, _treasures, _events):
		self._name = _name
		self._treasures = [PyTreasureReference(**(o<<a)) for a in _treasures]
		self._events = [PyCrisisReference(**(o<<a)) for a in _events]
		Location.__init__(self, self._name, self._treasures, self._events)
