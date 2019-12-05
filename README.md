# Machine Learning Tutorial

To start the machine learning tutorial launch Jupyter Notebook and open the release/1/index.ipynb file with the following command:
```ipython notebook release/1/index.ipnb```

You will need to have the following Python 3 packages installed:
* numpy
* scipy
* matplotlib
* sklearn
* pandas
* jupyter notebook

For convenience we advise to use the [Anaconda Python Package](https://www.continuum.io/downloads)


## JupyterHub (BETA)

If you want to host this workshop you can use the included Dockerfile to build a JupyterHub which you can build and launch with the following commands:

```docker build . -t ml-tutorial```

```docker run -p 8000:80 ml-tutorial```

Surf to `http://localhost:8000` to start the tutorial and log in with `user001` and password `password`.

The docker image is also available on docker hub so running it might also work with:
```docker run -p 8000:80 pbutenee/ml-tutorial```
without the need for downloading the code or building the container.
