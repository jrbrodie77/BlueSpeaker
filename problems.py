from pyo import *
s = Server().boot()
s.start()
sf = SfPlayer('01 dancing queen.aif', loop=False).out()
s.gui(locals())