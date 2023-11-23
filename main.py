
import os
import sys
import subprocess

INSTALL = 'pip install -r requirements.txt'

def install_requirements():
    process = subprocess.Popen(INSTALL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    # Print the output
    if process.returncode != 0:
        print(f"Error occurred: {stderr.decode('utf-8')}")
    else:
        print(f"Output: {stdout.decode('utf-8')}")

if __name__ == '__main__':

    print('Current working directory: ', os.getcwd())
    
    # install the cache dependencies
    import data.dataset_names as dataset_names
    print('Dataset names imported.')

    # install the requirements
    install_requirements()
    print('Requirements installed.')

    # configure the environment
    from config import configuration
    config = configuration()
    config.create_yaml()
    print('Configuration file created.')

