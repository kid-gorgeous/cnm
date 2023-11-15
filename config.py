import os
import yaml
import json
import argparse
from termcolor import colored

# If this arguements wrong, print the help message that will offer the correct arguements
class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help()
        print(colored("config.py: error: {}\n".format(message), 'red'))
        print(colored("Please provide the config name with --config <config_name>", 'red'))
        exit(2)

# This class will create a YAML configuration file for the user
#  to specify the path to the data, and the path to the external hard drive
# TODO: change default file path to a virtual path so when the operating system detects
# the hard drive it will automatically create a symbolic link to the external hard drive
class configuration:
    def help(self):
        message = """
            -h or --help: Display the help message
            --filename: Specify the name of the YAML configuration file
            --config: Display the contents of the YAML configuration file
            --create: Create a YAML configuration file
            --user: Add a user to the YAML configuration file
        """
        print(colored("{}\n".format(message), 'green'))

    def __init__(self, filename, host='localhost', port=9999):
        self.filename = filename
        self.video = False
        self.video_size = [720, 480]
        self.text = '### YAML CONFIGURATION FILE ###'
        self.features = []
        self.face_recognition = False
        self.host = 'localhost'
        self.port = 9999
        self.user = 'root'

    # Creates a YAML file with the default conditions
    def create_yaml(self, filename):
        data = {
            'filename': self.filename,
            'video': self.video,
            'video_size': self.video_size,
            'device': 'mps', # unless windows then 'cpu'
            'text' : self.text,
            'features': [],
            'face_recognition': False,
            'host': 'localhost',
            'port': 9999,
            'user': 'user' 
        }
        try:
            if not os.path.exists(self.filename):
                with open(self.filename, 'w') as file:
                    yaml.dump(data, file, default_flow_style=False)
            else:
                raise Exception("{}\n".format(data))
        except Exception as e:
            print(colored(e, 'green'))

    # Adds a user to the YAML file
    def add_user(self, user):
        try:
            data = self.load_config()
            
            data.update({'user': user})

            with open(self.filename, 'w') as file:
                yaml.dump(data, file, default_flow_style=False)
        except Exception as e:
            print("Error updating user: {}".format(e))

    # Reads the YAML file
    def read_yaml(self):
        try:
            with open(self.filename, 'r') as file:
                data = yaml.safe_load(file)
            return json.dumps(data)

        except FileNotFoundError:
            print("File {} not found.".format(self.filename))

        except yaml.YAMLError as exc:
            print("Error in configuration file: {}".format(exc))
    
    def load_config(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                self.video = config['video']
                self.video_size = config['video_size']
                self.text = config['text']

                yaml.safe_dump({'features': []}, file)

        elif os.path.getsize(self.filename) == 0:
            raise ValueError('The YAML file is empty')
            return {}
        
        with open(self.filename, 'r') as file:
            config = yaml.safe_load(file)
        if not isinstance(config, dict):
            raise TypeError('Expected a dictionary in the YAML file')
        return config
    

if __name__ == '__main__':

    # Examples:

    # filename = 'config.yaml'
    # config = configuration(filename)

    # Download file and change username to specify a user
    #   to create a file path. I have not added this os feature 
    #   to the default configuration constructor (__init__)
    # config.add_user('username')

    # Display the YAML information for conformation
    # settings = config.load_config()
    # print(settings)

#-------------------------#
    # Adding parser for cli interaction
    parser = argparse.ArgumentParser(description='Create a YAML configuration file')

    parser.add_argument('--filename', type=str, default='config.yaml', help='Name of the configuration file')
    parser.add_argument('--config', action='store_true', help='Display contents of the configuration file') 
    parser.add_argument('--create', action='store_true', help='Create a YAML configuration file')
    parser.add_argument('--user', type=str, help='Add a user to the YAML configuration file')

    args = parser.parse_args()
    config = configuration(args.filename)

    if args.create:
        config.create_yaml(args.filename)
    if args.config:
        config.read_yaml()
    if args.user:
        config.add_user(args.user)
    if args.filename:
        config.filename = args.filename
        # print(colored("{}".format(config.filename), "green"))
    else:
        pass

# TODO: 
#   - Create a configuration file for the your username to link the path names
#   - Add os operations to the default ctor to create a symbolic link for the user name
#   - Add a class method function to add a feature to the YAML file