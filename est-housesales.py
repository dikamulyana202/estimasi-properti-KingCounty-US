import pickle
import streamlit as st

model = pickle.load(open('housesales.sav', 'rb'))

st.title('Estimasi Harga rumah di amerika ')

bathrooms = st.number_input('Input Jumlah kamar mandi')
bedrooms = st.number_input('Input Jumlah kamar tidur')
waterfront = st.number_input('Input properti tepi air')
sqft_living = st.number_input('Input total karbohidrat')
grade = st.number_input('Input kualitas')
sqft_above = st.number_input('Input luas area')
yr_built = st.number_input('Input tahun pembangunan')
let = st.number_input('Input koordinat garis bujur')
long = st.number_input('Input koordinat garis katulistiwa')
zipcode = st.number_input('Input kodepos')
sqft_lot15 = st.number_input('Input luas lahan pada tahun 2015')
sqft_living15 = st.number_input('Input luas bangunan pada tahun 2015')


predict = ''

if st.button('Estimasi Kalori'):
    predict = model.predict(
        [[bathrooms, bedrooms, waterfront, sqft_living, grade, sqft_above,
            yr_built, let, long, zipcode, sqft_lot15, sqft_living15]]
    )
    st.write('Estimasi Harga Properti : ', predict)
