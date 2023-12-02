import csv
import matplotlib.pyplot as plt


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
    return average


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
            months.remove(month)
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
        result = 100 * float(difference) // float(listOfSales[index1])
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
        print('Total sales in {}: {}'.format(monthName, total))
    # Find the average of made sales and print it.
    print("Average sales in 2018: {}".format(avg(sales)))
    # Plot sales across the year.
    drawPlot("Sales in 2018", months, sales, "Month", "Sales")
    # Print out the month in which the sale was the lowest and then the one with the highest sales amount.
    salesMonthDict = findLowestHighestSalesMonths(months, sales)
    lowestSale = min(salesMonthDict)
    highestSale = max(salesMonthDict)
    print("The lowest sales value is: {} in {}".format(lowestSale, salesMonthDict[lowestSale]))
    print("The highest sales value is: {} in {}".format(highestSale, salesMonthDict[highestSale]))
    # Calculate the percentage difference in sales for each month.
    percenDif, monthPeriods = calculatePercentDif(sales, months)
    drawPlot('Monthly changes as a percentage', monthPeriods, percenDif, 'month periods', 'monthly changes in %')

