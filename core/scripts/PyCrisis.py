from coreJSON import *
from logic import Crisis
from PyCrisis import PyCrisis
from PyCrisisResolution import PyCrisisResolution
class PyCrisis(Crisis):
	def __init__(self, _NONE, _name, _description, _resolution):
		self._NONE = PyCrisis(**(o<<_NONE))
		self._name = _name
		self._description = _description
		self._resolution = PyCrisisResolution(**(o<<_resolution))
		Crisis.__init__(self, self._NONE, self._name, self._description, self._resolution)
