import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Data App", layout="wide")

st.markdown("""
<style>
body, .main {
    background-color: black;
    color: white;
}
.sidebar .sidebar-content {
    background-color: #000000;
    color: white;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_csv(path):
    return pd.read_csv(path)

st.sidebar.title("Navigation")

option = st.sidebar.radio(
    "Choose a section",
    [
        "Display datasets",
        "Google Forms & KoBoToolbox",
        "Dashboard"
    ]
)

if "selected_dataset" not in st.session_state:
    st.session_state.selected_dataset = None


if option == "Display datasets":
    st.header("Datasets")
    st.write("CoinAfrique is a mobile and web platform for buying and selling goods and services in French-speaking Africa. Users can post free classifieds for items like clothing, electronics, vehicles, and real estate, and connect directly with buyers or sellers nearby. It aims to make local commerce simple and accessible via smartphones")
    st.write("Select a dataset below to display it:")

    csv_files = {
        "Data Vetements hommes": "data/vetements-homme.csv",
        "Data Vetements hommes via web scraper": "data/coin_africa_vetements-homme.csv",
        "Data chaussures enfants": "data/chaussures-enfants.csv",
        "Data Chaussures enfants via web scraper": "data/africa_coin_chaussures-enfants.csv",
        "Data chaussures hommes": "data/chaussures-homme.csv",
        "Data chaussures homme via web scraper": "data/coin_africa_chaussures-homme.csv",
        "Data vetements enfants": "data/vetements-enfants.csv",
        "Data vetements enfants via web scraper": "data/coin_afrique_vetements-enfants.csv",
    }

    cols = st.columns(4)  
    index = 0
    for name, path in csv_files.items():
        col = cols[index % 4]  
        if col.button(name):
            st.session_state.selected_dataset = (name, path)
        index += 1

    if st.session_state.selected_dataset:
        name, path = st.session_state.selected_dataset
        st.subheader(f"Dataset: {name}")
        df = load_csv(path)
        st.dataframe(df)

      
        st.download_button(
            label=f"Download {name}",
            data=df.to_csv().encode("utf-8"),
            file_name=f"{name}.csv",
            mime="text/csv"
        )


elif option == "Google Forms & KoBoToolbox":
    st.header("Google Forms & KoBoToolbox")

    st.subheader("KoBoToolbox Form")
    st.write("Click below to open your KoBoToolbox form:")
    st.link_button("Open KoBo Form", url="https://ee-eu.kobotoolbox.org/x/vHSkdLlo")

    st.subheader("Google Form")
    st.write("Click below to open your Google Form:")
    st.link_button("Open Google Form", url="https://docs.google.com/forms/d/e/1FAIpQLSdzBZ31PrlBkM5svPEiecOPQMPCZMmJPgg2ibIsia92Fiwbyg/viewform?usp=dialog")


elif option == "Dashboard":
    st.header("Dashboard")
    st.write("Simple statistics from the Dataset :")
    df = load_csv("data/vetements-homme.csv")

    st.subheader("Dashboard Images")
    col1, col2 = st.columns(2)
    col1.image("images/dashboard_image.png", caption="Price Variation of Men’s Clothing", width=650)
    col2.image("images/plot_julianna2.png", caption="Price Variation of Men’s shoes", width=700)

    col3, col4 = st.columns(2)
    col3.image("images/plot_julianna3.png", caption="Price Variation of kid’s Clothing", width=600)
    col4.image("images/plot_julianna4.png", caption="Price Variation of kid’s shoes", width=700)
