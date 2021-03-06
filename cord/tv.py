import plotly.express as px
import csv
  
with open("tv vs.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Size of TV", y="Average time spent watching TV in a week (hours)")
    fig.show()