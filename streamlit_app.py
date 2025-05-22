import streamlit as st

st.title("🎈 kue manis")
st.write(
    " kue manis pemanis hidup"
)
st.image("IMG-20250514-WA0036.jpg")


#st.header ("Aplikasi mengecrk nilai genap/ganjil")
angka = st.number_input("Tulis sebuah angka:", value=0, steps=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap") 
else:
    st.write(f"{angka} adalah bilangan ganjil")
