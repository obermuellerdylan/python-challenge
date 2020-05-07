import os
import csv

#Path to CSV File
budget_data = os.path.join('Resources', 'budget_data.csv')

#Defining Function
def financial_analysis(): 
    

    #Creating list to organize data
    months = []
    monthly_profit = []
    monthly_change = []

    for row in csvreader:
        months.append(row[0])
        monthly_profit.append(int(row[1]))

    # Total Months and Income
    total_months = len(months)
    net_income = sum((monthly_profit))

    #Looping through profit to find monthly change
    for i in range(total_months-1):
        difference = monthly_profit[i+1] - monthly_profit[i]
        monthly_change.append(difference)

        #Finding max and min then applying the month
        max_profit = max(monthly_change)
        max_loss = min(monthly_change)
    
        if max_profit == int(monthly_change[i]):
            max_profit_month = months[i+1]
        elif max_loss == int(monthly_change[i]):
            max_loss_month = months[i+1]
    
    average_change = round(sum(monthly_change) / (total_months-1),2)

    # Printing Results
    print('Financial Analysis')
    print('-----------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_income}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {max_profit_month} (${max_profit})')
    print(f'Greatest Decrease in Profits: {max_loss_month} (${max_loss})')

    # write results to text file
    # Specify the file to write to
    output_path = os.path.join("Resources", "main.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as txtfile:
    

        # Write the first row (column headers)
        txtfile.write('Financial Analysis\n')
        txtfile.write('-----------------------\n')
        txtfile.write(f'Total Months: {total_months}\n')
        txtfile.write(f'Total: ${net_income}\n')
        txtfile.write(f'Average Change: ${average_change}\n')
        txtfile.write(f'Greatest Increase in Profits: {max_profit_month} (${max_profit})\n')
        txtfile.write(f'Greatest Decrease in Profits: {max_loss_month} (${max_loss})\n')

# Open file and create csvreader - skip header
with open(budget_data, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #RUN FUNCTION
    financial_analysis()
    
    


    
    