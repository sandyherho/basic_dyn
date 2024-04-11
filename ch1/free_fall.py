#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 04:51:48 2024

@author: Sandy Herho
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
plt.style.use("bmh")

grav_const = 9.81 # [m/s]
init_pos = 0 # [m]
init_vel = .5 # [m/s]
init_mass = 5 # [kg]

init_cond = [init_pos, init_vel, init_mass]

init_time = 0 # [s]
final_time = 5 # [s]
num_data = 100
tout = np.linspace(init_time, final_time, num_data)

def free_fallling_obj(time, state, grv_const):
    x1, x2, x3 = state
    dxdt = [x2,
            grv_const + (x3 - 2)*(x2/x3),
            -x3 + 2]
    return dxdt

sol = solve_ivp(free_fallling_obj, (init_time, final_time),
                init_cond, t_eval=tout, args=(grav_const,))

xout = sol.y

plt.figure(1)
plt.plot(tout, xout[0, :])
plt.xlabel(r"$t$ [s]", fontsize=18)
plt.ylabel(r"$x$ [m]", fontsize=18)
plt.tight_layout()

plt.figure(2)
plt.plot(tout, xout[0, :])
plt.xlabel(r"$t$ [s]", fontsize=18)
plt.ylabel(r"$\dot{x}$ [m/s]", fontsize=18)
plt.tight_layout()

plt.figure(3)
plt.plot(tout, xout[0, :])
plt.xlabel(r"$t$ [s]", fontsize=18)
plt.ylabel(r"$m$ [kg]", fontsize=18)
plt.tight_layout()