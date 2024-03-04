import matplotlib.pyplot as plt
import pandas as pd

def generate_report(file_path: str):
    df = pd.read_csv(file_path)
    print(df.head())
    return