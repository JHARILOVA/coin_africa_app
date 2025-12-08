import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Data App", layout="wide")


st.markdown("""
<style>
body {
    background-color: white;
    color: black;
}
.sidebar .sidebar-content {
    background-color: #000000;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# DATA LOADING FUNCTION
# ------------------------------
@st.cache_data
def load_csv(path):
    return pd.read_csv(path)

# ------------------------------
# SIDEBAR NAVIGATION
# ------------------------------
st.sidebar.title("Navigation")

option = st.sidebar.selectbox(
    "Choose a section",
    [
        "Display my 8 datasets",
        "Google Forms",
        "Dashboard"
    ]
)

# ------------------------------
# SESSION STATE FOR DISPLAY
# ------------------------------
if "selected_dataset" not in st.session_state:
    st.session_state.selected_dataset = None

# ------------------------------
# 1️⃣ DISPLAY 8 CSV FILES
# ------------------------------
if option == "Display my 8 datasets":
    st.header("📂 Display my 8 datasets")
    st.write("Select a dataset below to display it:")

    # 8 datasets
    csv_files = {
        "Vetements_hommes": "data/vetements-homme.csv",
        "coin_africa_vetements-homme": "data/coin_africa_vetements-homme.csv",
        "chaussures-enfants": "data/chaussures-enfants.csv",
        "africa_coin_chaussures-enfants": "data/africa_coin_chaussures-enfants.csv",
        "chaussures-homme": "data/chaussures-homme.csv",
        "coin_africa_chaussures-homme": "data/coin_africa_chaussures-homme.csv",
        "vetements-enfants": "data/vetements-enfants.csv",
        "coin_afrique_vetements-enfants": "data/coin_afrique_vetements-enfants.csv",
    }

    # ----------- Horizontal boutons -----------
    cols = st.columns(4)  # 4 colonnes = 4 boutons par ligne

    index = 0
    for name, path in csv_files.items():
        col = cols[index % 4]   # passer au bouton suivant horizontalement
        if col.button(name):
            st.session_state.selected_dataset = (name, path)
        index += 1

    # ----------- Display selected dataset -----------
    if st.session_state.selected_dataset:
        name, path = st.session_state.selected_dataset
        st.subheader(f"Dataset: {name}")
        df = load_csv(path)
        st.dataframe(df)

# ------------------------------
# 2️⃣ GOOGLE FORMS SECTION
# ------------------------------
elif option == "Google Forms":
    st.header("Google Forms & KoBoToolbox")

    st.subheader("KoBoToolbox Form")
    st.write("Click below to open your KoBoToolbox form:")
    st.link_button("Open KoBo Form", url="https://ee-eu.kobotoolbox.org/x/vHSkdLlo")

    st.subheader("Google Form")
    st.write("Click below to open your Google Form:")
    st.link_button("Open Google Form", url="https://docs.google.com/forms/d/e/1FAIpQLSdzBZ31PrlBkM5svPEiecOPQMPCZMmJPgg2ibIsia92Fiwbyg/viewform?usp=dialog")

# ------------------------------
# 3️⃣ DASHBOARD SECTION
# ------------------------------
# elif option == "Dashboard":
#     st.header("Dashboard")

#     st.write("Example of simple statistics from Dataset 1:")
#     df = load_csv("data/vetements-homme.csv")

#     st.subheader("General Statistics")
#     st.write(df.describe())

#     st.subheader("Line Chart")
#     st.line_chart(df)

# elif option == "Dashboard":
#     st.header("Dashboard")

#     st.write("Example of simple statistics from Dataset 1:")
#     df = load_csv("data/vetements-homme.csv")

#     # st.subheader("General Statistics")
#     # st.write(df.describe())

#     # st.subheader("Line Chart")
#     # st.line_chart(df)

#     st.subheader("Dashboard Image")
#     st.image("images/dashboard_image.png", caption="My Dashboard Illustration", use_column_width=True)
#     st.image("images/plot_julianna2.png", caption="My Dashboard Illustration", use_column_width=True)
#     st.image("images/plot_julianna3.png", caption="My Dashboard Illustration", use_column_width=True)
#     st.image("images/plot_julianna4.png", caption="My Dashboard Illustration", use_column_width=True)
elif option == "Dashboard":
    st.header("Dashboard")

    st.write("Example of simple statistics from Dataset 1:")
    df = load_csv("data/vetements-homme.csv")

    st.subheader("Dashboard Images")

    # Première ligne : 2 colonnes
    col1, col2 = st.columns(2)
    # On utilise width en fonction de la largeur de la colonne
    # Ici 500 px est une taille confortable
    col1.image("images/dashboard_image.png", caption="Dashboard 1", width=650)
    col2.image("images/plot_julianna2.png", caption="Dashboard 2", width=700)

    # Deuxième ligne : 2 colonnes
    col3, col4 = st.columns(2)
    col3.image("images/plot_julianna3.png", caption="Dashboard 3", width=600)
    col4.image("images/plot_julianna4.png", caption="Dashboard 4", width=700)



# ------------------------------
# DOWNLOAD BUTTON (ALWAYS VISIBLE)
# ------------------------------
if st.session_state.selected_dataset:
    name, path = st.session_state.selected_dataset
    st.download_button(
        label=f"⬇️ Download {name}",
        data=load_csv(path).to_csv().encode("utf-8"),
        file_name=f"{name}.csv",
        mime="text/csv"
    )
