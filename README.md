######################################## HOW TO USE CONFIG_PARSER.PY #######################################################

########################################### CREATE CONFIG FILE ############################################################
Create a .cnf file in a text editor
Each section and setting must be written on a new line.
At least one section is required.
Settings may be used more than once but not in the same section.
Spaces, tabs, and comments denoted by # are ignored.

Each configuration section is named:     [name]
Each setting is written as:              setting_name = value

EXAMPLE:
[hp8]
 printer						= lwfi/bser
 fd								= unicode.dgs
 phy_img_compression			= rlencode
 #Dont display
 phy_tech_top_margin			= 0 mm
 output_unicode_mode=8bits
 
 hib1	= "&11H"/A4,S/A3,S/LETTER,LEGAL,S/EXECUTIVE,S

## Section 2 ##

[ps]
iso_grey_level					= 0
hob1							= "&11G"

printer							= 1j4p/ps
margin_mode=1


########################################### CREATE DEFAULT FILE ###########################################################
Create another .cnf file in a text editor

If a setting in any section of the default file is not present in a section of the config file, the setting from the defualt file will be added to the configuration's output.

Conventions of the default file are the same as the config file. There must be at least one section. Additional sections are valid but are ignored within the script.

Settings may have an empty value.
Settings may be used more than once but not in the same section.


########################################### RUNNING THE SCRIPT ############################################################

Open the config_parser.py file in an editor

At the top of the code, edit the INPUT FILES and OUTPUT FILE fields.
CONFIG_FILEPATH = filepath (and file) to your config file
DEFAULT_FILEPATH = filepath (and file) to your default file
OUTPUT_FILEPATH = filepath (and file name) you desire your new .cnf to be created




