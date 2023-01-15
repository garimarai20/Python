#  to run, do not click the play button , but instead , in the terminal , type:
#  -> cd Mini_project

#  -> streamlit run mini.py 




import streamlit as st 
import pandas as pd 
import plotly.express as px
import numpy as np 

st.set_page_config(
    page_title="Recruitment Analysis",
    page_icon="📊",
    layout="wide"
)

@st.cache
def load_data():
    return pd.read_csv('Placement_Data_Full_Class.csv')


st.title(" Recruitment Analysis ")
st.subheader(" Campus Recruitment Analysis of college students using their Secondary school percentage, Highschool Percentage and specialization, gender, and status of placement whether they are placed or not. ")
st.write("Below is the data frame used for analysis and visualization")
df=load_data()
st.dataframe(df,use_container_width=True)

st.line_chart(df,y='status',x='ssc_p',use_container_width=True)
st.bar_chart(df,y= "salary",x ="hsc_s", use_container_width=True)
st.balloons()
color=st.color_picker('Pick a color','#00f900')
st.write('THE CURRENT COLOR IS ',color)
st.bar_chart(df, y='degree_p',x='status',use_container_width=True)


st.sidebar.header("Select Option")
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



st.subheader(" The following points are obtained after the analyis of the dataframe\n")
st.write("\n ->  A majority of the college students were Male. ")
st.image('gender.png')
st.write(" \n-> The men who had their degree type as SCIENCE have the highest salary.")
st.image('degreetypevssalary.png')
st.write("\n -> Most people took commerce as their High school Degree type")
st.image('hsc.png')
st.write( "\n -> Below the Histogram of High School Percentage is shown ")
st.image('hist_hsc.png')
st.write(" \n -> As a result of this recruitment analysis large number of students were placed.")
st.image('placed.png')