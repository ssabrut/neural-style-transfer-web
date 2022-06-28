# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:31:20 2022

@author: micha
"""

import tensorflow as tf

def gram_matrix(tensor):
    result = tf.linalg.einsum('bijc,bijd->bcd', tensor, tensor)
    