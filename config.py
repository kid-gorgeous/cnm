import os
import yaml
import json
import argparse
from termcolor import colored


# This class will create a YAML configuration file for the user
#  to specify the path to the data, and the path to the external hard drive
# TODO: change default file path to a virtual path so when the operating system detects
# the hard drive it will automatically create a symbolic link to the external hard drive
class configuration:
    def help(self):
        message = """
        Configurations:
        -h or --help: Display the help message
        --filename: Specify the name of the YAML configuration file
        --config: Display the contents of the YAML configuration file
        --create: Create a YAML configuration file
        --user: Add a user to the YAML configuration file
        """
        # print('{}'.format(message))
        print(colored("{}\n".format(message), 'green'))

    def __init__(self, host='localhost', port=9999):
        self.filename = 'config.yaml'
        self.video = False
        self.video_size = [720, 480]
        self.text = '### YAML CONFIGURATION FILE ###'
        self.features = []
        self.face_recognition = False
        self.host = 'localhost'
        self.port = 9999
        self.user = os.getlogin()

    # Creates a YAML file with the default conditions
    def create_yaml(self):
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
            'user': self.user
        }
        try:
            if not os.path.exists(self.filename):
                with open(self.filename, 'w') as file:
                    yaml.dump(data, file, default_flow_style=False)
            else:
                raise Exception("{}\n".format('The file already exists.'))

        except Exception as e:
            # print("Error creating YAML file: {}".format(e))
            print(colored(e, 'green'))


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
# TODO: 
#   - Create a configuration file for the your username to link the path names
#   - Add os operations to the default ctor to create a symbolic link for the user name
#   - Add a class method function to add a feature to the YAML file
    pass