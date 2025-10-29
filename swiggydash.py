import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv("D:/yenaval/swig_profin/cleaned_data.csv")
df['cuisine'] = df['cuisine'].astype(str).apply(lambda x: [i.strip() for i in x.split(',')])

# Page Config
st.set_page_config("Swiggy Restaurant Recommender", page_icon="🍽️", layout="wide")

# Sidebar Filters
with st.sidebar:
    st.markdown("##  Customize Your Search")
    selected_city = st.selectbox(" City", sorted(df['city'].dropna().unique()))
    cuisines = sorted(set(c for sublist in df['cuisine'] for c in sublist))
    selected_cuisines = st.multiselect(" Cuisine", cuisines, default=["Biryani"])
    selected_rating = st.slider(" Minimum Rating", 0.0, 5.0, 3.5, 0.1)
    selected_cost = st.slider(" Max Cost for Two", 100, 2000, 500, 50)
    dark_mode = st.checkbox(" Enable Dark Mode")

# Custom Theme CSS
primary_bg = "#1e1e1e" if dark_mode else "#f0f2f6"
text_color = "#f8f9fa" if dark_mode else "#000"
card_bg = "#2c2c2e" if dark_mode else "#ffffff"
accent_color = "#61dafb" if dark_mode else "#007bff"

st.markdown(f"""
    <style>
    @keyframes fadeSlide {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    section[data-testid="stSidebar"] {{
        background-color: {primary_bg};
        color: {text_color};
        padding: 1rem;
        border-right: 2px solid #ddd;
        animation: fadeSlide 0.6s ease-in-out;
    }}
    .restaurant-card {{
        background-color: {card_bg};
        color: {text_color};
        padding: 1.5rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
        animation: fadeSlide 0.8s ease-in-out;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    .badge {{
        background-color: {accent_color};
        color: white;
        padding: 0.3rem 0.6rem;
        border-radius: 12px;
        font-size: 0.8rem;
        margin-right: 5px;
    }}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown(f"<h1 style='text-align:center; color:{accent_color};'>🍴 Swiggy Restaurant Recommender</h1>", unsafe_allow_html=True)

# Filter Data
filtered_df = df[
    (df['city'].str.lower() == selected_city.lower()) &
    (df['rating'] >= selected_rating) &
    (df['cost'] <= selected_cost) &
    (df['cuisine'].apply(lambda x: any(c in x for c in selected_cuisines)))
]

# Show Results
if not filtered_df.empty:
    st.success(f" {len(filtered_df)} restaurants found in {selected_city.title()}. Browse your recommendations below!")

    cols = st.columns(2)

    for idx, (_, row) in enumerate(filtered_df.iterrows()):
        col = cols[idx % 2]

        rating = row['rating']
        if rating >= 4.0:
            rating_color = "#28a745"
        elif rating >= 3.0:
            rating_color = "#fd7e14"
        else:
            rating_color = "#dc3545"

        cuisines_html = " ".join([f"<span class='badge'>{c}</span>" for c in row['cuisine']])

        with col:
            st.markdown(f"""
            <div class="restaurant-card">
                <h4 style="color:{accent_color}; margin-bottom:0.3rem;">{row['name']}</h4>
                <p> <strong>City:</strong> {row['city']}</p>
                <p> {cuisines_html}</p>
                <p> <strong style="color:{rating_color};">Rating:</strong> <span style="color:{rating_color};">{rating} ({int(row['rating_count'])} ratings)</span></p>
                <p> <strong>Cost for two:</strong> ₹{row['cost']}</p>
                {f"<a href='{row['link']}' target='_blank' style='color:{accent_color}; text-decoration:underline;'>🔗 View Menu</a>" if pd.notna(row['link']) else ""}
            </div>
            """, unsafe_allow_html=True)
else:
    st.warning("No restaurants match your filters. Try adjusting your preferences.")
    st.markdown("![No Data](https://cdn-icons-png.flaticon.com/512/7486/7486793.png)", unsafe_allow_html=True)

# Optional: Add Map View (requires lat/lng)
# if 'latitude' in df.columns and 'longitude' in df.columns:
#    st.map(filtered_df[['latitude', 'longitude']])
