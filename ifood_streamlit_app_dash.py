
import streamlit as st
import pandas    as pd
import numpy     as np
import plotly.graph_objects as go
#from datetime import datetime, time
import plotly.express as px 
import plotly.figure_factory as ff


# ------------------------------------------
# settings
# ------------------------------------------
st.set_page_config( layout='wide' )


# ------------------------------------------
# Helper Functions
# ------------------------------------------
@st.cache( allow_output_mutation=True )
def get_data(path):
    df = pd.read_csv(path)

    return df

#st.write(df.head())
#f_days = st.sidebar.multiselect( 'Enter days of week', df.day_of_week.unique() ) 
def filter_seg(df):
    f_seg = st.sidebar.multiselect( 'Enter Segment', df.Segment.unique() ) 

    if f_seg == []:
        df = df.copy()
    else:
        df= df.loc[df['Segment'].isin(f_seg)] 
        
    return df




st.header('Ifood Dash')  


def response(df):
    
    df_1= df.groupby('cohort')['Response'].sum().reset_index()
    fig = px.line(df_1, x="cohort", y="Response", title='Tendencia de aceitação da campanha por cohort')
    
    st.plotly_chart( fig, use_container_width=True )

    return None

def edu(df):
    
    edu = df.groupby(['Education', 'ResponseTxt'])['Response'].count().reset_index().sort_values(ascending = True, by = 'Response')

    import plotly.express as px
    fig = px.bar(edu, x='Education', y='Response', color='ResponseTxt')
    

    st.plotly_chart( fig, use_container_width=True )
    return None
    
    

def marital(df):
    
    marital = df.groupby(['Marital_Status', 'ResponseTxt'])['Response'].count().reset_index().sort_values(ascending = True, by = 'Response')
    
    
    fig = px.bar(marital, x='Marital_Status', y='Response', color='ResponseTxt'
                            )
    
    st.plotly_chart( fig, use_container_width=True )
    return None

def purchase(df):
    purchase = df.groupby(['BiggerPurchases', 'ResponseTxt'])['Response'].count().reset_index().sort_values(ascending = True, by = 'Response')

    fig = px.bar(purchase, x='BiggerPurchases', y='Response', color='ResponseTxt')
    
    st.plotly_chart( fig, use_container_width=True)
    return None


if __name__ == "__main__":
    # ETL
    path = 'ml_project1_data_treated.csv'
      
    # load data
    df = get_data(path)
    
    
    # transform data
    df = filter_seg(df)
    
    edu(df)

    marital(df)

    purchase(df)

    response(df)







    


