import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


def fetch_data():
    
    dataset = pd.read_csv('assets.csv')
    assets = dataset['Assets']

    data = yf.download(assets.to_list(), start="2019-01-01", end="2024-01-01")


    print(data.head(20))
    print("\n\n")
    print(data.tail(20))


def main():
    fetch_data()




if __name__ == "__main__":
    main()

