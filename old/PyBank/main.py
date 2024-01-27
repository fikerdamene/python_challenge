import os
import csv

# List files and directories in a given path

path = 'Resources/budget_data.csv'

# Getting the directory for script and checking if it exists

script_dir = os.path.dirname(os.path.abspath(__file__))

# Bring directories together and specify the relative path

budget_csv = os.path.join(script_dir, "Resources", "budget_data.csv")


# Introduce the analysis folder
                         
analysis_folder = os.path.join(script_dir, "analysis")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")      

    # Skip header
    next(csvreader)

    # Initialize variables to store results
    total_month = 0
    net_total = 0
    last_PnL = 0
    changes = []
    greatest_increase = {"date": "", "amount": float("-inf")}
    greatest_decrease = {"date": "", "amount": float("inf")}

    for row in csvreader:

        # Check if the row has at least two columns

        if len(row) >= 2:

            # Extract date and; profit and loss

            date = row[0]
            profit_loss = int(row[1])

            # Calculate total number of months and profit/loss
            
            total_month += 1
            net_total += profit_loss

            # Calculate change
        
            change = profit_loss - last_PnL

            # Calculate change in profit/loss and store

            if total_month > 1:
                changes.append(change)

                # Update greatest increase and decrease
                if change > greatest_increase["amount"]:
                    greatest_increase["date"] = date
                    greatest_increase["amount"] = change

                if change < greatest_decrease["amount"]:
                    greatest_decrease["date"] = date
                    greatest_decrease["amount"] = change

            # Update last profit and loss
            last_PnL = profit_loss

    # Calculate average
    average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

    # # Print result to terminal
    print(f"Financial Analysis",f"--------------------------------", \
          f"Total Months: {total_month}",f"Net Total: ${net_total}",\
          f"Average Change: ${average_change:.2f}",\
          f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})",\
          f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})",sep="\n")

    # Export result to a text file in the 'analysis' folder
    output_path = os.path.join(analysis_folder, "financial_analysis.txt")
    with open(output_path, "w") as output_file:
        output_file.write(f"Financial Analysis\n"f"----------------------------------------\n"\
                          f"Total Months: {total_month}\n"f"Net Total: ${net_total}\n"\
                          f"Average Change: ${average_change:.2f}\n"\
                          f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"\
                          f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")
        

    


    
