# TripEase
Sure! Here's a clean and informative `README.md` for your **TripEase** AI Travel Planner project:

---

## 🌍 TripEase - AI-Powered Travel Planner

TripEase is your personal AI travel planner that generates customized travel itineraries using Google's Gemini Pro model and real-time weather data via OpenWeather API. Plan trips in seconds with a simple, beautiful Streamlit interface.

---

### 🚀 Features

* 🧠 **AI-Powered Itinerary**: Generates day-by-day travel plans for any destination.
* 🌦️ **Live Weather Updates**: Shows current weather using OpenWeather API.
* 🎯 **Simple UI**: Intuitive and interactive interface built with Streamlit.
* 🔒 **Secure API Key Handling**: Uses `.env` for keeping secrets safe.

---

### 📸 Preview

![TripEase Demo](https://your-screenshot-link-or-local-preview-if-added-later)

---

### 🛠️ Installation

1. **Clone this repo**

   ```bash
   git clone https://github.com/your-username/tripease.git
   cd tripease
   ```

2. **Create and populate `.env` file**

   ```env
   GEMINI_API_KEY=your_gemini_api_key
   OPENWEATHER_API_KEY=your_openweather_api_key
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

### ✅ Requirements

* Python 3.8+
* [Gemini API key](https://makersuite.google.com/app)
* [OpenWeather API key](https://openweathermap.org/api)

---

### 📁 Project Structure

```
tripease/
│
├── app.py               # Main Streamlit app
├── .env                 # API keys and secrets (not tracked in git)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

### 🙌 Credits

* Gemini Pro by Google Generative AI
* OpenWeather API
* Streamlit for the frontend

---

### 🔐 Disclaimer

This is a demo application intended for educational and hackathon purposes. **Do not use it in production without securing API keys properly.**

---

Would you like a logo/banner for the README or app interface as well?
