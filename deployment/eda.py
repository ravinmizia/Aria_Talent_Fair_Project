import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import plotly


page_bg_img = '''
<style>
body {
background-image: url("https://raw.githubusercontent.com/andfanilo/social-media-tutorials/master/20220817-streamlit_css_background/image.jpg");
background-size: cover;
}
</style>
'''

#melebarkan
st.set_page_config(
    page_title='ARIA Nutrition',
    initial_sidebar_state='expanded'

)



def run():

    # Set title
    st.markdown("<h1 style='text-align: center; color: black;'>ARIA Plant Nutrition</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: grey ;'>Exploratory Data Analysis</h2>", unsafe_allow_html=True)

    st.markdown('***')

    # library pillow buat gambar

    
    image = Image.open('ariaicon.png')
   
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')
    with col2:
        st.image(image) 
    with col3:
        st.write(' ')



    st.markdown('---')    

    # Nampilin dataframe
    st.write('### Data Table')

    data = pd.read_excel('aria_data.xlsx')
    st.dataframe(data)

    st.markdown('***')
    #barplot
    fig = plt.figure(figsize=(8,5))


    st.write('### Pola Distribusi Variabel dan Target ')
    
    # distribusi data
    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(25,8))

    n = 0
    m = 0
    for i in data.iloc[:,1:5].columns:
        sns.scatterplot(data, x=i, y='target', hue='sample_type', ax=axes[0][n]) 
        n = n+1
    for col in data.iloc[:,5:9].columns:
        sns.scatterplot(data, x=col, y='target', hue='sample_type', ax=axes[1][m]) 
        m = m+1
    plt.tight_layout()
    st.pyplot(fig)

    st.write('###### - Singkatnya variabel bisa dikategorikan menjadi 4 kategori :')
    st.write('###### - Grup 1 (v1, v3) = nilai variabelnya jelas berbeda pada tipe sample yang berbeda. Secara visual pun, v1 dan v3 memiliki korelasi yang cukup tinggi.')
    st.write('###### - Grup 2 (v2,v4,v5,v6)  = nilai variabelnya masih bisa dibedakan pada masing masing tipe sampel (lab 1 dan lab 2) namun masuk terlihat terpisah. Juga secara visual pada scatterplot, variabel-variabel ini terlihat memiliki korelasi yang cukup tinggi.')
    st.write('###### - Grup 3 (v7) = nilai data pada v7 ini tersebar secara merata, independen terhadap sample_type. DIstribusi valuenya cenderung lebih tinggi dari v1 s/d v6.')
    st.write('###### - Grup 4 (v8) = adalah variabel yang paling berbeda. Tidak hanya valuenya yang jauh lebih tinggi. Distrbusi nya pun serupa dengan Grup 2 hanya saja berbanding terbalik.')   
    st.markdown('***')




    st.write('### Analisa Perilaku Variabel')
    #plot
    # plotting data berdasarkan nilai variabel
    fig1, (ax1,ax2,ax3) = plt.subplots(3,1, figsize=(15,10))
    sns.lineplot(data.iloc[:,8:9], ax=ax1, ls='--')
    ax1.axvline(100, c='r', ls='--')
    ax1.axvline(130, ls='--')
    ax1.text(60,5000,'Batas antara Lab 1 dan Lab 2', c='r', fontsize=12)
    ax1.text(132,4500,'30th input Lab 2', c='b', fontsize=12)

    sns.lineplot(data.iloc[:,7:8], ax=ax2, ls='--')
    ax2.axvline(100, c='r', ls='--')
    ax2.axvline(130, ls='--')
    #ax2.text(70,800,'Batas antara Lab 1 dan Lab 2', c='r', fontsize=9)

    sns.lineplot(data.iloc[:,1:7], ax=ax3)
    ax3.axvline(100, c='r', ls='--')
    ax3.axvline(130, ls='--')
    #ax3.text(70,600,'Batas antara Lab 1 dan Lab 2', c='r', fontsize=9)

    st.pyplot(fig1)
    st.write('###### Pertama jika dilihat secara visual terdapat perbedaan perilaku value dari seluruh vriabel pada tipe sample atau lab yang berbeda. Rata-rata nilai v1 s/d v6 mengalami kenaikan yang cukup signifikan terutama v1 yang perbedaannya sampai 2x lipat.')
    st.write('###### Yang menarik lagi dari data yang didapatkan adalah adanya perubahan value variabel pada jenis sample lab 2, dimana ada trend ada loncatan pada input data ke 30 pada lab 2. Dimana variabel v1-v7 mengalami kenaikan nilai, sedangkan v8 mengalami penurunan yang signifikan.')
    

    st.markdown('***')

    #hist berdasarkan intpput user
    st.write('### Histograms')
    pilihan = st.selectbox('Pilih Kolum : ', ('v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8'))
    fig2=plt.figure(figsize=(15,5))
    sns.histplot(data[pilihan], bins=  30, kde=True)
    st.pyplot(fig2)


    st.markdown('***')


if __name__ == '__main__':
    run()