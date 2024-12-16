import numpy as np

ptn = """.#.
..#
###
"""

card = np.array([list(x) for x in ptn.split()])
print(np.fliplr(card))
