import streamlit as st
from tools import *

import pandas as pd



def display_admin():    
    
        
        # with st.expander("Create a new user"):
        #     create_user_tool()
        
        # with st.expander("Display the list of users"):
        #     read_users_tool()

        # with st.expander("Update a user"):
        #     update_user_tool()

        # with st.expander("Delete a user"):
        #     delete_user_tool()

    st.header('list of users')
    rows = read_users_tool()
    df = pd.DataFrame(rows,columns=('ID','LOGIN','PASSWORD','IS ADMIN' ))
    df.iloc[:, 3:]= df.iloc[:, 3:].astype(bool)
    st.table(df)
    
    

    col = st.columns(3)
    if col[0].button("create a new user" , key =  "create"):
        create_user_tool()

    if col[1].button("update a user" , key =  "update"):
        update_user_tool()

    if col[2].button("delete a user" , key =  "delete"):
        delete_user_tool()

