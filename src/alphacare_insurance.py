import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_insurance_data(file_path):
    """
    Load insurance data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file containing insurance data.
    
    Returns:
    pd.DataFrame: DataFrame containing the loaded insurance data.
    """
    try:
        data = pd.read_csv(file_path, delimiter='|')
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
def insurance_statistics(df):
        """
        Calculate basic statistics for insurance data.
        Parameters:
        data (pd.DataFrame): DataFrame containing insurance data.
        Returns:
        dict: Dictionary containing basic statistics.
        """
        if df is None:
            return {}
        
        stat = df.describe()
        print("Insurance Data Statistics:")
        print(stat)
        print("\n =================================================")
        print("\nMissing Values:")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])
        print("\n =================================================")
        info = df.info()
        print("\nData Information:")
        print(info)
        print("\n =================================================")
        # Display data types
        data_types = df.dtypes
        print("\nData Types:")
        print(data_types)
        print("\n =================================================")
        