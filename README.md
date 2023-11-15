### Cheat No More

Built to revolutionize test taking internationally. Get pwnd N3Rds. Lol

### Creating a config file
```bash
    python3 config.py --filename <config>.yaml --create --user <my_user>
```

### Installing the requirements
```bash
    pip3 install -r requirements.txt
```

## Moving Forward
---

Okay, so now that everything is installed properly you can use the backend. The reason why I've set it up this way is so its simple to use in the state its in right now. The great thing about this stage because it comes out of the command line. 

<br>
---

### Setup.py Information
#### Do not run anyone of this code until everything is done... It is the big red button
The setup.py file is used when we want to distrubute the python project as a package that others can install and use. Here's a step-by-step quide on how to use it:

1. Create a setup.py file in the root directory of the project
2. Fill in the setup.py file with information about the project. 
```python3

    from setuptools import setup, find_packages

    setup(
        name='Your-Package-Name',
        version='0.1',
        packages=find_packages(),
        description='A short description of your project',
        author='Your Name',
        author_email='your.email@example.com',
        url='https://github.com/yourusername/your-package-name',
        install_requires=[
            'numpy',
            'pandas',
            # Add other dependencies here
        ],
    )
```
3. Once setup.py file is ready, we can create a distribution package of the project by running the following command in the terminnal: 
```bash 
python3 setup.py sdist
```

This command will create a source distribution (sdist) of the project. The distribution package will be a .tar.gz file in the dist directory of the project.

4. Others can now install the package by downloading the .tar.gz file and running the following command:

```bash 
pip3 install the-package-name.tar.gz
```

Replace the-package-name.tar.gz with the path to the tar.gz file

5. If you want to upload the package to the python Package Index  (PyPI), we can use the twine tool. First, install twine using pip: 
```bash
pip3 install twine
```

6. Then, upload the package to PyPI using the following command:
```bash 
twine upload dist/*
```

This command will opload all files in the dist directory to PyPI. We'll be prompted to enter a PyPI username and password.

7. Once the package is on PyPI, anyone can install it using pip: 
```bash
pip3 install the-package-name
```

Replace The-Package-Name with the name of the package

### Please do not run any of the code above