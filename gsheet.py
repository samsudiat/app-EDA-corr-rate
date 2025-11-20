import streamlit as st
import pandas as pd

st.title("Result ST")

SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1jxeIwmbgdtxXorTkVta9B7I9Ugirv3Ta/edit?usp=sharing&ouid=107287618249371338490&rtpof=true&sd=true"
SHEET_NAME = "RESULT%20ST"

@st.cache_data(ttl=600)  # Data akan di-cache selama 600 detik (10 menit)
def load_data(url, sheet_name):
    try:
        if '/edit' in url:
            base_url = url.split('/edit')[0]
        else:
            base_url = url

        csv_export_url = f"{base_url}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        
        df = pd.read_csv(csv_export_url)
        return df
    except Exception as e:
        st.error(f"Gagal memuat data dari Google Sheet. Pastikan URL, nama sheet ('{sheet_name}'), dan aksesnya publik. Error: {e}")
        return pd.DataFrame()

st.info(f"Memuat data dari sheet: **{SHEET_NAME}**")
df = load_data(SPREADSHEET_URL, SHEET_NAME)

if not df.empty:
    st.success(f"Data dari sheet '{SHEET_NAME}' berhasil dimuat!")
    st.dataframe(df)
    
    st.subheader("Informasi Data")
    st.write(f"Jumlah Baris: **{len(df)}**")
    st.write(f"Jumlah Kolom: **{len(df.columns)}**")

else:
    st.warning("Tidak ada data yang dimuat. Periksa URL spreadsheet atau nama sheet Anda.")