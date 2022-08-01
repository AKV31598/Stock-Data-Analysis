import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import requests as r

#Animation
import json
import requests
from streamlit_lottie import st_lottie


st.markdown("<h1 style='text-align: center; color: white;'>WELCOME TO STOCK BOAT</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>STOCK DATA WEB APP </h3>", unsafe_allow_html=True)
st.markdown('<h5 style="text-align: left;background-color: transparent; padding-left: 5px; padding-bottom: 10px;">Enter to Search on web</h5>', unsafe_allow_html=True)

# for search bar
query = st.text_input('', help='Enter the search string and hit Enter/Return')
query = query.replace(" ", "+") #replacing the spaces in query result with +

if query: #Activates the code below on hitting Enter/Return in the search textbox
    try:#Exception handling 
        req = r.get(f"https://www.bing.com/search?q={query}",
                    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"})
        result_str = '<html><table style="border: none;">' #Initializing the HTML code for displaying search results
        
        if req.status_code == 200: #Status code 200 indicates a successful request
            bs = BeautifulSoup(req.content, features="html.parser") #converting the content/text returned by request to a BeautifulSoup object
            search_result = bs.find_all("li", class_="b_algo") #'b_algo' is the class of the list object which represents a single result
            search_result = [str(i).replace("<strong>","") for i in search_result] #removing the <strong> tag
            search_result = [str(i).replace("</strong>","") for i in search_result] #removing the </strong> tag
            result_df = pd.DataFrame() #Initializing the data frame that stores the results
            
            for n,i in enumerate(search_result): #iterating through the search results
                individual_search_result = BeautifulSoup(i, features="html.parser") #converting individual search result into a BeautifulSoup object
                h2 = individual_search_result.find('h2') #Finding the title of the individual search result
                href = h2.find('a').get('href') #title's URL of the individual search result
                cite = f'{href[:50]}...' if len(href) >= 50 else href # cite with first 20 chars of the URL
                url_txt = h2.find('a').text #title's text of the individual search result
                #In a few cases few individual search results doesn't have a description. In such cases the description would be blank
                description = "" if individual_search_result.find('p') is None else individual_search_result.find('p').text
                #Appending the result data frame after processing each individual search result
                result_df = result_df.append(pd.DataFrame({"Title": url_txt, "URL": href, "Description": description}, index=[n]))
                count_str = f'<b style="font-size:20px;">Bing Search returned {len(result_df)} results</b>'
                
                
                ########################################################
                ######### HTML code to display search results ##########
                result_str += f'<tr style="border: none;"><h3><a href="{href}" target="_blank">{url_txt}</a></h3></tr>'+\
                f'<tr style="border: none;"><strong style="color:green;">{cite}</strong></tr>'+\
                f'<tr style="border: none;">{description}</tr>'+\
                f'<tr style="border: none;"><td style="border: none;"></td></tr>'
            result_str += '</table></html>'
            
        #if the status code of the request isn't 200, then an error message is displayed along with an empty data frame        
        else:
            result_df = pd.DataFrame({"Title": "", "URL": "", "Description": ""}, index=[0])
            result_str = '<html></html>'
            count_str = '<b style="font-size:20px;">Looks like an error!!</b>'
            
    #if an exception is raised, then an error message is displayed along with an empty data frame
    except:
        result_df = pd.DataFrame({"Title": "", "URL": "", "Description": ""}, index=[0])
        result_str = '<html></html>'
        count_str = '<b style="font-size:20px;">Looks like an error!!</b>'
    
    st.markdown(f'{count_str}', unsafe_allow_html=True)
    st.markdown(f'{result_str}', unsafe_allow_html=True)
    st.markdown('<h3>Data Frame of the above search result</h3>', unsafe_allow_html=True)
    st.dataframe(result_df)

#@st cache for animation and loaded data
@st.cache
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.subheader('This is Streamlit Web Application for Stock Market Data Analysis')
lottie_ani1 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ihtte3uv.json")

st_lottie(
    lottie_ani1,
    speed=1,
    reverse=False,
    quality="high",
    height=500,
    width=1400,
    key=None,
)
st.header('Provides Graphical Representations of Stocks Insights')
lottie_ani2 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_qtwdoohk.json")

st_lottie(
    lottie_ani2,
    speed=1,
    reverse=False,
    quality="low",
    height=500,
    width=1400,
    key=None,
)

st.markdown("<h2 style='text-align: right; color: yellow;'>Select your assets to view the insights in the market data</h2>", unsafe_allow_html=True)
lottie_ani3 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ocib98vu.json")
st_lottie(
    lottie_ani3,
    speed=1,
    reverse=False,
    quality="high",
    height=500,
    width=1400,
    key=None,
)

st.markdown("<h2 style='text-align: right; color: violet;'>Compare Multiple Stock and graphs</h2>", unsafe_allow_html=True)
lottie_ani4 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_la18dnfn.json")
st_lottie(
    lottie_ani4,
    speed=1,
    reverse=False,
    quality="low",
    height=900,
    width=1400,
    key=None,
)
st.markdown("<h6 style='text-align: left; color: skyblue;'>© STOCK-BOAT</h6>", unsafe_allow_html=True)
######################################