'''
Created on Oct 15, 2016

@author: thierry
'''


constant_unit = 10
constant_card_height = 15 * constant_unit
constant_card_width  = 10 * constant_unit
constant_nb_cols = 4
constant_nb_rows = 3
constant_color_background = (0.0, 0.4, 0.0, 1.0)    # rgba
constant_color_highlight  = (1.0, 0.2, 0.2, 0.6)    # rgba
constant_color_card       = (1.0, 1.0, 1.0, 1.0)    # rgba
constant_color_card_back  = (0.0, 0.2, 0.0, 1.0)    # rgba
constant_color_blue       = (0.0, 0.0, 0.8, 1.0)    # rgba
constant_color_blue_half  = (0.0, 0.0, 0.8, 0.3)    # rgba
constant_color_red        = (0.8, 0.0, 0.0, 1.0)    # rgba
constant_color_red_half   = (0.8, 0.0, 0.0, 0.3)    # rgba
constant_color_green      = (0.0, 0.8, 0.0, 1.0)    # rgba
constant_color_green_half = (0.0, 0.8, 0.0, 0.3)    # rgba
constant_spacing = constant_unit
constant_padding = constant_unit
constant_table_width  =  constant_card_width *  constant_nb_cols      \
                      +     constant_spacing * (constant_nb_cols - 1) \
                      +     constant_padding * 2
constant_table_height = constant_card_height *  constant_nb_rows      \
                      +     constant_spacing * (constant_nb_rows - 1) \
                      +     constant_padding * 2


