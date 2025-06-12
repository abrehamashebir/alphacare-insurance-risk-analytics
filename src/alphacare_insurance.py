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
        print
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
        
def check_duplicates(df):
    """
    Check for duplicate entries in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): DataFrame to check for duplicates.
    
    Returns:
    int: Number of duplicate rows.
    """
    if df is None:
        return 0
    
    duplicates = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates}")
    df = df.drop_duplicates(inplace=True)
    print("Duplicates removed.")
    # Optionally, return the number of duplicates
    
    return duplicates

def check_null_values(df):
    """
    Check for null values in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): DataFrame to check for null values.
    
    Returns:
    pd.Series: Series containing the count of null values for each column.
    """
    if df is None:
        return pd.Series()
    
    null_counts = df.isnull().sum()
    null_percentage = (null_counts / len(df)) * 100
    print("Null values in each column (with percentage):")
    print(null_counts[null_counts > 0])
    print(null_percentage[null_percentage > 0])
    print("\n =================================================")
    print("Total null values in the DataFrame:", null_counts.sum())
    print("\n =================================================")
    print("Percentage of null values in each column:")
    print(null_percentage[null_percentage > 0])
    print("\n =================================================")
    print("Total null values in the DataFrame:", null_counts.sum())
    print("\n =================================================")
    print("Total percentage of null values in the DataFrame:", null_percentage.sum())
    print("\n =================================================")   
    print("Null values in each column:")
    print(null_counts[null_counts > 0])
    print("\n =================================================")

def handling_null_values(df):
    """
    Handle null values in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): DataFrame to handle null values.
    
    Returns:
    pd.DataFrame: DataFrame with null values handled.
    """
    if df is None:
        return df
    
    # Fill numeric columns with mean
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    # Fill categorical columns with mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if not df[col].mode().empty:
            # Fill with mode only if mode exists
            if df[col].mode()[0] is not None:   
              df[col] = df[col].fillna(df[col].mode()[0])
    
    print("Null values handled.")
    
    return df