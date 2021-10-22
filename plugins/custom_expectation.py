import great_expectations as ge
from datetime import datetime, timezone
from datetime import date
import pandas as pd
import numpy as np

from great_expectations.dataset import (
    PandasDataset,
    MetaPandasDataset,
)

class MyCustomPandasDataset(PandasDataset):

    _data_asset_type = "MyCustomPandasDataset"

    @MetaPandasDataset.column_map_expectation
    def expect_column_values_to_calculate_age(self,column,min_age=None,date_format=None):

        column_aux = pd.to_datetime(column,format=date_format)
        now = pd.Timestamp('now')
        column_aux = column_aux.where(column_aux < now, column_aux - np.timedelta64(100, 'Y')) 
        column_aux = (now - column_aux).astype('<m8[Y]') 

        column_aux = column_aux > min_age
    
        return column_aux