from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    print (shape)
    res = np.zeros(shape=shape, dtype="float32")
    res[210:480, 320:600] = -1.5
    res[0:200, 200:640] = 1

    res[300:480, 0:240] = 1.2
    #res[0:240, 320:640] = 0.2
    #res[240:480, 320:640] = -0.5
    # these are random values
    #only allow what  is right
  
    

   # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    res[210:480, 40:320] = -1.5
    res[0:200, 0:400] = 1
    res[300:480, 400:640] = 1.2


    #res[240:480, 320:640] = 1.5
    #res[0:240, 320:640] = 1
    #res[240:480, 0:320] = -0.5
    #res[0:240, 0:320] = 0.2




    # these are random values
   

    # ---
    return res