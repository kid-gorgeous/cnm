import os
import yaml
from termcolor import colored

class configuration:
    def __init__(self, filename):
        self.filename = filename
        self.video = False
        self.video_size = [720, 480]
        self.text = '### YAML CONFIGURATION FILE ###'

    def create_yaml(self):
        data = {
            'filename': f"{self.filename}",
            'video': self.video,
            'video_size': self.video_size,
            'text' : self.text,
        }

        try:
            if not os.path.exists(self.filename):
                with open(self.filename, 'w') as file:
                    yaml.dump(data, file, default_flow_style=False)
            else:
                raise Exception("File already exists \n")

        except Exception as e:
            print(colored(e, 'red'))

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
    # settings = config.load_config()
    # print(settings)