import pandas as pd

def compute_median_mean_diff(df):
    # Calculer la moyenne et la médiane
    mean = df.mean()
    median = df.median()
    
    # Calculer la différence entre la moyenne et la médiane
    diff = mean - median
    
    # Créer un DataFrame avec les résultats
    result_df = pd.DataFrame({'Mean': mean, 'Median': median, 'Difference': diff})
    
    return result_df

# Exemple d'utilisation
""" data = {'A': [1, 2, 3, 4, 5],
       'B': [2, 4, 6, 8, 10],
        'C': [3, 6, 9, 12, 15]}
df = pd.DataFrame(data)
result = compute_median_mean_diff(df)
print(result)
 """