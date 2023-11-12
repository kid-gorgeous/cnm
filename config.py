import os
import yaml
from termcolor import colored

class configuration:
    
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

    def create_yaml(self):
        data = {
            'filename': f"{self.filename}",
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
                raise Exception("File already exists \n")

        except Exception as e:
            print(colored(e, 'red'))

    def add_user(self, user):
        data = self.read_yaml()
        data['user'] = user
        with open(self.filename, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)

    def read_yaml(self):
        try:
            with open(self.filename, 'r') as file:
                data = yaml.safe_load(file)
            return data

        except FileNotFoundError:
            print(f"File {self.filename} not found.")

        except yaml.YAMLError as exc:
            print(f"Error in configuration file: {exc}")
    
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

    def addfeature(self, feature):
        config = self.load_config()
        if 'features' not in config:
            config['features'] = []
        elif not isinstance(config['features'], list):
            raise ValueError('Expected a list under the key "features" in the YAML file')
        config['features'].append(feature)
        with open(self.filename, 'w') as file:
            yaml.dump(config, file, default_flow_style=False)

    

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

    pass

# TODO: 
#   - Create a configuration file for the your username to link the path names
#   - Add os operations to the default ctor to create a symbolic link for the user name
#   - Add a class method function to add a feature to the YAML file