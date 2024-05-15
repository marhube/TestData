import os
import sys
#Forsøk på  systematisk testing
import unittest
import pandas as pd
import numpy as np
from TestData import TestData
from math import ceil
from datetime import  date
#

class TestTestData(unittest.TestCase):
    #Memo to self: Testing every function with input both with and without na
    def test_create_float_column(self):
        print('Er nå inne i TestTestData(.test_create_float_column')
        test_n = 5        
        float_col_with_na = TestData.create_float_column(n=test_n,with_na=True)
        float_col_without_na = TestData.create_float_column(n=test_n,with_na=False)
        float_col_no_rows = TestData.create_float_column(n=0,with_na=True)
        element_class_check = [
            isinstance(float_col_with_na[ind],float) and 
                isinstance(float_col_without_na[ind],float) 
                    for ind in range(len(float_col_with_na))
                ]
        #
        
        subresults = [
            isinstance(float_col_with_na, np.ndarray),
            isinstance(float_col_without_na, np.ndarray),
            isinstance(float_col_no_rows, np.ndarray),
            len(float_col_with_na) == test_n,
            len(float_col_no_rows) == 0,                      
            sum(np.isnan(float_col_with_na)) == ceil(len(float_col_with_na)/2),
            sum(np.isnan(float_col_without_na)) == 0,
            pd.Series(element_class_check).all()
        ] 
        # Check if every "sub-test" is passed 
        self.assertTrue(pd.Series(subresults).all()) 
    
    def test_create_int_column(self):
        print('Er nå inne i TestTestData.test_create_int_column')
        test_n = 5        
        int_col_with_na = TestData.create_int_column(n=test_n,with_na=True)
        int_col_without_na = TestData.create_int_column(n=test_n,with_na=False)
        int_col_no_rows = TestData.create_int_column(n=0,with_na=True)
        element_class_check = [
            (pd.isna(int_col_with_na[ind]) or isinstance(int_col_with_na[ind],np.int64)) and 
                isinstance(int_col_without_na[ind],np.int64) 
                    for ind in range(len(int_col_with_na))
                ]
        #
        print(f'element_class_check  er {element_class_check }.')
        
        
        subresults = [
            isinstance(int_col_with_na, pd.Series),
            isinstance(int_col_without_na, pd.Series),
            isinstance(int_col_no_rows, pd.Series),
            len(int_col_with_na) == test_n,
            len(int_col_no_rows) == 0,                      
            sum(pd.isna(int_col_with_na)) == ceil(len(int_col_with_na)/3),
            sum(pd.isna(int_col_without_na)) == 0,
            pd.Series(element_class_check).all()
            ]   
        # Check if every "sub-test" is passed 
        self.assertTrue(pd.Series(subresults).all()) 
        
   
    def test_create_datetime_column(self):
        print('Er nå inne i TestTestData.test_create_datetime_column')
        test_n = 5        
        datetime_col_with_na = TestData.create_datetime_column(n=test_n,with_na=True)
        datetime_col_without_na = TestData.create_datetime_column(n=test_n,with_na=False)
        datetime_col_no_rows = TestData.create_datetime_column(n=0,with_na=True)
        element_class_check = [
            (pd.isna(datetime_col_with_na[ind]) or 
             isinstance(datetime_col_with_na[ind],pd._libs.tslibs.timestamps.Timestamp)) and 
                isinstance(datetime_col_without_na[ind],pd._libs.tslibs.timestamps.Timestamp) 
                    for ind in range(len(datetime_col_with_na))
                ]       
               
        subresults = [
            isinstance(datetime_col_with_na, pd.Series),
            isinstance(datetime_col_without_na, pd.Series),
            isinstance(datetime_col_no_rows, pd.Series),
            len(datetime_col_with_na) == test_n,
            len(datetime_col_no_rows) == 0,                      
            sum(pd.isna(datetime_col_with_na)) == ceil(len(datetime_col_with_na)/3),
            sum(pd.isna(datetime_col_without_na)) == 0,
            pd.Series(element_class_check).all() 
            ]   
        # Check if every "sub-test" is passed 
        self.assertTrue(pd.Series(subresults).all()) 
        
    
    def test_create_date_column(self):
        print('Er nå inne i TestTestData.TestTestDatatest_create_date_column')
        test_n = 5        
        date_col_with_na = TestData.create_date_column(n=test_n,with_na=True)
        date_col_without_na = TestData.create_date_column(n=test_n,with_na=False)
        date_col_no_rows = TestData.create_date_column(n=0,with_na=True)
        element_class_check = [
            (pd.isna(date_col_with_na[ind]) or 
             isinstance(date_col_with_na[ind],date)) and 
                isinstance(date_col_without_na[ind],date) 
                    for ind in range(len(date_col_with_na))
                ]       
               
        subresults = [
            isinstance(date_col_with_na, pd.Series),
            isinstance(date_col_without_na, pd.Series),
            isinstance(date_col_no_rows, pd.Series),
            len(date_col_with_na) == test_n,
            len(date_col_no_rows) == 0,                      
            sum(pd.isna(date_col_with_na)) == ceil(len(date_col_with_na)/4),
            sum(pd.isna(date_col_without_na)) == 0,
            pd.Series(element_class_check).all() 
            ]   
        # Check if every "sub-test" is passed 
        self.assertTrue(pd.Series(subresults).all())   
    
    
    def test_create_nan_column(self):
        print('Er nå inne i TestTestData.test_create_nan_column')
        test_n = 5        
        nan_col = TestData.create_nan_column(n=test_n)
        nan_col_no_rows = TestData.create_nan_column(n=0)
        element_class_check = [
            pd.isna(nan_col[ind]) and 
                isinstance(nan_col[ind],float) 
                    for ind in range(len(nan_col))
                ]
        #
        print(f'element_class_check  er {element_class_check }.')
        
        
        subresults = [
            isinstance(nan_col, np.ndarray),
            isinstance(nan_col_no_rows, np.ndarray),
            len(nan_col) == test_n,
            len(nan_col_no_rows) == 0,                      
            sum(np.isnan(nan_col)) == len(nan_col),                
            pd.Series(element_class_check).all()
            ]   
        # Check if every "sub-test" is passed 
        self.assertTrue(pd.Series(subresults).all()) 

    def test_create_na_column(self):
        print('Er nå inne i TestTestData.test_create_na_column')
        test_n = 5        
        na_col = TestData.create_na_column(n=test_n)
        na_col_no_rows = TestData.create_na_column(n=0)
        element_class_check = [
            pd.isna(na_col[ind]) and isinstance(na_col[ind],pd._libs.missing.NAType) 
            for ind in range(len(na_col))
                ]    
        #
        print(f'element_class_check  er {element_class_check }.')
        
        
        subresults = [
            isinstance(na_col, pd.Series),
            isinstance(na_col_no_rows, pd.Series),
            len(na_col) == test_n,
            len(na_col_no_rows) == 0,                      
            sum(pd.isna(na_col)) == len(na_col),
            pd.Series(element_class_check).all()
            ]   
        # Check if every "sub-test" is passed 
        self.assertTrue(pd.Series(subresults).all()) 
  
    def test_create_nat_column(self):
        print('Er nå inne i TestTestData.test_create_nat_column')
        test_n = 5
        nat_col = TestData.create_nat_column(n=test_n)
        nat_col_no_rows = TestData.create_nat_column(n=0)
        element_class_check = [
            pd.isna(nat_col[ind]) and isinstance(nat_col[ind],pd._libs.tslibs.nattype.NaTType) 
            for ind in range(len(nat_col))
            ]
        #          
             
        print(f'element_class_check  er {element_class_check }.')
        
        subresults = [
            isinstance(nat_col, pd.Series),
            isinstance(nat_col_no_rows, pd.Series),
            len(nat_col) == test_n,
            len(nat_col_no_rows) == 0,                      
            sum(pd.isna(nat_col)) == len(nat_col),
            pd.Series(element_class_check).all() 
            ]   
        
        # Check if every "sub-test" is passed 
        self.assertTrue(pd.Series(subresults).all()) 

    def test_create_none_column(self):
        print('Er nå inne i TestTestData.test_create_none_column')
        test_n = 5
        none_col = TestData.create_none_column(n=test_n)
        none_col_no_rows = TestData.create_none_column(n=0)
        element_class_check = [none_col[ind] is None for ind in range(len(none_col))]
        #          
             
        print(f'element_class_check  er {element_class_check }.')
        
        subresults = [
            isinstance(none_col, pd.Series),
            isinstance(none_col_no_rows, pd.Series),
            len(none_col) == test_n,
            len(none_col_no_rows) == 0,                      
            sum(pd.isna(none_col)) == len(none_col),
            pd.Series(element_class_check).all() 
            ]   
        
        # Check if every "sub-test" is passed 
        self.assertTrue(pd.Series(subresults).all())


    def test_generate_test_data(self):
        print('Er nå inne i TestTestData.test_generate_test_data')
        test_n = 5
        test_data = TestData.generate_test_data(n = test_n,include_all_missing = True,include_str_date = True)
        subresults = [
            isinstance(test_data, pd.DataFrame),
            test_data.shape[0] == test_n
        ]

        self.assertTrue(pd.Series(subresults).all())


if __name__ == '__main__':
    unittest.main()
