import unittest
from unittest.mock import patch
import os
import pandas as pd
import sqlite3
from pipeline import fetch_data, preprocess_data, merge_data, save_to_sqlite, main

class TestPipeline(unittest.TestCase):

    def setUp(self):
        # Mock data for CO2
        self.co2_data = pd.DataFrame({
            'country': ['Brazil', 'USA', 'Brazil'],
            'year': [2000, 2001, 2002],
            'co2': [10.5, 20.0, 0.0]
        })

        # Mock data for temperature
        self.temperature_data = pd.DataFrame({
            'year': [2000, 2001, 2002],
            'AverageTemperatureFahr': [86.0, 77.0, 95.0],
            'country': ['Brazil', 'Brazil', 'USA']
        })

        # Output file path setup
        self.folder_path = './test_output'
        self.sqlite_filename = 'test_brazil_climate_data.sqlite'
        self.output_file_path = os.path.join(self.folder_path, self.sqlite_filename)

    def tearDown(self):
        # Clean up generated output file after each test
        if os.path.exists(self.folder_path):
            for root, _, files in os.walk(self.folder_path):
                for file in files:
                    os.remove(os.path.join(root, file))
            os.rmdir(self.folder_path)

    @patch('pandas.read_csv')
    def test_fetch_data(self, mock_read_csv):
        # Test data fetching from a mocked URL
        mock_read_csv.return_value = self.co2_data
        data = fetch_data('mock_url')
        self.assertTrue(data.equals(self.co2_data), "Fetched data does not match expected mock data.")

    def test_preprocess_data(self):
        # Test data preprocessing, including filtering and column selection
        selected_columns = ['country', 'year', 'co2']
        processed_data = preprocess_data(
            self.co2_data,
            selected_columns=selected_columns,
            drop_zero='co2',
            country_filter='Brazil'
        )
        expected_data = self.co2_data[self.co2_data['country'] == 'Brazil']
        expected_data = expected_data[expected_data['co2'] != 0.0]
        self.assertTrue(processed_data.equals(expected_data), "Preprocessed data does not match expected result.")

    def test_merge_data(self):
        # Test merging of CO2 and temperature data
        co2_df = self.co2_data[self.co2_data['country'] == 'Brazil']
        co2_df = co2_df[co2_df['co2'] != 0.0]

        temperature_df = self.temperature_data[self.temperature_data['country'] == 'Brazil']
        merged_data = merge_data(co2_df, temperature_df, ['year', 'country'])
        
        self.assertIn('co2', merged_data.columns, "Merged data is missing CO2 column.")
        self.assertIn('AverageTemperatureFahr', merged_data.columns, "Merged data is missing temperature column.")
        self.assertEqual(len(merged_data), 1, "Merged data row count does not match expected result.")

    def test_save_to_sqlite(self):
        # Test saving data to an SQLite database
        mock_data = pd.DataFrame({'year': [2000], 'country': ['Brazil'], 'co2': [10.5], 'AverageTemperatureCelsius': [30.0]})
        save_to_sqlite(mock_data, self.folder_path, self.sqlite_filename, "test_table")
        conn = sqlite3.connect(os.path.join(self.folder_path, self.sqlite_filename))
        saved_data = pd.read_sql_query("SELECT * FROM test_table", conn)
        conn.close()
        self.assertTrue(saved_data.equals(mock_data), "Saved data does not match input data.")

    # System-test level 
    def test_pipeline_execution(self):
        # Ensure the output folder exists before running the pipeline
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        # Run the pipeline
        with patch('pipeline.save_to_sqlite') as mock_save:
            # Mock the save_to_sqlite method to redirect the output to the test folder
            def mock_save_to_sqlite(data, folder, filename, table_name):
                save_to_sqlite(data, self.folder_path, self.sqlite_filename, table_name)

            mock_save.side_effect = mock_save_to_sqlite
            main()

        # Check if the output SQLite file is created
        self.assertTrue(
            os.path.isfile(self.output_file_path),
            f"Pipeline did not generate the output SQLite file at {self.output_file_path}."
        )

        # Validate the contents of the SQLite database
        conn = sqlite3.connect(self.output_file_path)
        cursor = conn.cursor()
        # Check if the table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='brazil_climate_data';")
        table_exists = cursor.fetchone()
        self.assertIsNotNone(table_exists, "Table 'brazil_climate_data' was not found in the SQLite database.")

        # Check the contents of the table
        result = pd.read_sql_query("SELECT * FROM brazil_climate_data", conn)
        conn.close()

        # Ensure data was inserted into the table
        self.assertGreater(len(result), 0, "No data found in the 'brazil_climate_data' table.")


if __name__ == "__main__":
    unittest.main()
