import numpy as np
from scipy.integrate import solve_ivp
from manim import *

def lorenz_system(t, state, sigma = 10, beta = 8/3, rho=28):
    """
    Defines the Lorenz system of differential equations.
    
    Parameters:
        t (float): Time variable (not used in equations but required by solver).
        state (list): State vector [x, y, z].
        sigma (float): Prandtl number.
        beta (float): Rayleigh number divided by geometric parameter.
        rho (float): Dimensionless parameter related to convection.
        
    Returns:
        list: Derivatives [dx/dt, dy/dt, dz/dt].
    """
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

def ode_solution_points(initial_conditions, state0, time, dt=0.01):
    """
    Solves the Lorenz system for given initial conditions and parameters.
    
    Parameters:
        initial_conditions (list): Initial state [x0, y0, z0].
        t_span (tuple): Time span (t_start, t_end).
        t_eval (array): Time points at which to store the solution.
        sigma (float): Prandtl number (default=10).
        beta (float): Rayleigh number divided by geometric parameter (default=8/3).
        rho (float): Dimensionless parameter related to convection (default=28).
        
    Returns:
        dict: Solution with time points and corresponding states.
    """
    solution = solve_ivp(
        lorenz_system, 
        t_span = (0, time), 
        y0 = state0, 
        t_eval= np.arange(0, time, dt),
    )
    return solution.y.T # Transpose to get states as rows

class LorenzAttractor(Scene):
    def construct(self):
        #set up the axis
        axes = ThreeDAxes()
        
        self.add(axes)