__author__ = 'jubin'

from fuzzywuzzy import process

import re

first_pass_high_score = 0

first_pass_low_score = 0

hi_category = {}

low_category = {}

category_id = 1

low_category_id=1

def compare_choices(choices=[]):

    global category_id

    global low_category_id

    hi_category.clear()

    category_id = 1

    low_category.clear()

    low_category_id = 1

    for idx, val in enumerate(choices):

        query = val

        query = re.sub("[^a-z A-Z]", "", val)  # keep only alphabets and spaces

        subset = [re.sub("[^a-z A-Z]", "", x) for x in choices if x != val]

        best_match = process.extract(query, subset, limit=len(subset))

        hi_match = get_first_pass_high_score(best_match)

        if len(hi_match) > 0:

            hi_match.append(query)

            #print('hi')

            #print(hi_match)

            form_category(hi_match)

        else:

            low_match = get_first_pass_low_score(best_match)

            low_match.append(query)

            #print('low')

            #print(low_match)

            form_low_category(low_match)


def form_category(l=[]):

    global category_id

    found_category = False

    if len(l) == 0:
        return

    for key, item in hi_category.items():
        if item.intersection(l):
            hi_category[key].update(l)
            found_category = True

    if not found_category:
        hi_category[category_id] = set(l)
        category_id = category_id + 1

def form_low_category(l=[]):

    global low_category_id

    found_category = False

    if len(l) == 0:
        return

    for key, item in low_category.items():
        if item.intersection(l):
            low_category[key].update(l)
            found_category = True

    if not found_category:
        low_category[low_category_id] = set(l)
        low_category_id = low_category_id + 1



def get_first_pass_high_score(vals=[]):
    return [v[0] for i, v in enumerate(vals) if v[1] >= first_pass_high_score]


def get_first_pass_low_score(vals=[]):
    return [v[0] for i, v in enumerate(vals) if v[1] < first_pass_high_score and v[1] >= first_pass_low_score]


def get_bottom_score(vals=[]):
    return [v[0] for i, v in enumerate(vals) if v[1] < first_pass_low_score]

