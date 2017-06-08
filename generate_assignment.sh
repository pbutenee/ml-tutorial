#!/bin/bash
set -e
nbgrader assign 1 --force
cp release/1/index.ipynb .

rm -r data
mkdir data
cp source/1/data/* data/

rm -r images
mkdir images
cp source/1/images/* images/
