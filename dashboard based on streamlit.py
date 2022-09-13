import time
from tkinter.tix import COLUMN  # to simulate a real time data, time loop
import plotly.figure_factory as ff
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import altair as alt
import matplotlib.pyplot as plt
import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)
df = pd.read_excel('data.xlsx',index_col ="NO")
st.set_page_config(
    page_title="Data Science Assigment Dashboard [Abdurhman Abrar]",
    page_icon="✅",
    layout="wide",
)
st.title("Data Science Assigment Dashboard [Abdurhman Abrar]")
st.subheader('Data is from Ministry of Peace Project called Young Volunteers Management System')
category_based_on_sex = df.groupby(['sex'])['sex'].count()
x = df.groupby(['sex'])['sex'].count()
totalMale = x['Male']
totalFemale = x['Female']
total = totalMale+totalFemale
malePercent = totalMale/total
femalePercent = totalFemale/total
male, female = st.columns(2)
male.metric("Total Male Percentage", str(round(malePercent*100,2))+"%")
female.metric("Total Female Percentage",  str(round(femalePercent*100,2))+"%")
male_to_female_prop = df.groupby(by=["sex"]).count()[['University']].rename(columns={"University":"Count"}).reset_index()

male_to_female_pie_fig = male_to_female_prop.iplot(kind="pie", labels="sex", values="Count",
                         title="Male to Female Proportion using PIE chart",
                         asFigure=True,
                        hole=0.4)

male_to_female_pie_fig



#worknig area



simple_crosstab = pd.crosstab(df['Region'], df['University'])   
st.bar_chart(simple_crosstab)

head_col,tail_col = st.columns(2)

with head_col:
    st.markdown("### Data Head " )
    st.dataframe(df.head())

with tail_col:
    st.markdown("### Data Tail " )
    st.dataframe(df.tail())

head_col,tail_col = st.columns(2)

with head_col:
    st.markdown("### University Participation " )
    # print(df.groupby(['University'])['University'].count())
    st.bar_chart(data=df.groupby(['University'])['University'].count().reset_index(name='Universities quota'),x='University')
    


with tail_col:
    st.markdown("### Data Tail " )
    st.dataframe(df.tail())
st.header("Basic data")


st.header("Region based outputs")
region_filter = st.selectbox("Select the Region", pd.unique(df["Region"]))
dfnew = df[df["Region"] == region_filter]
col1,col2 = st.columns(2)

with col1:
    st.markdown("### Volunteers from "+region_filter )
    st.dataframe(df.loc[df['Region'] == region_filter])

with col2:
    st.header("Volunteers ")
    region_crosstab = pd.crosstab(dfnew['Region'], dfnew['University'])   
    st.bar_chart(region_crosstab)

