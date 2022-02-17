import streamlit as st


from tools import authentication


st.set_page_config(
    page_title='My App',
    layout='wide',
    page_icon=':rocket:'
)

# CSS
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)








if __name__ == '__main__':
    st.sidebar.image('./images/download.png', output_format='png')

    #authentication
    authentication()
  