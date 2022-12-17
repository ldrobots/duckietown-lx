from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    res[160:480, 320:640] = -0.5
    res[0:160, 260:640] = 0.5

    #res[0:160, 0:300] = 0.3
    res[200:480, 0:200] = 0.5
    res[280:480, 200:320] = 0.4

    
    #res[0:240, 320:640] = 0.2
    #res[240:480, 320:640] = -0.5
    # these are random values
    #only allow what  is right
  
    

   # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    res[160:480, 0:320] = -0.5
    res[0:160, 0:380] = 0.52
    #res[0:160, 320:640] = 0.3
    res[200:480, 440:640] = 0.5
    res[280:480, 320:440] = 0.4


    #res[240:480, 320:640] = 1.5
    #res[0:240, 320:640] = 1
    #res[240:480, 0:320] = -0.5
    #res[0:240, 0:320] = 0.2




    # these are random values
   

    # ---
    return res