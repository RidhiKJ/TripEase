import streamlit as st
import google.generativeai as genai
import requests
import os
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")  # Optional

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")  # Updated model

# Streamlit config
st.set_page_config(page_title="TripEase - AI Travel Planner", layout="centered")

# --- Font Styling ---
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        font-size: 15px;
        line-height: 1.6;
    }
    h1, h2, h3 {
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# --- UI ---
st.title("🌍 TripEase: Your AI-Powered Travel Planner")

with st.form("travel_form"):
    origin = st.text_input("Your Origin", placeholder="e.g., Goa")
    destination = st.text_input("Destination", placeholder="e.g., Japan")
    date = st.date_input("Travel Start Date")
    days = st.number_input("Number of Days", min_value=1, value=3)
    budget = st.selectbox("Budget", ["Low", "Moderate", "High"])
    interests = st.text_area("Your Interests", placeholder="e.g., temples, food, adventure, shopping")
    submit = st.form_submit_button("Generate Itinerary")

if submit:
    if not destination or not origin:
        st.warning("Please fill in both origin and destination.")
    else:
        # Weather API
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={destination}&appid={OPENWEATHER_API_KEY}&units=metric"
        try:
            weather_res = requests.get(weather_url)
            if weather_res.status_code == 200:
                weather_data = weather_res.json()
                weather = f"{weather_data['weather'][0]['description'].capitalize()}, {weather_data['main']['temp']}°C"
            else:
                weather = "Weather info unavailable."
        except:
            weather = "Weather info unavailable."

        # Prompt for Gemini
        prompt = f"""
        Design a {days}-day travel itinerary from {origin} to {destination}, starting on {date}.
        The user has a {budget.lower()} budget and is interested in {interests}.
        Include:
        - Travel options from {origin} to {destination}
        - Accommodation suggestions
        - Daily sightseeing plans
        - Must-try food and drinks
        - Any local customs or tips
        Be brief but helpful and practical.
        """

        # Generate itinerary
        try:
            response = model.generate_content(prompt)
            itinerary = response.text.replace("\n", "<br>")

            st.subheader(f"🌤 Weather in {destination}:")
            st.write(weather)

            st.subheader("📅 Suggested Itinerary:")
            st.markdown(itinerary, unsafe_allow_html=True)

            # Optional: Fetch image from Unsplash
            if UNSPLASH_ACCESS_KEY:
                unsplash_url = f"https://api.unsplash.com/search/photos?query={destination}&client_id={UNSPLASH_ACCESS_KEY}&per_page=1"
                image_res = requests.get(unsplash_url)
                if image_res.status_code == 200:
                    img_data = image_res.json()
                    if img_data['results']:
                        img_url = img_data['results'][0]['urls']['regular']
                        st.image(img_url, caption=f"{destination}", use_column_width=True)
        except Exception as e:
            st.error(f"Failed to generate itinerary: {e}")


