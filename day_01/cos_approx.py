#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Qusai Al Shidi'
__email__ = 'qusai@umich.edu'

# =============================================================================
# from math import factorial
# from math import pi
# import math
# import numpy as np
# =============================================================================


def cos_approx(x, accuracy=10):
    """
    This funct is used for testing comprehended
    
    Examples:
        from math import pi
        cos_approx(pi) = -1.0
    """
    comprehended = [x**(2*n)*(-1)**n/math.factorial(2*n) for n in range(accuracy)] 
    sum_val = sum(comprehended)
    return sum_val


# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    print("cos(0) = ", cos_approx(0))
    print("cos(pi) = ", cos_approx(pi))
    print("cos(2*pi) = ", cos_approx(2*pi))
    print("more accurate cos(2*pi) = ", cos_approx(2*pi, accuracy=50))


# =============================================================================
# import matplotlib.pyplot as plt  # here is the good stuff
# 
# x = np.linspace(0, 1)  # default num is 50
# y = np.exp(x)
# plt.plot(x, np.exp(x))
# 
# plt.xlabel(r'$0 $\le$ x < 1$')
# plt.ylabel(r'$e^x$')
# plt.title('Exponential function')
# plt.show()  # shows plot, can be saved
# =============================================================================

"""A 3D plot script for spherical coordinates.
"""
# =============================================================================
# __author__ = 'Yu Hong'
# __email__ = 'yu.hong@mavs.uta.edu'
# 
# # import shit
# from datetime import datetime # for date convert
# from swmfpy.web import get_omni_data # package
# import matplotlib.pyplot as plt  # use for plot
# from matplotlib import dates as mdates # use for date format
# 
# #%% give the start and end time
# start_time = datetime(1994, 5, 21) # start time 
# end_time = datetime(1994, 5, 22) # end time
# data = get_omni_data(start_time, end_time)  # returns a dictionary
# data.keys()
# 
# #%% extract our parameters
# al = data['al'] # AL index 
# stmp = data['times'] # time
# 
# #%%
# time_fmt = '%H:%M:%S' # time format
# 
# fig,ax = plt.subplots(1,1,figsize=(10,5)) # set figures format 
# 
# ax.xaxis.set_major_formatter(mdates.DateFormatter(time_fmt)) # axis format 
# plt.plot(stmp, al)
# plt.ylabel(r'$AL (nT)$', font = '25')
# plt.xlabel(r'$UT  (hours)$', font = '25')
# plt.title('AL during 1994-05-22')
# =============================================================================












