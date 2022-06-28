# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:31:20 2022

@author: micha
"""

import tensorflow as tf
from tensorflow.keras import Model

def gram_matrix(tensor):
    """
    
    Get the gram matrix from the i and j product (Gij)
    
    Parameters
    ----------
    tensor : Output tensor from each style layer output.

    Returns
    -------
    None.
    
    """
    
    result = tf.linalg.einsum('bijc,bijd->bcd', tensor, tensor) # equation pattern from gram matrix with batches
    gram_matrix = tf.expand_dims(result, axis=0) # add batches to outer layer
    input_shape = tf.shape(tensor) # get the shape of input tensor
    i_dot_j = tf.cast(input_shape[1] * input_shape[2], tf.float32) # convert the dot product to tf float32
    return gram_matrix / i_dot_j

def load_pre_trained_model(weights=None):
    """

    Create the pre trained model

    Parameters
    ----------
    weights : Path to local weights.

    Returns
    -------
    model : Keras class Model loaded with pre trained model.

    """
    
    vgg = tf.keras.applications.VGG19(include_top=False, weights=weights) # initialize pre trained model
    vgg.load_weights(weights) # load the pre trained model weights
    content_layers = ['block4_conv2'] # select the layer for content layer
    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1'] # select the layer for style layer
    content_output = vgg.get_layer(content_layers[0]).output # get the content layer output
    style_output = [vgg.get_layer(style_layer).output for style_layer in style_layers] # get all the style layer output
    gram_style_output = [gram_matrix(output) for output in style_output] # get the gram matrix for all output style layer
    model = Model([vgg.input], [content_output, gram_style_output])
    return model