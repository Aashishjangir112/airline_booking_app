from flask import Flask, render_template, request
import requests
import pandas as pd
import random

app = Flask(__name__)

API_KEY = '994fc8777b1a9c5331ec81679d93eb2e'
BASE_URL = 'http://api.aviationstack.com/v1/flights'


def fetch_airline_data(limit=20):
    params = {'access_key': API_KEY, 'limit': limit}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get('data', [])
    return []


def analyze_routes(data):
    routes = []
    for flight in data:
        try:
            dep = flight['departure']['airport']
            arr = flight['arrival']['airport']
            if dep and arr:
                routes.append(f"{dep} → {arr}")
        except:
            continue
    df = pd.DataFrame(routes, columns=["Route"])
    route_counts = df['Route'].value_counts().reset_index()
    route_counts.columns = ['Route', 'Count']
    return route_counts


def generate_price_trends(routes):
    trends = []
    for _, row in routes.iterrows():
        prices = [random.randint(3000, 12000) for _ in range(7)]
        trends.append({
            'route': row['Route'],
            'prices': prices,
            'days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        })
    return trends


def generate_ai_insights(routes):
    if routes.empty:
        return "No data available to analyze trends."

    top_route = routes.iloc[0]
    insight = (
        f"The most frequent route this week is <b>{top_route['Route']}</b> with "
        f"<b>{top_route['Count']}</b> flights. This suggests a high travel demand "
        f"between these two airports. Consider booking early to avoid price hikes."
    )
    return insight


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    raw_data = fetch_airline_data()
    route_stats = analyze_routes(raw_data)

    price_trends = generate_price_trends(route_stats)
    insights = generate_ai_insights(route_stats)

    return render_template(
        'results.html',
        popular_routes=route_stats.to_dict(orient='records'),
        price_trends=price_trends,
        insights=insights
    )


if __name__ == '__main__':
    app.run(debug=True)
