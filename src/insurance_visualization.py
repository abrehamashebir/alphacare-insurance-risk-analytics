
import matplotlib.pyplot as plt
import seaborn as sns
def univariate_visualization(df, column):
    """
    Create a univariate visualization for a given column in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column (str): The column to visualize.
    
    Returns:
    None
    """
   
    
    plt.figure(figsize=(10, 6))
    
    if df[column].dtypes == 'object':
        sns.countplot(data=df, x=column)
        plt.xticks(rotation=45)
    else:
        sns.histplot(df[column], kde=True)
    
    plt.title(f'Univariate Visualization of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def bivariate_visualization(df, column1, column2):
    """
    Create a bivariate visualization for two columns in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column1 (str): The first column to visualize.
    column2 (str): The second column to visualize.
    
    Returns:
    None
    """
    
    plt.figure(figsize=(10, 6))
    
    if df[column1].dtypes == 'object' or df[column2].dtype == 'object':
        sns.countplot(data=df, x=column1, hue=column2)
        plt.xticks(rotation=45)
    else:
        sns.scatterplot(data=df, x=column1, y=column2)
    
    plt.title(f'Bivariate Visualization of {column1} and {column2}')
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()

