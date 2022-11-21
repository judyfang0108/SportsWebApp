import streamlit as st
from nba import *
from nfl import *
# Sidebar options
option = st.sidebar.selectbox('Navigation',
                              ["Home",
                               "NBA",
                               "NFL"
                               ])

st.set_option('deprecation.showPyplotGlobalUse', False)
if option == 'Home':
    st.write(
        """
				## Project Description
				This is a complete text analysis tool developed by Prakhar Rathi. It's built in with multiple features which can be accessed
				from the left side bar.
			"""
    )

# Word Cloud Feature
elif option == "NBA":
    nba()
elif option == "NFL":
    nfl()
    