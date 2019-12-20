import configparser


# These files should be changed to your desired filepaths
# INPUT FILES
# .cnf file with configuration settings
CONFIG_FILEPATH = 'C:/Users/bleblanc/Documents/Scripts/driver_settings/drivers.cnf'
# .cnf file with default configuration settings to be used when a section within a config file section does not exist
DEFAULT_FILEPATH = 'C:/Users/bleblanc/Documents/Scripts/driver_settings/driver_default_settings.cnf'

# OUTPUT FILE
OUTPUT_FILEPATH = 'C:/Users/bleblanc/Documents/Scripts/driver_settings/driver_settings_complete.cnf'


# Get all parameters present across all sections
# Each section uses all parameters but default if not assigned in cnf sections
# Sets standard order of parameters to appear in each section
def get_parameter_list(sect_list, config):
    par_list = []

    for section in sect_list:
        for setting in config[section]:
            if setting not in par_list:
                par_list.append(setting)
    return par_list


# Print cnf
def print_parsed_cnf(par_list, sect_list, config):
    for section in sect_list:
        print(section)
        for par in par_list:
            if par in config[section]:
                print("    " + par + " = " + config[section][par])
            else:
                print("    " + par + " = DEFAULT")
        print("\n")
    return


# default_config holds every setting
# if config doesnt have a setting existing in default_config, use default_config's setting default and add to new_config
# if default_config does not have a default setting, do not add setting to the new_config
# return the edited new_config object
def add_default_settings(config, def_config):
    new_config = configparser.ConfigParser()
    sects = config.sections()
    def_sects = def_config.sections()
    for section in sects:
        old_section_name = str(config[section])
        temp = old_section_name.replace("<Section: ", '')
        new_section_name = temp.replace(">", '')

        if new_section_name == "END":
            break
        # initialize dictionary to hold append setting key-value pairs to and later add to config object's section
        new_setting_dict = {}

        for def_section in def_sects:
            for def_setting in def_config[def_section]:
                # Do not add the same setting into the dictionary twice
                if def_setting not in new_setting_dict:

                    if def_setting in config[section]:
                        new_setting_dict["    " + str(def_setting)] = config[section][def_setting]
                    else:
                        new_setting_dict["    " + str(def_setting)] = def_config[def_section][def_setting]

        # create a new section in new_config and add the dictionary to that section
        new_config[new_section_name] = new_setting_dict

    return new_config


def write_new_config(new_config, out_file):
    with open(out_file, 'w') as newfile:
        new_config.write(newfile)
        print("File: " + out_file)
    return


def main(file, def_file, out_file):
    # Set file input/output conventions


    # Create ConfigParse object for cnf file
    config = configparser.ConfigParser()
    config.read(file)
    # Create ConfigParse object for default settings cnf file
    default_config = configparser.ConfigParser()
    default_config.read(def_file)

    # sect_list = default_config.sections()
    # par_list = get_parameter_list(sect_list, default_config)
    # print_parsed_cnf(par_list,sect_list, default_config)

    new_config = add_default_settings(config, default_config)

    write_new_config(new_config, out_file)

    # sect_list = config.sections()

    # par_list = get_parameter_list(sect_list, config)

    # print_parsed_cnf(par_list, sect_list, config)
    return


if __name__ == "__main__":
    file = CONFIG_FILEPATH
    def_file = DEFAULT_FILEPATH
    out_file = OUTPUT_FILEPATH
    main(file, def_file, out_file)

