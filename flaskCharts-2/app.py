from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/google-charts/pie-chart')
def google_pie_chart():
    data = {'Task' : 'Hours per Day', 'Work' : 11, 'Eat' : 2, 'Commute' : 2, 'Watching TV' : 2, 'Sleeping' : 7}
    return render_template('pie-chart.html', data=data)

if __name__ == "__main__":
    app.run()

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px

# sns.set()
# df = pd.read_csv('/kaggle/input/daily-temperature-of-major-cities/city_temperature.csv', low_memory= False)
# df.head()
# df.info()
# print(f'{df.shape[1]} columns and {df.shape[0]} rows.')