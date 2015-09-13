__author__ = 'jubin'

import pprint
import pandas as pd
import jtk.com.string.comparer.algo as algo
import jtk.com.string.comparer.file_loader as file_loader
from sys import argv


if __name__ == "__main__":

    file_path = "../data.csv"

    df1 = file_loader.load_csv(file_path, False)

    df1 = file_loader.get_other_external(df1)

    products = pd.Series(df1.PRODUCT.values.tolist()).unique().tolist()

    algo.first_pass_high_score=70

    algo.first_pass_low_score = 60

    for product in products:
        print('\n')

        print('Analysing Product... ' + product )

        df_product = df1[df1.PRODUCT == product]

        algo.compare_choices(df_product.RAISER_COMMENTS)

        print('Categories on the higher similarity')

        print(pprint.pprint(algo.hi_category))

        print('Categories on the lower similarity')

        print(pprint.pprint(algo.low_category))

        print("Opening the file...")

        target = open(product+'.category.exception', 'w')

        target.write('\nCategories on the higher similarity \n')
        target.write('----------------------------------- \n')

        for key, elem in algo.hi_category.items():
            target.write('\nCategory ' + str(key) + '\n')
            target.write('------------- \n')
            [target.write(str(i) + '\n') for i in elem]

        target.write('\nCategories on the Lower similarity \n')
        target.write('---------------------------------- \n')

        for key, elem in algo.low_category.items():
            target.write('\nCategory ' + str(key) + '\n')
            target.write('------------- \n')
            [target.write(str(i) + '\n') for i in elem]

        target.close()