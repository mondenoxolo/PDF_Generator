#Importing and install dependencies
import sys
from datetime import date
from pathlib import Path
import sqlite3
import pandas as pd #analyse the data
import plotly.express as px #create plots
from fpdf import FPDF #COnvert to actual PDF

#define paths and chart style
#define the plotly template
plotly_template = "seaborn"

#define the paths
current_dir = Path(__file__).resolve().parent if hasattr(sys, 'frozen') else Path.cwd()
database_path = current_dir / "sales.db"
output_dir = current_dir / "output"

#create the output directory and its parent directory if they do not exist
output_dir.mkdir(parents=True, exist_ok=True)

#TOTAL SALES BY MOTNH
#CReate a connection to the database
conn = sqlite3.connect(database_path)

#Execute the query and load results into a Pandas Dataframe
query = '''SELECT sale_date, SUM(total_price) as total_sales
            FROM sales
            GROUP BY sale_date
            ORDER BY sale_date ASC
'''
df = pd.read_sql_query(query, conn)

#print the dataaframe
print(df)

#cehck the data types
df.info()

#COnvert sale_date to datetime
df['sale_date'] = pd.to_datetime(df['sale_date'])
df.info()

#set the sale_date column as index
df = df.set_index('sale_date')
df.head(3)

#Resample the data to a monthly frequency and compute the sum
df_monthly = df.resample('ME').sum()
df_monthly


#Map the month number to short month month name
df_monthly['month_name'] = df_monthly.index.strftime('%b')
df_monthly

#Create th eplotly figure with text parameter
fig = px.bar(df_monthly,
            x = 'month_name',
            y = 'total_sales',
            template = plotly_template,
            text = 'total_sales')

#set out layout
fig.update_layout(
        title = "Total sales by month",
        xaxis_title = "Month",
        yaxis_title = "Total Sales (R)",
        yaxis_tickprefix = '(R)'
)   

#Show the plot
fig.show()

#Save the chart as aPNG Image
fig.write_image(output_dir/ 'monthly_sales.png',
    width=1200,
    height=400,
    scale=4)

#CReate PDF Report
#define the font color as RGB values 
font_color = (64, 64, 64)

#fin PNG files in the output folder
chart_filenames = [str(chart_path) for chart_path in output_dir.glob("*png")]

#create a pdf document and set the page size
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 24)

#Add the overall page title
title = f"Sales Report as of {date.today().strftime('%m%d%Y')}"
pdf.set_text_color(*font_color)
pdf.cell(0, 20, title, align='C', ln=1)

#Add each chart to the pdf docuemtn

for chart_filename in chart_filenames:
    pdf.ln(10) #Adding padding at the top next to chart
    pdf.image(chart_filename, x=None, y=None, w=pdf.w - 20, h=0)

#Save the pdf docuemtn to a file disk
pdf.output(output_dir / "sales_report.pdf", "F")