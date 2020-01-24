# -*- coding: utf-8 -*-
"""
Base class representation of the TDK-Lambda Genesys 750W / 1500W power supply. 

Commanication commands and procedure implemented in this code is based on the description given in the 
Genesys USER MANUAL. 

The user manual can be found under this link:
https://www.us.tdk-lambda.com/hp/product_html/genesys1u.htm



"""

__version__ = "0.0.1"
__author__ = "kha"



import serial





_INIT_CMD = {
    'address':                  'ADR',
    'clear_status':             'CLS',
    'reset':                    'RST',
    'remote_mode':              'RMT',
    'multi-drop_option':        'MDAV',
    'master-slave':             'MS'
}

_ID_CMD = {
    'identification':           'IDN',
    'software_version':         'REV',
    'serial_number':            'SN',
    'date_of_last_test':        'DATE'
}

_OUTPUT_CMD = {
    'set_voltage':              'PV',
    'actual_voltage':           'MV',
    'set_current':              'CV',
    'actual_current':           'MC',
    'operation_mode':           'MODE',
    'display_V_n_C':            'DVC',
    'power_supply_status':      'STT',
    'adc_filter':               'FILTER',
    'output_mode':              'OUT',
    'foldback_protection':      'FLD',
    'foldback_delay':           'FLB',
    'reset_foldback_delay':     'RSTFLB',
    'over_voltage_protection':  'OVP'
    'ovp_maximum':              'OVM',
    'under_voltage_limit':      'UVL',
    'auto_restart_mode':        'AST',
    'save_settings':            'SAV',
    'recall_last_settings':     'RCL'
}


    
