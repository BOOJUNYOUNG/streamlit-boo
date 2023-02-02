import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def  plotting_demo():
    
    #uploaded_file = st.file_uploader("Choose a file")

    #money=pd.read_csv(uploaded_file)
    money = pd.read_csv("money_data7.csv")

    option = st.selectbox(
        'How would you like to choice year ?',
        ('2020', '2021', '2022'))

    option2 = int(option)

    st.write('You selected:', option)

    money = money[:] [money['A_YEAR']== option2]
    
    global  aa          
    
    aa = money

    fig, ax = plt.subplots(2,2, figsize=(12,8))

    plt.subplot(221)
    plt.plot(  list( money['A_MONTH'] ), list( money['A_RATE'] ), color='red' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('America rate')


    plt.subplot(222)
    plt.plot(  list( money['A_MONTH'] ), list( money['K_RATE'] ), color='blue' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('Korea rate')

    plt.subplot(223)
    plt.plot(  list( money['A_MONTH'] ), list( money['KOSPI'] ), color='green' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('Kospi Rate')

    plt.subplot(224)
    plt.plot(  list( money['A_MONTH'] ), list( money['HOUSE_PRICE'] ), color='yellow' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('House Price')

    st.pyplot(fig)
    #st.dataframe(money)
       
        



def bar_chart():

    url = " https://sports.news.naver.com/kbaseball/record/index?category=kbo&year= "

    years = ['2015', '2016','2017', '2018', '2019', '2020', '2021', '2022' ]

    baseball = pd.DataFrame([]) 

    for i in years: 
        df1 = pd.read_html(url+i)[0]
        df1['년도'] =  i 
        baseball = pd.concat([baseball, df1], axis=0)
        
        baseball.팀.replace({'두산':'Doosan','삼성':'Samsung','한화': 'Hanwha','롯데':'Lotte','넥센':'Nexen','키움':'Kiwoom'}, inplace=True)
    
    option = st.selectbox(
        'How would you like to choice year ?',
        ('2015', '2016','2017', '2018', '2019', '2020', '2021', '2022'))

    st.write('You selected:', option)

    baseball_graph = baseball[baseball.년도==option]
    
    global bb
    bb = baseball_graph
    
    x = baseball_graph.팀
    y = baseball_graph.승률
    
    fig, ax = plt.subplots(figsize=(12,8))

    colors = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7' ,'C8', 'C9', 'C10' ]
    plt.bar(x, y, color= colors ) 

    for i, v in enumerate( y ):
        plt.text(i-0.4, v+0.01, v)

    plt.title( "year korea baseball winrate data", position=(0.5,1.1))
    st.pyplot(fig)    

 

elif select_language =='야구 순위와 승률 빠르게 파악하기':
    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

    with tab1:
        tab1.subheader("A tab with a chart")
        bar_chart()
        
    with tab2:
        tab2.subheader("A tab with the data")
        st.dataframe(bb)
