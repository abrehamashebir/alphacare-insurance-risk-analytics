import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from src.alphacare_insurance import handling_null_values
def preprocess_data(df, target_column, categorical_cols, numerical_cols):
    # Handle missing values
    df = handling_null_values(df, numerical_cols)

    # Encode categorical features
    df = encode_features(df, categorical_cols)

    # Ensure target column is present
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in DataFrame.")

    return df

def encode_features(df, categorical_cols):
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoded = encoder.fit_transform(df[categorical_cols])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_cols))
    
    df = df.drop(columns=categorical_cols)
    df = pd.concat([df.reset_index(drop=True), encoded_df], axis=1)
    return df

def split_data(df, target_column, claim_only=False):
    if claim_only:
        df = df[df['TotalClaims'] > 0]

    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=0.2, random_state=42)
