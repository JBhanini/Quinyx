import pandas as pd

excel = 'sales data 2019 1-3.xlsx'


def process_data(excel_file):
    df = pd.read_excel(excel)
    df.dropna()
    df.rename(columns = {'Transaction Time':'Time', 'Unit Qty':'Unit', 'Total Trans Value':'Value'}, inplace=True)
    df.sort_values(by=['Time'], inplace=True)
    df["Stamp"] = df['Date'].astype(str) +" "+ df["Time"].astype(str)
    df['Stamp'] = pd.to_datetime(df['Stamp'])
    df.set_index("Stamp", inplace=True)
    df_grouped = df.resample("15min").sum()
    df_grouped.to_csv('output.csv')
    return "Done processing ---- Created csv"


process_data(excel)