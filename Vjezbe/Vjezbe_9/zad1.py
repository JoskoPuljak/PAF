#moduli
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import planeti as plan

#definiranje objekta
Sunceizemlja=plan.dvaplaneta((0,0),(1.486*(10**11),0),29783)


#plot trajectory
Sunceizemlja.plot_trajectory(10000,31556909)
