# Machine Learning Tutorial
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Installation

Clone the repo and create a [virtual environment](https://docs.python.org/3/library/venv.html) in the root folder. After activating the environment, install the required packages:

        pip install -r requirements.txt

## Taking the tutorial

Open the `release/1/index.ipynb` Jupyter notebook with the following command:

        jupyter notebook release/1/index.ipynb

## Updating the tutorial

Change the notebooks in the `source/` folder and, after saving your changes, run:

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
