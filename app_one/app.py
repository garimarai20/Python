
#  to run, do not click the play button , but instead , in the terminal , type:
#  -> cd app_one
#  -> streamlit run app.py 



import streamlit as st 
import pandas as pd 
import plotly.express as px
import numpy as np 

st.set_page_config(
    page_title="App One",
    page_icon="😊",
    layout="wide"
)

@st.cache
def load_data():
    return pd.read_csv('cps_85_wages.csv') # not the best way to read in streamlit

#   df= pd.read_csv('cps_85_wages.csv') # not the best way to read in streamlit


st.title(" Streamlit Data One ")
st.subheader("Very Easy data analytics in python ")
df=load_data()
st.dataframe(df,use_container_width=True)

st.bar_chart(df,x= "WAGE", y="EDUCATION", use_container_width=True)


st.sidebar.header("Select Optio")
if st.sidebar.checkbox("Show Pivot Table Summary"):
    st.subheader("Pivot Table Summary")
    c1, c2 = st.columns(2)
    categorical_cols= df.select_dtypes(exclude=np.number).columns
    numeric_cols = df.select_dtypes(include=np.number).columns
    index_col = c1.selectbox("Pivot Index", options=categorical_cols)
    values_col= c2.multiselect("Pivot Values",options=numeric_cols)
    func=c1.selectbox("Pivot Function", options=["mean","Sum","count","min","max","std"])
    pivot_df= df.pivot_table(index=index_col, values=values_col,aggfunc=func)
    c2.dataframe(pivot_df,use_container_width=True)
    for col in values_col:
        fig=px.pie(pivot_df,values=col,names=pivot_df.index)
        st.plotly_chart(fig)



