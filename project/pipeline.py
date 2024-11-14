import os
import shutil
import pandas as pd
import sqlite3

def fetch_data(url):
    """
    Fetch CSV data from a URL and load it into a DataFrame.
    """
    return pd.read_csv(url)

def preprocess_data(df, selected_columns, drop_zero=None, rename_columns=None, fahrenheit_column=None, celsius_column=None, country_filter=None):
    """
    Preprocess the DataFrame with specified operations: column selection, renaming, filtering, and conversions.
    """
    df = df[selected_columns]  # Select specific columns
    
    if rename_columns:
        df = df.rename(columns=rename_columns)  # Rename columns

    if country_filter:
        df = df[df['country'] == country_filter]  # Filter by country

    df = df.dropna()  # Remove rows with null values

    if drop_zero:
        df = df[df[drop_zero] != 0.0]  # Drop rows with zero values in specified column

    if fahrenheit_column and celsius_column:
        df[celsius_column] = (df[fahrenheit_column] - 32) * 5.0 / 9.0
        df = df.drop(columns=[fahrenheit_column])  # Drop Fahrenheit column after conversion

    return df

def merge_data(df1, df2, join_columns):
    """
    Merge two DataFrames on specified columns.
    """
    return pd.merge(df1, df2, on=join_columns)

def save_to_sqlite(df, folder_path, sqlite_filename, table_name):
    """
    Save the DataFrame to an SQLite database.
    """
    os.makedirs(folder_path, exist_ok=True)  # Ensure the directory exists
    conn = sqlite3.connect(os.path.join(folder_path, sqlite_filename))
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

def main():
    # Dataset 1: CO2 and Greenhouse Gas Emissions for Brazil
    co2_url = "https://nyc3.digitaloceanspaces.com/owid-public/data/co2/owid-co2-data.csv"
    co2_selected_columns = ['country', 'year', 'co2']
    co2_df = fetch_data(co2_url)
    co2_df = preprocess_data(co2_df, co2_selected_columns, drop_zero='co2', country_filter='Brazil')

    # Dataset 2: Earth Surface Temperature Data for Brazil
    temperature_url = "https://figshare.com/ndownloader/files/4938964"
    temperature_selected_columns = ['year', 'AverageTemperatureFahr', 'Country']
    temperature_rename_columns = {'Country': 'country'}
    temperature_df = fetch_data(temperature_url)
    temperature_df = preprocess_data(
        temperature_df,
        temperature_selected_columns,
        rename_columns=temperature_rename_columns,
        fahrenheit_column='AverageTemperatureFahr',
        celsius_column='AverageTemperatureCelsius',
        country_filter='Brazil'
    )

    # Merge DataFrames on 'year' and 'country'
    joined_df = merge_data(co2_df, temperature_df, ['year', 'country'])

    # Save the merged DataFrame to an SQLite database
    folder_path = "../data"
    sqlite_filename = "brazil_climate_data.sqlite"
    save_to_sqlite(joined_df, folder_path, sqlite_filename, "brazil_climate_data")

if __name__ == "__main__":
    main()
