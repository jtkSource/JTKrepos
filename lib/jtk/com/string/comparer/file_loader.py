__author__ = 'jubin'

import pandas as pd
import numpy as np
import jtk.com.string.comparer.algo as algo

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def load_csv(path, indeces=[0]):

    df = pd.read_csv(path, index_col=indeces)

    return df


def get_other_external(df):

    return df[(df.EXEC_TYPE == "EXTERNAL") & (df.DESC == "OTHER")]