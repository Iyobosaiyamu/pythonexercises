import csv
import datetime

# Function to convert epoch timestamp to datetime
def convert_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Read the sales data from the CSV file
with open('sales.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Skip the header row
    sales_data = list(csv_reader)

# Calculate total sales for each product
product_sales = {}
for row in sales_data:
    product_name = row[1]
    quantity = int(row[2])
    price = float(row[3])
    if product_name in product_sales:
        product_sales[product_name]['quantity'] += quantity
        product_sales[product_name]['sales_amount'] += quantity * price
    else:
        product_sales[product_name] = {
            'quantity': quantity,
            'sales_amount': quantity * price
        }

# Find the first and last sale timestamps
timestamps = [int(row[0]) for row in sales_data]
first_sale_timestamp = min(timestamps)
last_sale_timestamp = max(timestamps)

# Convert timestamps to readable format
first_sale_datetime = convert_timestamp(first_sale_timestamp)
last_sale_datetime = convert_timestamp(last_sale_timestamp)

# Write the sales report to a new PSV file
with open('sales_report.psv', 'w', newline='') as psv_file:
    psv_writer = csv.writer(psv_file, delimiter='|')
    psv_writer.writerow(['Product Name', 'First Sale Datetime', 'Last Sale Datetime', 'Total Quantity Sold', 'Total Sales Amount'])
    for product_name, sales_info in product_sales.items():
        quantity_sold = sales_info['quantity']
        total_sales_amount = sales_info['sales_amount']
        psv_writer.writerow([product_name, first_sale_datetime, last_sale_datetime, quantity_sold, total_sales_amount])

print("Sales report generated successfully.")