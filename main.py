# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Load the sample dataset
def load_data():
    data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    return data

# Scatter plot function
def scatter_plot(data):
    st.subheader("Scatter Plot")
    sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species")
    st.pyplot()

# Bar chart function
def bar_chart(data):
    st.subheader("Bar Chart")
    data_grouped = data.groupby("species").mean()
    data_grouped.plot(kind="bar")
    st.pyplot()

# Histogram function
def histogram(data):
    st.subheader("Histogram")
    num_bins = st.sidebar.slider("Number of bins:", 5, 50, 20)
    species = st.sidebar.selectbox("Select a species:", data["species"].unique())
    data_species = data[data["species"] == species]
    sns.histplot(data=data_species, bins=num_bins)
    st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Example Healthcare App")
st.write("Welcome to the example healthcare app. This app demonstrates basic data visualization and exploration using a sample dataset.")

# Load the sample dataset
data = load_data()

# Display the dataset
st.subheader("Dataset")
st.write(data)

# Create interactive data exploration features
st.sidebar.title("Data Exploration")
st.sidebar.subheader("Choose a visualization:")

plot_options = ["Scatter Plot", "Bar Chart", "Histogram"]
plot_choice = st.sidebar.selectbox("Select a plot type:", plot_options)

if plot_choice == "Scatter Plot":
    scatter_plot(data)
elif plot_choice == "Bar Chart":
    bar_chart(data)
elif plot_choice == "Histogram":
    histogram(data)
