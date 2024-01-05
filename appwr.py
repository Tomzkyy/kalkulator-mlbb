import streamlit as st
import pandas as pd
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(
    page_title="Kalkulator Winrate By TOMZKY",
    # page icon menggunakan logo dan perbesar ukurannya
    page_icon="logo.png"
)

# Set the width of the main content
img = Image.open("logo.png")
img = img.resize((200, 200))
# Convert the image to a base64 string
buffered = BytesIO()
img.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Display the image with spacing
st.markdown(
    f'<div style="text-align: center; margin-bottom: 20px;"><img src="data:image/png;base64,{img_str}" width="200"></div>',
    unsafe_allow_html=True,
)

# Judul without spacing
st.markdown("<h1 style='text-align: center; color: black;'>Kalkulator Winrate MLBB</h1>",
            unsafe_allow_html=True)

# Deskripsi with spacing
st.markdown("<div style='text-align: center; margin-bottom: 20px;'>Kalkulator ini digunakan untuk menghitung berapa banyak match yang harus dimainkan tanpa kekalahan untuk mencapai winrate yang diinginkan.</div>", unsafe_allow_html=True)

# Fungsi untuk menghitung total match


def calculate_total_match(total_match, winrate_saat_ini, winrate_yang_diinginkan):
    result = (winrate_yang_diinginkan * total_match - winrate_saat_ini *
              total_match) / (100 - winrate_yang_diinginkan)
    return round(result)


# Fungsi utama
def main():

    # inputan user
    total_match = int(st.number_input("Total match saat ini", min_value=0))
    winrate_saat_ini = st.number_input(
        "Winrate saat ini (contoh = 55.75)")
    winrate_yang_diinginkan = st.number_input(
        "Winrate yang diinginkan (contoh = 60.00)")

    button = st.button("**Hitung**", type="primary")

    # Tombol hitung
    if button:
        result = calculate_total_match(
            total_match, winrate_saat_ini, winrate_yang_diinginkan)

        # Output
        st.success(
            f"Anda harus bermain sebanyak {result} match tanpa kekalahan untuk mencapai winrate {round(winrate_yang_diinginkan)}%")


if __name__ == "__main__":
    main()
