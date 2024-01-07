import streamlit as st

st.write("<center>Insira abaixo os dados.</center>", unsafe_allow_html=True )
formulario="""
        <script type="text/javascript" src="https://form.jotform.com/jsform/233385865863067"></script>
        """

st.markdown(formulario, unsafe_allow_html=True)