"""\
Basis set constructor

>>> from pyquante2.geo.samples import h
>>> basisset(h,'sto3g')
    [cgbf((0.0, 0.0, 0.0),(0, 0, 0),[3.42525091, 0.62391373, 0.1688554],[0.1543289707029839, 0.5353281424384733, 0.44463454202535485])]

Haven't figured out how to test the basis set yet. Print it out?

Copyright (c) 2004, Richard P. Muller. All Rights Reserved. 

 PyQuante version 1.2 and later is covered by the modified BSD
 license. Please see the file LICENSE that is part of this
 distribution. 
"""

from pyquante2 import settings
from pyquante2.basis import data
from pyquante2.basis.cgbf import cgbf
from pyquante2.basis.tools import sym2pow

class basisset:
    def __init__(self,atoms,name,**kwargs):
        self.bfs = []
        basis_data = getattr(data,name)
        omit_f = kwargs.get('omit_f',settings.omit_f)
        for atom in atoms:
            for sym,prims in basis_data[atom.atno]:
                if omit_f and sym == 'F': continue
                exps = [e for e,c in prims]
                coefs = [c for e,c in prims]
                for power in sym2pow[sym]:
                    self.bfs.append(cgbf(atom.r,power,exps,coefs))
        return

    def __getitem__(self,i): return self.bfs.__getitem__(i)
    def __repr__(self): return repr(self.bfs)
    def __len__(self): return len(self.bfs)

# Can define shellbasisset here, which is essentially a normal basis set, but has the functions
# shorted into shells. Overload the normal basis set.

if __name__ == '__main__':
    import doctest
    doctest.testmod()