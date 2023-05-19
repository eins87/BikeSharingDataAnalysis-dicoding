import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the datasets
all_data = pd.read_csv('dashboard/all.csv')
weather_rentals = all_data.groupby('season_x')['cnt_y'].mean().reset_index()

# Create the Streamlit app
import streamlit as st

name="Andi Winata"
email="andi.winata879@gmail.com"

def main():
    st.title("Bike Sharing Data Analysis - dicoding")

    # Sidebar
    with st.sidebar:
        st.subheader("My Profile")
        st.write("Nama : "+ name)
        st.write("Email : "+ email)

    # First row
    st.subheader('Berapa banyak pengguna berdasarkan season/musim?')

    # Create a bar plot
    fig_season = plt.figure(figsize=(8, 6))
    sns.barplot(data=weather_rentals, x='season_x', y='cnt_y')
    plt.xlabel('Season/musim')
    plt.ylabel('Rata-rata Pengguna')
    plt.xticks(range(4),['spring', 'summer', 'fall', 'winter'])
    plt.title('Rata-rata Bike Rentals berdasarkan season/musim')
    st.pyplot(fig_season)

    # Second row with three columns
    st.subheader('Pada jam berapa rata-rata pengguna paling banyak per-hari dan per-minggu?')
    col1, col2 = st.columns(2)
    with col1:
        st.write("Jam")
        fig_hr = plt.figure(figsize=(12, 6))
        sns.barplot(data=all_data, x='hr', y='cnt_y')
        plt.xlabel('jam dalam sehari')
        plt.ylabel('Pengguna')
        plt.title('Rata-rata Bike Rentals setiap jam')
        st.pyplot(fig_hr)
    with col2:
        st.write("Hari")
        fig_day = plt.figure(figsize=(12, 6))
        sns.barplot(data=all_data, x='weekday_x', y='cnt_y')
        plt.xlabel('Hari dalam seminggu')
        plt.ylabel('pengguna')
        plt.title('Rata-rata Bike Rentals setiap hari')
        plt.xticks(range(7), ['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Min'])
        st.pyplot(fig_day)

    # Third row
    st.subheader('Kesimpulan')
    st.subheader('1. Berapa banyak pengguna berdasarkan season/musim?')
    st.write('dapat di lihat bahwa pengguna lebih banyak menggunakan Bike Sharing pada season/musim summer atau musim panas')
    st.subheader('Pada jam berapa rata-rata pengguna paling banyak per-hari dan per-minggu?')
    st.write('dari data tersebut pengguna paling banyak menggunakan Bike Sharing pada jam 17.00 atau jam 5 sore hari')
    st.write('dan pengguna paling banyak menggunakan Bike Sharing pada hari selasa')

if __name__ == '__main__':
    main()
