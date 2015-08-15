from coreJSON import *
from logic import CrisisResolution
from PyPerson import PyPerson
class PyCrisisResolution(CrisisResolution):
	def __init__(self, _resolver, _tech, _mech, _charisma):
		self._resolver = PyPerson(**(o<<_resolver))
		self._tech = _tech
		self._mech = _mech
		self._charisma = _charisma
		CrisisResolution.__init__(self, self._resolver, self._tech, self._mech, self._charisma)
