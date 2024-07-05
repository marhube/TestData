#******** Start type hinting
#******** Slutt type hinting

import os
import sys # For testing
import pandas as pd
import numpy as np
from importlib.metadata import version, PackageNotFoundError




def create_float_column(n: int, with_na: bool) -> np.ndarray:
    """Creates a float column with optional missing values."""
    rng = np.random.default_rng()
    col = rng.uniform(0, 100, n)
    if with_na:
        col[::2] = np.nan
    return col

def create_nan_column(n: int) -> np.ndarray:
    """Creates a float column with optional missing values."""
    col = np.asarray([np.nan for iter in range(n) ] )
    return col


def create_int_column(n: int, with_na: bool) -> pd.Series:
    """Creates an integer column with optional missing values."""
    col:pd.core.series.Series = pd.Series(np.random.randint(0, 100, n), dtype="Int64")
    if with_na:
        col[::3] = pd.NA
    return col

def create_na_column(n:int) -> pd.Series:
    col = pd.Series([pd.NA for iter in range(n)], dtype="Int64")
    return col

def create_datetime_column(n: int, with_na: bool) -> pd.Series:
    """Creates a datetime column with optional missing values."""
    col = pd.Series(pd.date_range(start='2023-01-01', periods=n, freq='h'),dtype='datetime64[us]')
    if with_na:
        col[::4] = pd.NaT
    return col

def create_nat_column(n:int) -> pd.Series:
    
    col = pd.Series([pd.NaT for iter in range(n)],dtype = 'datetime64[us]')
    return col

def create_none_column(n:int) -> pd.Series:
    col = pd.Series([None for iter in range(n)])
    return col


def create_date_column(n: int, with_na: bool) -> pd.Series:
    """Creates a date-only column with optional missing values."""
    col = pd.Series(pd.date_range(start='2023-01-01', periods=n, freq='D').date)
    if with_na:
        col[::4] = pd.NaT
    return col

#Memo to self: Must explicitly declare type for "col" for "mypy" to accept
# the output type of "create_string_columns"
def create_string_column(n: int, with_na: bool) -> list[str | None]:
    """Creates a string column with optional missing values."""    
    col: list[str | None] = [f'str{i}' for i in range(n)]
    if with_na:
        col = [s if i % 2 != 0 else None for i, s in enumerate(col)]
    return col


    


def generate_test_data(n: int,include_all_missing: bool = False,include_str_date: bool = False) -> pd.DataFrame:
    """Generates a test DataFrame with specified data types and missing values."""
    test_data_dict =  {
        'float_with_na': create_float_column(n, True),
        'float_no_na': create_float_column(n, False),
        'int_with_na': create_int_column(n, True),
        'int_no_na': create_int_column(n, False),
        'datetime_with_na': create_datetime_column(n, True),
        'datetime_no_na': create_datetime_column(n, False),
        'date_with_na': create_date_column(n, True),
        'date_no_na': create_date_column(n, False),
        'str_with_na': create_string_column(n, True),
        'str_no_na': create_string_column(n, False)
    }
    
    if include_all_missing:
        test_data_dict['float_only_na'] = create_nan_column(n)
        test_data_dict['int_only_na'] = create_na_column(n)
        test_data_dict['datetime_only_na'] = create_nat_column(n)
        test_data_dict['date_only_na'] = create_nat_column(n)
        test_data_dict['str_only_na'] = create_none_column(n)
    #
    test_data = pd.DataFrame(test_data_dict) 
 
    
    if include_str_date:
        test_data['str_datetime_with_na'] = test_data['datetime_with_na'].map(
            lambda x: str(x) if not pd.isna(x) else None)
        test_data['str_date_with_na'] = test_data['date_with_na'].map(
            lambda x: str(x) if not pd.isna(x) else None)
        
    
       
    return test_data


