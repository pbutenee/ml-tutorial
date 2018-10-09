# Machine Learning Tutorial

To start the machine learning tutorial lauch Jupyter Notebook and open the release/1/inex.ipnb file with the following command:
```ipython notebook release/1/inex.ipnb```

You will need to have the following Python 3 packages installed:
* numpy
* scipy
* matplotlib
* sklearn
* pandas
* jupyter notebook

For convenience we advice to use the [Anaconda Python Package](https://www.continuum.io/downloads)


## JupyterHub (BETA)

If you want to host this workshop you can use the included Dockerfile to build a JupyterHub wich you can build and launch it with the following commands:
```docker build . -t ml-tutorial```
```docker run -p 8000:8000 ml-tutorial```

This will create a couple of users with as login `user00X` and password `password`.