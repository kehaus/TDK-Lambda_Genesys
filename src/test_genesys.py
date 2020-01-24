#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script contains short hardware test sequences to illustrate how to use the 
GenesysBase class

Test scripts requires hardware to be connected to computer. Ensure that com 
port name is set correctly 


"""
__author__ = "kha"
__version__ = "1.0.0"


import time


from genesys_base import GenesysBase



com = '//dev//ttyUSB0'      # comport naming convention for Linux systems
                            #   change if necessary


# build up communication to request Hardware information
with GenesysBase(com) as g:
    print(g.get_model_id())
    print(g.get_software_version())

time.sleep(3)

# build up communication to change output 
with GenesysBase(com) as g:
    g.set_output_on()
    g.set_voltage(0)
    time.sleep(5)
    g.set_voltage(4)
    for i in range(10):
        print(g.get_voltage())
    g.set_voltage(0)
    g.set_output_off()
    



