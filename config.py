import os
import yaml
from termcolor import colored

class configuration:
    def __init__(self, filename):
        self.filename = filename

    def create_yaml(self):
        data = "### YAML CONFIGURATION FILE CREATED ###"
        try:
            if not os.path.exists(self.filename):
                with open(self.filename, 'w') as file:
                    yaml.dump(data, file, default_flow_style=False)
            else:
                raise Exception("File already exists \n")
        except Exception as e:
            print(colored(e, 'red'))

    def read_yaml(self):
        with open(self.filename, 'r') as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            data = yaml.safe_load(file)
        return data
    

if __name__ == '__main__':
    filename = 'config.yaml'
    config = configuration(filename)
    # config.create_yaml()
    # config.read_yaml()
    # print(config.read_yaml())

    