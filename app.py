import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly_express as px
import plotly.graph_objects as go

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

df = pd.read_csv(link)

df["continent"] = df["continent"].apply(lambda x: x.replace(" ", "").replace(".", ""))

if "continent" not in st.session_state:
    st.session_state["continent"] = "all"

if st.session_state["continent"] == "US":
	filtered_df = df[df["continent"] == "US"]
elif st.session_state["continent"] == "Europe":
	filtered_df = df[df["continent"] == "Europe"]
elif st.session_state["continent"] == "Japan":
	filtered_df = df[df["continent"] == "Japan"]
else:
	filtered_df = df

st.title("Study of the Cars Dataset")

st.write("Dataframe")
filtered_df

fig1 = px.box(filtered_df["mpg"])

fig2 = px.box(filtered_df["cylinders"])

fig1

st.write("Le nombre de mpg est plus élevé en moyenne au japon qu'en Amérique.")

fig2

st.write("Le nombre de cylindes est beaucoup plus élevé en Amérique que dans le reste du monde.")

col1, col2, col3 = st.columns(3)
if col1.button("US"):
    st.session_state["continent"] = "US"
    st.rerun()
if col2.button("Europe"):
    st.session_state["continent"] = "Europe"
    st.rerun()
if col3.button("Japan"):
    st.session_state["continent"] = "Japan"
    st.rerun()