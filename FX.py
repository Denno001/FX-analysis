import streamlit as st
import yfinance as yf
import pandas as pd
import base64
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns


st.write('''
#### This app compares and analyses perfomance of various currency pairs using adjusted close price data from the [Yahoo Finance](https://finance.yahoo.com/) library.  
* ##### Data captured here starts from 2008 up to the last updated values in the library.
''')
('---')
#...extracting only the adj close....
FX = yf.download('USDKES=X USDCAD=X USDCNY=X USDGHS=X USDINR=X USDJPY=X USDNGN=X USDRUB=X USDGBP=X GBPKES=X USDZAR=X USDEUR=X', start='2008-01-01')['Adj Close']

#..renaming columns....

dict = {'GBPKES=X': 'GBP/KES',
        'USDCAD=X': 'USD/CAD',
        'USDCNY=X': 'USD/CNY',
        'USDEUR=X': 'USD/EUR',
        'USDGBP=X': 'USD/GBP',
        'USDGHS=X': 'USD/GHS',
        'USDINR=X': 'USD/INR',
        'USDJPY=X': 'USD/JPY',
        'USDKES=X': 'USD/KES',
        'USDNGN=X': 'USD/NGN',
        'USDRUB=X': 'USD/RUB',
        'USDZAR=X': 'USD/ZAR'}
        
FX.rename(columns=dict, inplace=True)
FX = FX.reset_index().set_index('Date', drop=False)
FX = FX.reset_index(drop=True)
#FX


#....inserting sidebar and label
st.sidebar.header('Filter Data')

#...filtering currency columns....
currency = ['GBP/KES', 'USD/CAD', 'USD/CNY', 'USD/EUR', 'USD/GBP', 'USD/GHS', 'USD/INR','USD/JPY','USD/KES','USD/NGN', 'USD/RUB', 'USD/ZAR']
sel_currency = st.sidebar.multiselect('Currencies', currency,default=['USD/KES', 'USD/JPY'])
FX2 = FX[sel_currency]
#FX2

#....inserting year multiselect....
year = st.sidebar.multiselect('Select Year(s)', range(2008,2024), range(2008,2024))
#...filter multiple years....
FX3 = FX[FX['Date'].dt.year.isin(year)]
#FX3

#...dropping colums from FX2 to remain with date only.....
FX4 = FX3.drop(columns=['GBP/KES', 'USD/CAD', 'USD/CNY', 'USD/EUR', 'USD/GBP', 'USD/GHS', 'USD/INR','USD/JPY','USD/KES','USD/NGN', 'USD/RUB', 'USD/ZAR'])
#FX4

#...joining FX3 and FX4...
FX5 = FX4.join(FX2)
#FX5

#...inserting columns...
col1, col2 = st.columns([1,1])
col1.subheader('Complete Data')
col1.write('Data Dimesion:'  + str(FX.shape))
col2.subheader('Filtered Data')
col2.write('Data Dimesion:'  + str(FX5.shape))
col1.write(FX)
col2.write(FX5)

#....file download....FX
def filedownload(FX):
    csv = FX.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  
    href = f'<a href="data:file/csv;base64,{b64}">Download Complete Data</a>'
    return href
col1.write(filedownload(FX), unsafe_allow_html=True)


#....filedownload...FX5....
def filedownload(FX5):
    csv = FX5.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  
    href = f'<a href="data:file/csv;base64,{b64}">Download Filtered Data</a>'
    return href
col2.write(filedownload(FX5), unsafe_allow_html=True)

('---')

#filtered chart..
st.write('''
#### Line Chart Visualizing Filtered Values
''')
fig, ax = plt. subplots()
FX5.set_index('Date').plot(ax=ax)
ax.set_ylabel('Currencies')
ax.legend(loc='center right', bbox_to_anchor=(1.25, 0.5))
st.pyplot(fig)
('---')

#...computation analysis....
st.write('''
## Percentage Change Results
''')

#..daily percentage change of filtered data...
FX6 = FX5.set_index('Date')
FX6 = FX6.pct_change() * 100
#FX6


#..period change of filtered data....
FX7 = FX5.set_index('Date')
FX7 = FX7/FX7.iloc[0] - 1
FX7 = FX7 * 100
#FX7

#..inserting columns...
col1, col2 = st.columns([1,1])
col1.subheader('Daily % Change')
col2.subheader('Period % Change')
col1.write(FX6)
col2.write(FX7)

#..max and min computed values values....
FX8 = FX6.max()
FX9 = FX7.max()
FX10 = FX6.min()
FX11 = FX7.min()

('---')


#..correlation heatmap....
st.write('''
## Selected Option Will be Displayed Here
''')
corr = FX.corr(method='pearson')
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
#fig

from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title='Select an Option', 
        options=['Correlation Heatmap', 'Highest Daily Change', 'Highest Period Change', 'Lowest Daily Change', 'Lowest Period Change'],
        icons=['calculator', 'percent', 'arrow-up-circle-fill', 'arrow-down-square-fill', 'percent'],
        default_index=2
    )
if selected == 'Correlation Heatmap':
    st.write(fig)
if selected == 'Highest Daily Change':
    st.write(FX8)
if selected == 'Highest Period Change':
    st.write(FX9)
if selected == 'Lowest Daily Change':
    st.write(FX10)
if selected == 'Lowest Period Change':
    st.write(FX11)




