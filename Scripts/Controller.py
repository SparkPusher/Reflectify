from .Model import Model
from .View import View
import sys

class Controller():

    def __init__(self):

        self.model = Model()
        self.viewport = View(self.model)
        pass

    def __del__(self):
        pass

