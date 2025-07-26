# ✈️ Airline Route Insight Dashboard

This Flask-based web application fetches real-time airline flight data from the [AviationStack API](https://aviationstack.com/), analyzes popular routes, generates mock price trends, and provides AI-driven travel insights.

## 🔧 Features

- ✅ Real-time data from AviationStack API
- ✅ Most frequently traveled airline routes
- ✅ Weekly mock price trends per route
- ✅ AI-generated travel insight (based on demand)
- ✅ Beautiful UI with live backgrounds and animations

## 📸 Screenshots
<img src="https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=800" width="100%" />

## 🚀 How It Works

1. User lands on the homepage and clicks "Fetch Live Data"
2. Data is fetched from the API and analyzed
3. Routes are ranked by popularity
4. Mock price trends are generated per route
5. Insightful summary is shown at the top

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, Bootstrap, custom CSS
- **API**: AviationStack
- **Deployment**: PythonAnywhere

## 📁 Project Structure

airline_booking_app/
│
├── app.py
├── templates/
│ ├── index.html
│ └── results.html
├── requirements.txt
└── README.md


## 📦 Setup & Run Locally

```bash
git clone https://github.com/yourusername/airline_booking_app.git
cd airline_booking_app
pip install -r requirements.txt
python app.py


🚨 Replace API_KEY in app.py with your own key from AviationStack

🧠 AI Insight Example
"The most frequent route this week is Delhi → Mumbai with 9 flights. Consider booking early to avoid price hikes."

📝 Author
Aashish Jangir


📄 License
This project is licensed under the MIT License.