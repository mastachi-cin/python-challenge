import os
import csv

# Lists
date_ls = []
pl_ls = []
change_pl_ls = []
date_pl_ls = []

total_months = 0
net_total = 0

# Function to calculate average for changes
def calculate_average(numbers_ls):

    sum_total = 0.0
    # Sum up all the elements in the list
    for i in range(len(numbers_ls)):
        sum_total += numbers_ls[i]

    # Total sum divided by total elements
    return sum_total / len(numbers_ls)
    
# Function to export results to a text file
def export_results_to_text_file():
    # Set file path
    file_path = os.path.join("Analysis", "financial_analysis.txt")

    # Write text file
    text_file = open(file_path,"w")

    # Write the header row
    text_file.write("Financial Analysis \n")
    text_file.write("______________________________ \n \n")

    # Write Total Months
    text_file.write(f'Total Months: {total_months} \n')

    # Write Total
    text_file.write(f'Total: {net_total} \n')

    # Write Average change
    text_file.write(f'Average Change: ${average_change} \n')

    # Write Greatest increase in profits
    text_file.write(f'Greatest Increase in Profits: {date_greatest_inc} (${greatest_inc}) \n')

    # Write Greatest decrease in profits
    text_file.write(f'Greatest Decrease in Profits: {date_greatest_dec} (${greatest_dec}) \n')

    # Close file
    text_file.close()
    return
    
# Function to print results to terminal
def print_results_to_terminal():

    # Print the header row
    print("Financial Analysis")
    print("______________________________ \n")

    # Print Total Months
    print(f'Total Months: {total_months}')

    # Print Total
    print(f'Total: {net_total}')

    # Print Average change
    print(f'Average Change: ${average_change}')

    # Print Greatest increase in profits
    print(f'Greatest Increase in Profits: {date_greatest_inc} (${greatest_inc})')

    # Print Greatest decrease in profits
    print(f'Greatest Decrease in Profits: {date_greatest_dec} (${greatest_dec})')

    return
    
# Main
# File path
file_path = os.path.join("Resources", "budget_data.csv")

# Open budget_csv as csvfile:
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Save and skip header
    csv_header = next(csvreader)

    for row in csvreader:
        # Total number of months
        total_months += 1

        # Net total amount of Profit/Losses
        net_total += int(row[1])

        # Dates list
        date_ls.append(row[0])

        # Profit/losses list
        pl_ls.append(int(row[1]))


# Changes in Profit/Losses
for i in range(len(pl_ls)-1):
    change_pl_ls.append(pl_ls[i + 1] - pl_ls[i])
    date_pl_ls.append(date_ls[i + 1])

#Average change
average_change = round(calculate_average(change_pl_ls),2)

# Gratest increase/decrease in profits
greatest_dec = 0
greatest_inc = 0
for i in range(len(change_pl_ls)):
    # Gratest decrease
    if change_pl_ls[i] < greatest_dec:
        greatest_dec = change_pl_ls[i]
        date_greatest_dec = date_pl_ls[i]

    # Gratest increase
    if change_pl_ls[i] > greatest_inc:
        greatest_inc = change_pl_ls[i]
        date_greatest_inc = date_pl_ls[i]

# Export text file with results
export_results_to_text_file()

# Print results to terminal
print_results_to_terminal()

