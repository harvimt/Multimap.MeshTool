from args import *
from ..base_filters import *
import collada
import os

def FilterGenerator():
    class ColladaLoadFilter(LoadFilter):
        def __init__(self):
            super(ColladaLoadFilter, self).__init__('load_collada', 'Loads a collada file')
        def apply(self, filename):
            if not os.path.isfile(filename):
                raise FilterException("argument is not a valid file")
            try:
                col = collada.Collada(filename)
            except collada.DaeError as e:
                print e
                raise FilterException("errors while loading file")
                
            return col
    return ColladaLoadFilter()
