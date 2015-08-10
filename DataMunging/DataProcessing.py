import pandas as pd


def sum_of_digits(str_value):
    """
    Sum up all the digits in a number till it is single digit
    Eg:
          1 => 1
         11 => 2
        123 => 6
       1235 => 2
         98 => 8
    """
    total = 0
    for num in str_value:
        total += int(num)
    if total > 9:
        return sum_of_digits(str(total))
    return total

    
def do_processing(file_name):
    # Read an excel file. Make sure it is in in XLSX format and
    # you have XlsxWriter package installed.
    # Pandas uses this package to read excel files.
    df = pd.read_excel(file_name)
    # Split the name into first name and last name
    # You will get a pandas Series which has 1 column with a list in each row
    fn_ln_list = df['Name'].str.split(' ')
    # Use list comprehension to build a list for the first name and last name
    df['first_name'] = [name[0] for name in fn_ln_list]
    df['last_name'] = [name[1] for name in fn_ln_list]

    # Pandas DataFrame automatically recognizes the date field and converts
    # it into a datetime object. Using strftime to convert the datetime object
    # to a string in the format DDMMYYYY
    df['dob'] = df['Date Of Birth'].apply(lambda x: x.strftime('%d%m%Y'))
    # Sum the numbers in DOB to a single digit
    # Create a new field to save the sum of digits
    df['sum_dob'] = df['dob'].apply(sum_of_digits)
    print "\n\n\nDataFrame:\n"
    print "----------\n", df
    print "\n\n\nDataFrame Columns:\n"
    print "------------------\n", df.columns
    print "\n\n\nDataFrame Data Types:\n"
    print "---------------------\n", df.dtypes


if __name__ == '__main__':
    file_name = 'person_details.xlsx'
    do_processing(file_name)