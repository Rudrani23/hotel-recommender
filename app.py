import streamlit as st

st.set_page_config(page_title="Hotel Recommender", layout="wide")

import data_loader

@st.cache_data
def load_data():
    return data_loader.load_data()

df = load_data()

st.title("🏨 Indian Hotels Recommendation System")

states = data_loader.get_states(df)
if not states:
    st.error("No states found.")
    st.stop()

state = st.selectbox("Select State", states)

cities = data_loader.get_cities(df, state)
if not cities:
    st.warning(f"No cities found for {state}")
    st.stop()

city = st.selectbox("Select City", cities)

hotels = data_loader.get_hotels(df, state, city)
if hotels.empty:
    st.info(f"No hotels found in {city}, {state}.")
else:
    st.subheader(f"Hotels in {city}, {state}")

    HOTEL_COL = data_loader.HOTEL_COL
    STAR_COL = data_loader.STAR_COL
    ADDRESS_COL = data_loader.ADDRESS_COL
    REVIEW_COL = data_loader.REVIEW_COL

    for _, row in hotels.iterrows():
        st.markdown(f"### 🏨 {row.get(HOTEL_COL, 'N/A')}")
        st.markdown(f"⭐ **Star Rating:** {row.get(STAR_COL, 'N/A')}")
        st.markdown(f"📍 **Address:** {row.get(ADDRESS_COL, 'N/A')}")
        st.markdown(f"📝 **User Review Rating:** {row.get(REVIEW_COL, 'No review')}")
        st.markdown("---")

