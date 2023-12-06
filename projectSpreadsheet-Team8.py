import csv
import matplotlib.pyplot as plt
import pandas as pd

# Read data from a spreadsheet.
def readDataFromFile(fileName):
    data = []
    with open(fileName, 'r') as file:
        spreadsheet = csv.DictReader(file)
        for row in spreadsheet:
            data.append(row)
    return data


# Find the average of given list of numbers.
def avg(listOfNb):
    average = sum(listOfNb) / len(listOfNb)
    return round(average,2)


# Draw a plot.
def drawPlot(plotTitle, xValues, yValues, xLabel, yLabel):
    plt.figure(figsize=[10, 10])
    plt.title(plotTitle)
    plt.bar(xValues, yValues)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()


# Find months with the lowest and the highest sales.
def findLowestHighestSalesMonths(monthNames, saleAmounts):
    salesMonthDict = {}
    for sale in saleAmounts:
        for month in monthNames:
            salesMonthDict[sale] = month
            monthNames.remove(month)
            break
    return salesMonthDict

#  # Calculate monthly sales difference in percent across the year.
def calculatePercentDif(listOfSales, listOfMonths):
    percentDif = []
    nbOfDif = len(listOfSales) - 1
    monthsForDif = []
    for index1 in range(nbOfDif):
        index2 = index1 + 1
        difference = listOfSales[index2] - listOfSales[index1]
        monthsForDif.append(listOfMonths[index1] + '-' + listOfMonths[index2])
        result = 100 * difference // listOfSales[index1]
        percentDif.append(result)
    return percentDif, monthsForDif

if __name__ == '__main__':

    data = readDataFromFile('sales.csv')
    sales = []
    months = []
    for row in data:
        monthlySale = int(row['sales'])
        monthName = row['month']
        months.append(monthName)
        sales.append(monthlySale)
    total = sum(sales)
    # Plot sales across the year.
    drawPlot("Sales in 2018", months, sales, "Month", "Sales")
    # Calculate the percentage difference in sales for each month.
    percenDif, monthPeriods = calculatePercentDif(sales, months)
    drawPlot('Monthly changes as a percentage', monthPeriods, percenDif, 'month periods', 'monthly changes in %')
    # Find a month in which the sale was the lowest and then the one with the highest sales amount.
    salesMonthDict = findLowestHighestSalesMonths(months, sales)
    lowestSale = min(salesMonthDict)
    highestSale = max(salesMonthDict)

    # Add summary of the data into a new csv file.
    sales_data = pd.read_csv('sales.csv')

    # Add a zero value to the list of monthly changes for January.
    percenDif.insert(0, 0)
    # Add a new column to the sales file for the sales monthly changes.
    sales_data['monthly_changes[%]'] = percenDif
    sales_data.to_csv('sales2.csv', index = False)

    # Add summary of the gathered data into a new csv file.
    with open('sales2.csv', 'a') as sales_csv:
        sales_csv.write("Total sales across all months is {}.".format(total))
        sales_csv.write('\n')
        sales_csv.write('Average sales in 2018 was {}.'.format((avg(sales))))
        sales_csv.write('\n')
        sales_csv.write('The lowest sales value occurred in {} and had a value of {}'.format(salesMonthDict[lowestSale], lowestSale))
        sales_csv.write('\n')
        sales_csv.write('The highest sales value occurred in {} and had a value of {}'.format(salesMonthDict[highestSale], highestSale))
