import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    df = pd.read_csv(file)

    # Фильтровать данные по условию, в которых Брижит Бардо снималась актрисой
    filtered_data = df[df['Actress'] == 'Brigitte Bardot']

    # Создать график на основе отфильтрованных данных
    plt.bar(filtered_data['Year'], filtered_data['Title'])
    plt.xlabel('Year')
    plt.ylabel('Title')
    plt.title('Films with Brigitte Bardot as Actress')

    # Сохранить график в файл и отобразить его на странице
    plt.savefig('static/plot.png')
    return render_template('plot.html')

if __name__ == '__main__':
    app.run(debug=True)


