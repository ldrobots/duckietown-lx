from typing import Tuple

import numpy as np


def PIDController(
    v_0: float, y_ref: float, y_hat: float, prev_e_y: float, prev_int_y: float, delta_t: float
) -> Tuple[float, float, float, float]:
    """
    PID performing lateral control.

    Args:
        v_0:        linear Duckiebot speed (constant).
        y_ref:      target y coordinate.
        y_hat:      the current estimated y.
        prev_e_y:   tracking error at previous iteration.
        prev_int_y: previous integral error term.
        delta_t:    time interval since last call.

    Returns:
        v_0:        linear velocity of the Duckiebot
        omega:      angular velocity of the Duckiebot
        e:          current tracking error (automatically becomes prev_e_y at next iteration).
        e_int:      current integral error (automatically becomes prev_int_y at next iteration).
    """
    
  

    # These are random values, replace with your implementation of a PID controller in here
    e = y_ref - y_hat
    e_int = prev_e_y + e*delta_t
    e_dif = (e-prev_e_y)/delta_t

    e = y_ref - y_hat
    e_int = prev_e_y + e*delta_t
    e_dif = (e-prev_e_y)/delta_t

        #91     #87         #85     #84
    k = 1       # 1.4       #8      #5
    ki = 0      # 0.5       #0.4    #1
    kd = 2   # 0.6       #3      #0.5

    omega = k*e + (ki * e_int) + kd * e_dif
    print("Omega: ", omega)
    print(e)
    omega = max(min(omega, 1), -1)    
    # ---
    
    return v_0, omega, e, e_int
