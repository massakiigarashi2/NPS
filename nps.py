import streamlit as st
from PIL import Image
from io import BytesIO

#import plotly.graph_objects as go
import altair as alt
from urllib.error import URLError
from urllib.request import urlopen

import requests
import pandas as pd
r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRJMjhO1yr6ArOVOdpWX_9uQ8Ban7UYi7juE_6Gubd4Nd4Z5lZTKTRXzd-hyNbvRqXrCd2GaiN7ziXW/pub?gid=0&single=true&output=csv')
data = r.content
df = pd.DataFrame(pd.read_csv(BytesIO(data)))
perguntas = df['PERGUNTAS']

r1 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRJMjhO1yr6ArOVOdpWX_9uQ8Ban7UYi7juE_6Gubd4Nd4Z5lZTKTRXzd-hyNbvRqXrCd2GaiN7ziXW/pub?gid=762853940&single=true&output=csv')
data1 = r1.content
df1 = pd.DataFrame(pd.read_csv(BytesIO(data1)))
df1 = df1['Nota'].value_counts()
n = len(df1)
arr1 = []
for i in range(0,11):
    arr1.append(0)



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

from urllib.request import urlopen

def SendMAIL(assunto):
    # create message object instance 
    msg = MIMEMultipart()     
    # setup the parameters of the message 
    password = "efoqfcwiorncteas"
    msg['From'] = "prof.massaki@gmail.com"
    msg['To'] =   "prof.massaki@gmail.com"
    msg['Subject'] = assunto
    #file = "Python.pdf"
    # attach image to message body 
    #msg.attach(MIMEText(open(file).read()))     
    # create server 
    server = smtplib.SMTP('smtp.gmail.com: 587')     
    server.starttls()     
    # Login Credentials for sending the mail 
    server.login(msg['From'], password)      
    # send the message via the server. 
    server.sendmail(msg['From'], msg['To'], msg.as_string("MENSAGEM TESTE"))     
    server.quit()

st.set_page_config(
     page_title="Formulário de Cadastro",
     page_icon=":date:",
     layout="wide",
     initial_sidebar_state="expanded"     
 )

new=2

#st.write(df.head())
#st.title('ESCUTA ATIVA - CCT/Mackenzie')
st.header('Avaliação NPS!')


#txtNome = st.text_input("Digite seu nome completo 👇")

#st.dataframe(df)
#st.dataframe(df1)

option = st.selectbox('Escolha uma pergunta:', perguntas)
#Nota = st.slider('Digite nota?', 0, 10, 1)
#st.write("Nota ", Nota, 'na avaliação NPS.')
Nota = st.number_input("Digite sua avaliação NPS", min_value=0, max_value=10, value=10, step=1)
if option:    
    #url= 'https://docs.google.com/forms/d/e/1FAIpQLSeRz9xdCeMjvDUNEEJtJQxM5vYP9O_p0V6Y0elOJQuPS1Q4QQ/formResponse?&submit=Submit?usp=pp_url&entry.280447386={option}&entry.1586579028={Nota}'
    response = urlopen(
    f' https://docs.google.com/forms/d/e/1FAIpQLSeRz9xdCeMjvDUNEEJtJQxM5vYP9O_p0V6Y0elOJQuPS1Q4QQ/formResponse?&submit=Submit?usp=pp_url&entry.280447386={str(option)}&entry.1586579028={str(Nota)}')
    
    st.write('Pergunta selecionada:', option)           
    st.write('Nota atribuída:', Nota) 
      
if st.button('Confirmar 👇'):    
    #response = urlopen(f'{url}')
    html = response.read()

