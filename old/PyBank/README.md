Financial Analysis Script
This Python script performs financial analysis on budget data provided in a CSV file. It calculates various financial metrics, prints the results to the terminal, and exports the findings to a text file. The analysis includes metrics such as total months, net total, average change, greatest increase in profits, and greatest decrease in profits.
The prerequisites are:
- python 3.x
- csv file containing budget data
These steps have to be gone through:
- Clone the repository: git clone https://github.com/fikerdamene/financial-analysis-script.git
- Navigate the project directory
- Ensure the 'Resources' folder contains the budget data csv file
- Run the script
Output
The script will print the financial analysis results to the terminal and export them to a text file ('financial_analysis.txt') in the 'analysis' folder.
File Structure
- financial_analysis.py: The main Python script for financial analysis.
- Resources/budget_data.csv: The CSV file containing budget data.
- analysis/financial_analysis.txt: The exported text file with financial analysis results.
Results
The script calculates and provides the following financial metrics:
-Total Months
-Net Total
-Average Change
-Greatest Increase in Profits (Date and Amount)
-Greatest Decrease in Profits (Date and Amount)