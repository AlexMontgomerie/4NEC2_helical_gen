# -*- coding: utf-8 -*-
try:
    from necpp import *
except ImportError:
    print('Install necpp using \"(sudo) pip install necpp\"')

#define: unitsL, meters

#prepare
context = nec_context()

#Begin to build geometry

g = context.get_geometry()

#One helix

g.helix()
