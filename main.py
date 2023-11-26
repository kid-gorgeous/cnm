
import os
import sys
import subprocess

INSTALL = 'pip install -r requirements.txt'

def check_python_installed():
    command = "python3 --version"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print("Python is not installed.")
    else:
        print(f"Python is installed: {stdout.decode('utf-8')}")

def check_node_installed():
    command = "node --version"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print("Node is not installed.")
    else:
        print(f"Node is installed: {stdout.decode('utf-8')}")


def check_dependencies():
    
    check_python_installed()
    
    check_node_installed()


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


    # check if the dependencies are installed
    check_dependencies()
    print('Dependencies installed.')