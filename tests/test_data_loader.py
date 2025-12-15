import pytest
import pandas as pd
from src.data_loader import load_csv

def test_load_csv():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df.to_csv('test.csv', index=False)
    result = load_csv('test.csv')
    assert len(result) == 2