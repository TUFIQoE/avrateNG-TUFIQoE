#!/usr/bin/env python3
import os
import sys
import argparse
import pandas as pd  # requires panda installation
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load libs from lib directory
import loader
from log import *
from system import *


def main(params=[]):
    parser = argparse.ArgumentParser(description='avrateNG do some plots on generated csv file', epilog="mschaab 2017", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--cvsfilename', type=str, default="ratings.csv", help='filename of cvs file (generated by function convert_ratings_to_csv.py)')
    parser.add_argument('--group_by', type=str, default="video_name", help='Column by which the data is being grouped and plotted')

    argsdict = vars(parser.parse_args())
    lInfo("read {}".format(argsdict["cvsfilename"]))

    # Read in csv file and convert to pandas dataFrame
    ratingData = pd.read_csv(argsdict["cvsfilename"], sep=';', header=0, index_col=False)
    ratingData['rating'] = pd.to_numeric(ratingData['rating'], errors='coerce')

    # Check if grouping variable is valid
    if argsdict["group_by"] not in ratingData.columns:
        sys.exit('No valid grouping variable, use e.g. {}'.format(ratingData.columns))
    else:
        lInfo('Grouping data by {}'.format(argsdict["group_by"]))



    # Boxplot grouped by given grouping variable
    ratingData.boxplot(column='rating', by=argsdict["group_by"])
    #ratingData['rating_type'].plot.hist(by=argsdict["group_by"])
    plt.figure()
    ratingCategorical = ratingData[ratingData.rating.isnull()]
    print(ratingCategorical)
    sns.countplot(x=argsdict["group_by"], hue='rating_type', data=ratingCategorical, palette="Greens_d")
    plt.show()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))