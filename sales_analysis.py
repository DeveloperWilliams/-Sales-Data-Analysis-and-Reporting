# sales_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

class SalesDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        print("Data loaded successfully.")

    def clean_data(self):
        self.data.dropna(inplace=True)
        self.data.drop_duplicates(inplace=True)
        print("Data cleaned.")

    def analyze_sales(self):
        self.monthly_sales = self.data.groupby('month')['sales'].sum()
        print("Sales analysis complete.")

    def visualize_sales(self):
        plt.plot(self.monthly_sales)
        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Sales")
        plt.show()

    def save_report(self, output_path):
        self.monthly_sales.to_csv(output_path)
        print(f"Report saved to {output_path}")

# Example usage
if __name__ == "__main__":
    processor = SalesDataProcessor('sales_data.csv')
    processor.load_data()
    processor.clean_data()
    processor.analyze_sales()
    processor.visualize_sales()
    processor.save_report('monthly_sales_report.csv')
