import streamlit as st
from streamlit_gsheets import GSheetsConnection

# URL lengkap Google Sheet publik Anda
# Contoh: https://docs.google.com/spreadsheets/d/1BxiMVs0XRAmX6Z_GSSN_BVxN_L3e_s_a_T-F/edit?usp=sharing
PUBLIC_SHEET_URL = "https://docs.google.com/spreadsheets/d/1M395nIYCKa3euENuHc6E8fUeg-8Jfe0i/edit?usp=sharing&ouid=107287618249371338490&rtpof=true&sd=true" 

st.title("Aplikasi Streamlit & Google Sheets Publik 🌐")

# Membuat objek koneksi. Karena ini publik, tidak ada parameter secrets yang akan dibaca.
conn = st.connection("gsheets", type=GSheetsConnection)

try:
    # Menggunakan URL sebagai sumber data.
    df = conn.read(
        spreadsheet=PUBLIC_SHEET_URL, 
        worksheet="Sheet1", # Ganti dengan nama sheet Anda jika berbeda
        ttl="5m" # Cache data selama 5 menit
    ) 

    st.subheader("Data yang Dibaca dari Google Sheet Publik:")
    st.dataframe(df)

    st.success(f"Berhasil membaca {len(df)} baris data.")

except Exception as e:
    st.error(f"Gagal membaca data. Pastikan URL benar dan sheet benar-benar publik. Error: {e}")