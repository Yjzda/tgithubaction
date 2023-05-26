import pytest
import pandas as pd
from pipeline_data import compute_median_mean_diff

def test_compute_median_mean_diff():
    # Générer les données pour le test
    data = {'0': [1, 2, 3, 4, 5],
            '1': [2, 4, 6, 8, 10],
            '2': [3, 6, 9, 12, 15]}
    df = pd.DataFrame(data)
    
    # Appeler la fonction à tester
    result_df = compute_median_mean_diff(df)
    
    # Vérifier les résultats attendus
    expected_result = pd.DataFrame({
        'Mean': [3.0, 6.0, 9.0],
        'Median': [3.0, 6.0, 9.0],
        'Difference': [0.0, 0.0, 0.0]
    })
    print("result_df:")
    print(result_df)
    print("expected_result:")
    print(expected_result)
    result_df.reset_index(drop=True, inplace=True)
    expected_result.reset_index(drop=True, inplace=True)
    
    assert result_df.equals(expected_result)

# Exécuter les tests avec pytest
if __name__ == '__main__':
    pytest.main()
