#!/usr/bin/env python
# coding: utf-8


# In[1]:

primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"


import streamlit as st
import numpy as np
import joblib
from predict_cost import predict #  PREDICT çağırdığımız dosyadaki fonksiyon
#Arayüzümüz

st.markdown (' Fiyat Tahmini')
st.write('--')
# her öznitelik kolon için aşağıdaki gibi giriş alanı oluşturuyoruz
Ekran_Karti = st.number_input('-------EKRAN KARTI-------RTX 4060=47,RTX 3050=40,Intel Graphics=20,RTX 4050=46, Intel Iris Graphics=18,Dahili=14, AMD Radeon Graphics=2,RTX3060=53,RTX 4070=49,RTX 3050 Ti= 41,Radeon RX 580=9,Intel HD Graphics=15,Intel UHD Graphics 600=21,RTX 2050=37,RTX 4090=52,M3=28,Radeon RX 550=7,Intel XE Graphics=23,Belirtilmemiş=13,GT 740=54,RTX 2060 Super=39,MX450=36,AMD=0,RTX 4060Ti=48,GT 730=30,MX350=35,M2 8 Çekirdekli=26,GTX 1650=31,Radeon R7 240=6,GTX 1660 SUPER=32,RTX 2060=38,RTX 4080=51,M2 10 Çekirdekli=25,GT730=29,RTX 3060 Ti=42,AMD R7 250=1,GTX1050 Ti=33,Radeon Vega 3=11,RTX 4070 Ti=50,Radeon RX6500M=10,GT 730=56,Paylaşımlı=57,Quadro RTX 4000=58,RTX 3080=44,Intel Iris Pro Graphics=19,Intel HD Graphics 520=16,Radeon R5=4,GeForce MX330=34,Intel UHD Graphics 620=22,Radeon R7=5,M2 Pro 19 Çekirdekli=27,Radeon R3=3,RTX 3070Ti=43,M1 7 Çekirdekli=24,RTX A6000=55,RX 5500 XT=8,Intel HD Graphics 610=17,RTX 3080 Ti=45,Radeon Vega 8 =12  ')                 
Ekran_Karti_Hafizasi = st.number_input('----Ekran Kartı Hafızası----  Paylaşımlı = 7, ')
Ekran_Karti_Tipi = st.number_input('--- Ekran Kartı Tipi ---  Harici = 2, Dahili=1')
Garanti_Suresi = st.number_input('Garanti Süresi  2Yıl=0,3Yıl=1') 
Garanti_Tipi = st.number_input('---Garanti Tipi---  Resmi Distribütor Garantili = 18 , İthalatçı Garantili = 16 ')
Ram = st.number_input('Ram')
SSD_Kapasitesi = st. number_input('SSD Kapasitesi (megabayt türünden yazınız.)' )
Islemci_Tipi = st.number_input('---İslemci Tipi---  Intel = 17, AMD = 6')
Islemci_Cekirdek_Sayisi = st.number_input('İslemci Cekirdek Sayisi')
                                     
if st.button('<-- LAPTOP FİYATINI TAHMİN ET -->'):
    fiyat = predict(np.array([[Ekran_Karti, Ekran_Karti_Hafizasi, Ekran_Karti_Tipi, Garanti_Suresi, Garanti_Tipi, Ram, SSD_Kapasitesi,Islemci_Tipi,Islemci_Cekirdek_Sayisi]]))

    st.text(fiyat[0])

                                     
                  
# In[ ]:





