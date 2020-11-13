# Machine Learning Tutorial
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Installation

#### Option 1: Anaconda (new Python users)

Download the Python 3 [Anaconda installer](https://www.anaconda.com/distribution/#download-section) for your OS and open the Anaconda prompt.

Clone this repo using git or download it manually. Then, using the Anaconda prompt, cd into the ml-tutorial directory and move on to [Starting the tutorial](#Starting the tutorial).
 

        
#### Option 2: pip & virtual environment (advanced users)

Clone the repo and create a [virtual environment](https://docs.python.org/3/library/venv.html) in the root folder. After activating the environment, install the required packages:

        pip install -r requirements.txt

## Starting the tutorial

Open the `release/1/index.ipynb` Jupyter notebook with the following command:

        jupyter notebook release/1/index.ipynb

## Updating the tutorial

Activate the nbgrader notebook extension as documented [here](https://nbgrader.readthedocs.io/en/stable/user_guide/installation.html#installing-and-activating-extensions).
Change the notebooks in the `source/` folder, any new cells where students have to write code should be set to `Autograded answer` as documented [here](https://nbgrader.readthedocs.io/en/stable/user_guide/creating_and_grading_assignments.html#autograded-answer-cells).

After saving your changes, run:

        sh generate_assignment.sh

This will overwrite the existing `release/` directory.

While creating the notebooks in the `release/` directory, the [nbgrader](https://nbgrader.readthedocs.io/en/stable/) package will alter code segments that look like:

        ### BEGIN SOLUTION
        foo = bar
        ### END SOLUTION
        
into:

        ##### Implement this part of the code #####
        raise NotImplementedError("Code not implemented, follow the instructions.")
        
As specified in the `nbgrader_config.py` file.

## JupyterHub (BETA)

If you want to host this workshop you can use the included Dockerfile to build a JupyterHub which you can build and launch with the following commands:

```docker build . -t ml-tutorial```

```docker run -p 8000:80 ml-tutorial```

Surf to `http://localhost:8000` to start the tutorial and log in with `user001` and password `password`.

The docker image is also available on docker hub so running it might also work with:
```docker run -p 8000:80 pbutenee/ml-tutorial```
without the need for downloading the code or building the container.
