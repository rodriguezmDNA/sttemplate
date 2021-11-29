### Streamlit
from random import shuffle
#from awsUtils import *
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt

##########################################
tooltip_msg = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit
in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''

##########################################
st.sidebar.title('Sidebar')
st.sidebar.markdown('---')

## Selector
st.sidebar.markdown(':speaker: Normal selector :point_down:')
volume = st.sidebar.slider('Turn it up to 11:',0,11,value=4,step=1)

st.sidebar.markdown('---')
## Range selector
minValue,maxValue = st.sidebar.slider('Select values for a range',0,100,value=(25,75),step=5, help=tooltip_msg) #Input widget with tooltip 
st.sidebar.markdown(':point_up: Change the lower and higher bounds')
st.sidebar.write(f'Difference in range is `{maxValue-minValue}`')


st.sidebar.markdown('---')
## Show options of disease

selectboxoptions = list(range(0,5))
optionselection = st.sidebar.selectbox(
     f'Pick a number (n={len(selectboxoptions)})',
     [''] + selectboxoptions ) #Make No Filter default



#### Styling functions
stHTML = lambda string: st.markdown(string, unsafe_allow_html=True)
textCenter = lambda text: f"<p style='text-align:center;'> {text} </p>"
center_string = lambda x: f"<p style='text-align:center;'> {x} </p>"

#############################################
html_string = "<h1 style='text-align:center;'> This title is HTML </h1>"
stHTML(html_string)
st.markdown('## Streamlit supports markdown')
st.markdown('### markdown + emojis = :rocket: :moon:')
st.markdown('---')

#############################################
#Input widget with tooltip 
st.text_area('Here will be text-area', help=tooltip_msg)
#############################################

#Chart with tooltip 
st.markdown('<style>#vg-tooltip-element{z-index: 1000051}</style>', unsafe_allow_html=True)#hack to make tooltip visible in full-screen mode
demo_df = pd.DataFrame({
    'timestamp': [pd.Timestamp(2020, 1, i) for i in range(1, 31)],
    'value': np.random.randn(30).cumsum()
})
base = alt.Chart(demo_df).encode(
    x='timestamp:T',
    y='value:Q',
    tooltip=['value', 'timestamp']
)
line = base.mark_line()
points = base.mark_point(filled=True, size=40)
chart = (line + points).interactive()
st.altair_chart(chart, use_container_width=True)


#############################################
#Table with tooltip 
# df = pd.DataFrame(data=[[0, 1], [2, 3]])
# ttips = pd.DataFrame( data=[["Min", ""], [np.nan, "Max"]], columns=df.columns, index=df.index)
# #st.dataframe(df)
# s = df.style.set_tooltips(ttips).to_html()
# stHTML(s)

### Some space
stHTML('<br>')
stHTML('<br>')

#############################################

showS3 = st.checkbox('Read data from S3')
s3Path = 's3://foodome-datalake-development-us-east-1/datafreeze/source_data/datafreeze/20210721/datafreeze_20210721.tsv'
s3data = read_s3(s3Path)

if showS3:    
    st.write(f'Showing DataFreeze from `{s3Path}`')
    st.dataframe(s3data)
else:
    st.write('Data hidden')


st.markdown('---')


#############################################

st.markdown('## Turn the volume up! :speaker:')

## Flow control
if volume == 11:
    var='Noice!!!' 
    st.write(f'Volume is `{volume}`, noice!') #backticks to highligh variables

stHTML('<br>')
stHTML('<br>')
st.markdown('## What number am I thinking of?')
if optionselection != '':
    answer = list(set(selectboxoptions) - set([optionselection]))
    shuffle(answer)
    st.write(f"Oops, the correct answer is of `{answer[0]}`. Try again!")
else:
    st.write('Pick a number :point_left:')

#############################################
stHTML('<br>')
stHTML('<br>')
st.markdown('---')
st.write('Using HTML and some CSS to center the logo:')
logoDir = 'https://1jj36121ulnl3yz5ue21q04x-wpengine.netdna-ssl.com/wp-content/uploads/2020/05/Foodome_Logo.png'
components.html(f"<img src='{logoDir}' style='width:25%;margin-left: auto;margin-right: auto;display: block'>")

