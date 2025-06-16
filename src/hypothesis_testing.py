import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, chi2_contingency

def calculate_kpis(df):
    df = df.copy()
    df['Claim'] = df['TotalClaims'] > 0
    df['ClaimFrequency'] = df.groupby('PolicyID')['Claim'].transform('mean')
    df['ClaimSeverity'] = np.where(df['TotalClaims'] > 0, df['TotalClaims'] / df['TotalPremium'], np.nan)
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    return df

def run_ttest(group1, group2, metric):
    """Run Welch's t-test for numerical comparison (unequal variances assumed)."""
    g1 = group1[metric].dropna()
    g2 = group2[metric].dropna()
    if len(g1) < 2 or len(g2) < 2:
        return None
    stat, p_value = ttest_ind(g1, g2, equal_var=False)
    return p_value

def run_chi_squared(df, group_col, outcome_col):
    """Run chi-squared test of independence for categorical variables."""
    contingency_table = pd.crosstab(df[group_col], df[outcome_col])
    if contingency_table.shape[0] < 2 or contingency_table.shape[1] < 2:
        return None
    chi2, p_value, _, _ = chi2_contingency(contingency_table)
    return p_value

def hypothesis_test_by_group(df, group_col, metric):
    """Perform pairwise t-tests across all group combinations."""
    results = {}
    groups = df[group_col].dropna().unique()
    if len(groups) < 2:
        return {"error": f"Not enough unique values in {group_col}"}
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            g1 = df[df[group_col] == groups[i]]
            g2 = df[df[group_col] == groups[j]]
            p_value = run_ttest(g1, g2, metric)
            if p_value is not None:
                results[f"{groups[i]} vs {groups[j]}"] = p_value
    return results

def interpret_result(p_value, alpha=0.05):
    if p_value is None:
        return "Insufficient data"
    return "Reject H₀" if p_value < alpha else "Fail to Reject H₀"
