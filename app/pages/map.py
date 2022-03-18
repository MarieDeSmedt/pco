import streamlit as st
import pandas as pd
import numpy as np
from tools import *

        
def display_map():

    df = pd.read_csv("csv/drive_coor.csv")

    with st.expander("choisir les drives a afficher"):
        drives_selected_list = st.multiselect("Drives", options = df["siteLabel"], help = "Choisir les drives à observer sur la carte",)
        if len(drives_selected_list)>0:
            df_choosen_drives = df[df["siteLabel"].isin(drives_selected_list)]
            st.dataframe(df_choosen_drives.head())
         
    
    if len(drives_selected_list)>0:
       
        submitted = st.button("Visualiser sur la carte")

        if submitted:
            show_map(df_choosen_drives)