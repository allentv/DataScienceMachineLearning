# -*- coding: utf-8 -*-
"""
This module generates test data in .CSV format for the Case Study.
The data generated uses a random number generator to generate values and so the
output would be different between runs.


@author: Allen Thomas Varghese
@date: Mon Mar 28 07:57:59 2016
"""
import csv
import random
import numpy
import datetime


# Define the list of products to be used in the test data file
PRODUCT_LIST = ['Product1', 'Product2', 'Product3', 'Product4', 'Product5']


# Set the seed for the random number generator to generate same results in
# every run. The seed can be any arbitary integer.
# Uncomment the below lines during testing/development
# RANDOM_NUMBER_SEED = 1000
# random.seed(RANDOM_NUMBER_SEED)
# np.random.seed(RANDOM_NUMBER_SEED)


def some_random_number():
    return random.randint(0, 1000)


def get_user_ids():
    """
    Use a choice distribution to generate a list of random unique values
    i.e. without replacement of values
    """
    TOTAL_USERS = 50
    return list(numpy.random.choice(
        TOTAL_USERS, random.randint(1, TOTAL_USERS), replace=False
    ))


def get_value_list():
    """
    Returns a list of values filled with random numbers.
    The number of elements changes each time the function is called
    """
    return [some_random_number() for _ in range(some_random_number())]


def generate_test_data():
    """
    Create the test data file having the following information:
    Row_ID: Unique ID for each row in the file
    User_ID: A pre-defined set of user IDs
    Product: The name of the product
    Entry_Date: Date at which the data was entered
    """
    print("Test data generation started...")
    processing_start_time = datetime.datetime.now()
    
    SURVEY_DURATION = 90   # In days    
    today_date = datetime.datetime.today()
    start_date = today_date - datetime.timedelta(days=SURVEY_DURATION)

    with open('product_test_data.csv', 'w') as test_file:
        file_writer = csv.writer(test_file, quoting=csv.QUOTE_ALL)
        
        # Write the file header
        file_writer.writerow([
            "Row_ID", "User_ID", "Product", "Amount", "Entry_Date"
        ])
        
        row_id = 1   # A Row ID to keep track of how many records were created
        for day in range(SURVEY_DURATION):   # Data for each day of the survey
            # Extract the date portion        
            data_entry_date = str(
                start_date + datetime.timedelta(days=day)
            ).split()[0]
            for user_id in get_user_ids():   # The user IDs change for each day
                for product in PRODUCT_LIST:
                    file_writer.writerow([
                        row_id,
                        user_id,
                        product,
                        get_value_list(),
                        data_entry_date
                    ])
                    row_id += 1

        processing_end_time = datetime.datetime.now()
        print("Test data file generated in %s min %s seconds with %s records" % (
            (processing_end_time - processing_start_time).seconds / 60,
            (processing_end_time - processing_start_time).seconds,
            row_id
        ))


if __name__ == '__main__':
    generate_test_data()