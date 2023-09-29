#!/bin/bash

python main.py &

jupyter notebook --ip='*' --port=8888 --no-browser --allow-root --notebook-dir=/app/analytics --NotebookApp.notebook_filename=exploratory_analysis.ipynb
