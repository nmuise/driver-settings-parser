---
## HOW TO USE CONFIG_PARSER.PY

### 0. Quick reference for experienced users
`python config_parser.py <config_file> <default_config_file> <output_path/filename>`

`python config_parser.py` *(With the following files in the same directory as the script)*:
* `drivers.cnf`
* `driver_default_settings.cnf`

### 1. Create config file
* Create a .cnf file called `drivers.cnf` in a text editor
    * You can give it any name, but if you don't call it this you'll have to remember it later.
* Each section and setting must be written on a new line.
* At least one section is required.
    * Each configuration section is named:     [name]
    * Each setting is written as:              setting_name = value
* Settings may be used more than once but not in the same section.
* Spaces, tabs, and comments denoted by # are ignored.

#### EXAMPLE .cnf FILE:
```
[hp8]
 printer = lwfi/bser
 fd = unicode.dgs
 phy_img_compression = rlencode
 #Dont display
 phy_tech_top_margin = 0 mm
 output_unicode_mode=8bits
 
 hib1	= "&11H"/A4,S/A3,S/LETTER,LEGAL,S/EXECUTIVE,S

## Section 2 ##

[ps]
iso_grey_level = 0
hob1 = "&11G"

printer = 1j4p/ps
margin_mode=1
```

### 2. Create default config file
This file is used to define default values for certain sections.

* Create a .cnf file called `driver_default_settings.cnf` in a text editor.
    * You can give it any name, but if you don't call it this you'll have to remember it later.
* If a setting in any section of the default file is not present in a section of the config file, the setting from the defualt file will be added to the configuration's output.
* Format/content requirements of the default file are the same as the config file.
    * There must be at least one section. 
    * Additional sections are valid but are ignored within the script.
    * Settings may have an empty value.
        * Default values that are empty won't be added into config files.
    * Settings may be used more than once but not in the same section.


### 3. Run the script
Use either of the following two commands in a command prompt in the same directory as the script:
* `python config_parser.py <config_file> <default_config_file> <output_path/filename>`

* `python config_parser.py` *(With the following files in the same directory as the script)*:
    * `drivers.cnf`
    * `driver_default_settings.cnf`
