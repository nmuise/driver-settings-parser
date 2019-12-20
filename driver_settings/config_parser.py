import configparser
import sys
import os


def get_parameter_list(config):
    """Returns a list of all unique parameters present across all sections in 
    the given config.
    """
    par_list = []

    for section in config.sections():
        for setting in config[section]:
            if setting not in par_list:
                par_list.append(setting)
    return par_list

def get_parameter_dict(config, parameter_list=None):
    """Returns a dictionary mapping each config section to a list of all of its
    settings.
    """
    if parameter_list is None:
        parameter_list = get_parameter_list(config)

    parameter_dict = {}

    for section in config.sections():
        settings = []
        for setting in config[section]:
            settings.append(setting)
        parameter_dict.update({section:settings})
    
    return parameter_dict


def print_parsed_cnf(par_list, config):
    """Pretty-prints the given parsed config file to the console.
    """

    for section in config.sections():
        print(section)
        for par in par_list:
            if par in config[section]:
                print("    " + par + " = " + config[section][par])
            else:
                print("    " + par + " = DEFAULT")
        print("\n")
    return


def add_default_settings(config, def_config):
    """Adds default values into the config for any fields which have values
    defined in the default config, but which are not defined in the config. If
    a setting exists in the default config but has no value, no new setting is
    added to the newly-created config. 

    Returns the appended config.
    """
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
    """Writes out a file at the given output path/filename.
    """
    with open(out_file, 'w') as newfile:
        new_config.write(newfile)
        print("New config created: " + out_file)
    return


def main(config_file, default_file, out_file):
    """Given the supplied paths to config, default, and output files, assemble
    an appended version of config which contains parameters from the default
    as necessary, and write out that file.
    """
    # Create ConfigParse object for cnf file
    config = configparser.ConfigParser()
    config.read(config_file)

    # Create ConfigParse object for default settings cnf file
    default_config = configparser.ConfigParser()
    default_config.read(default_file)

    new_config = add_default_settings(config, default_config)

    write_new_config(new_config, out_file)

    return


if __name__ == "__main__":
    if len(sys.argv) == 1:
        config_file = 'drivers.cnf'
        default_file = 'driver_default_settings.cnf'
        out_file = 'driver_settings_complete.cnf'

        #Check if needed files exist
        if not os.path.exists(config_file):
            print("ERROR: no parameters were provided, but {0} did not lead to a file.".format(config_file))
            exit(3)
        if not os.path.exists(default_file):
            print("ERROR: no parameters were provided, but {0} did not lead to a file.".format(default_file))
            exit(3)

        main(config_file, default_file, out_file)
    else:
        if len(sys.argv) == 4:
            print("LEN 4")
            config_file = sys.argv[1]
            default_file = sys.argv[2]
            out_file = sys.argv[3]

            #check if supplied paths lead to files
            if not os.path.exists(config_file):
                print("ERROR: {0} does not lead to a readable file.".format(config_file))
                exit(2)
            if not os.path.exists(default_file):
                print("ERROR: {0} does not lead to a readable file.".format(default_file))
                exit(2)
            
            main(config_file, default_file, out_file)

        if len(sys.argv) != 4:
            print("ERROR: The usage of this command is:\r\n    $ python config_parser.py <config_file> <default_config_file> <output_path/filename>\r\nExactly three parameters must be provided.")
            exit(1)
