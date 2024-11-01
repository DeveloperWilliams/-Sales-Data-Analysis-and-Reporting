# Sales Data Analysis Pipeline

## Overview
This project processes raw sales data to produce insights into sales trends and performance. The pipeline cleans, analyzes, and visualizes data, and generates reports for further business insights.

## Features
- **Data Cleaning**: Removes nulls and duplicates for accuracy.
- **Analysis**: Calculates sales metrics (e.g., revenue, growth).
- **Visualization**: Graphs for trend analysis.
- **Reporting**: Generates summary CSV or PDF files.

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run `python main.py --input sales_data.csv --output report.pdf`
3. Find results in the `output` folder.

## Technologies Used
- `pandas` for data processing
- `matplotlib` for visualizations
- `SQLAlchemy` for optional database storage
