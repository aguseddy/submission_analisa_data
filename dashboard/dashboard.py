# Import Library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Tampilkan judul
st.title('Proyek Analisa Data')


# Load data csv hasil explorasi RQ1, RQ2, RQ3
rq1_df = pd.read_csv("rq1.csv")
rq2_df = pd.read_csv("rq2.csv")
rq3_df = pd.read_csv("rq3.csv")


with st.sidebar:
    # Menambahkan logo perusahaan
    st.caption('Nama: Eddy Muntina Dharma')
    st.caption('Email: aguseddy@gmail.com')
    st.caption('ID Dicoding: aguseddy')
    

# Visualisasi RQ1
st.subheader("10 Besar Kategori Produk yang paling banyak terjual")

fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    x="counts", 
    y="product_category_name_english",
    data=rq1_df.sort_values(by="counts", ascending=False),
    ax=ax
)

ax.set_title("10 Besar Kategori Produk yang paling banyak terjual", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.xaxis.grid(True)
ax.yaxis.grid(True)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)


# Visualisasi RQ2
st.subheader("Perkembangan omset penjualan per Bulan")

fig, ax = plt.subplots(figsize=(20, 10))

plt.plot(
    rq2_df["thn_bln"],
    rq2_df["jual"],
    lw=2
)
plt.xticks(rotation='vertical')
ax.set_title("Perkembangan omset penjualan per Bulan", fontsize=30)
ax.set_ylabel('Omset')
ax.set_xlabel('Periode')
ax.xaxis.grid(True)
ax.yaxis.grid(True)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

# Visualisasi RQ3
st.subheader("Segmentasi Customer")

fig, ax = plt.subplots(figsize=(20, 10))

sns.barplot(
    x="jml_customer", 
    y="customer_segment",
    data=rq3_df.sort_values(by="customer_segment", ascending=False),
    hue="customer_segment"
)

ax.set_title("Segmentasi Customer", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.xaxis.grid(True)
ax.yaxis.grid(True)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.caption('Copyright (c) 2024')