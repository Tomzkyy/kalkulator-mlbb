import streamlit as st
import pandas as pd

st.title("Kalkulator Winrate MLBB")

# Input
img_url = "logo.png"  # Ganti dengan URL gambar yang ingin Anda gunakan
st.sidebar.image(img_url, use_column_width=True)
st.sidebar.header("Silahkan masukan data")


def calculate_total_match(total_match, winrate_saat_ini, winrate_yang_diinginkan):
    result = (winrate_yang_diinginkan * total_match - winrate_saat_ini *
              total_match) / (100 - winrate_yang_diinginkan)
    return round(result)


def main():

    total_match = int(st.sidebar.number_input(
        "Jumlah Pertandingan", min_value=0))
    winrate_saat_ini = st.sidebar.number_input(
        "Winrate saat ini (55.75)")
    winrate_yang_diinginkan = st.sidebar.number_input(
        "Winrate yang diinginkan (65.75)")

    # Menampilkan hasil input pada tabel di sisi subheader
    st.subheader("Data yang telah dimasukkan")
    st.write("Jumlah pertandingan: ", f"{total_match}")
    st.write("Winrate saat ini: ", f"{winrate_saat_ini:.2f}%")
    st.write("Winrate yang diinginkan: ", f"{winrate_yang_diinginkan:.2f}%")

    # Tombol hitung
    if st.button("Hitung"):
        result = calculate_total_match(
            total_match, winrate_saat_ini, winrate_yang_diinginkan)

        # Output
        st.success(
            f"Anda harus bermain sebanyak {result} match tanpa kekalahan untuk mencapai winrate {round(winrate_yang_diinginkan)}%")


if __name__ == "__main__":
    main()
