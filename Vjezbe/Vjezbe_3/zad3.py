import math as mt

import arithm as stat
print(stat.aritm_sred([1,2,2,2,3,4,5,6,7,8]))
print(stat.stand_dev([1,2,2,2,3,4,5,6,7,8]))


import numpy as np
print(np.mean([1,2,2,2,3,4,5,6,7,8]))
print(np.std([1,2,2,2,3,4,5,6,7,8]))

#standardna devijacija u numpyu je razlicita od standardne devijacije u našoj funkciji jer je ona napravljena za velik broj podataka, stoga je možemo podijeliti s n-1
print(np.std([1,2,2,2,3,4,5,6,7,8])/mt.sqrt(len([1,2,2,2,3,4,5,6,7,8])-1))
#dobijemo isti kao i u našem modulu

