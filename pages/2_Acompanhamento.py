import streamlit as st

def embed_jotform_alternative():
    html_code = """
    <div class="jotform-embed" style="min-height: 1px;" data-id="23339603950805806" data-type="interactive" data-iframesource="www.jotform.com"></div>
    <script>(function(doc, id){var scripts=doc.getElementsByTagName("script")[0]; if (!doc.getElementById(id)){var script=doc.createElement("script"); script.async=1; script.id=id; script.src="https://cdn.jotfor.ms/s/umd/latest/for-report-embed.js"; scripts.parentNode.insertBefore(script, scripts);}})(document, "jotform-async");</script>
    """
    st.components.v1.html(html_code, height=1000)

# Example usage
st.title("Acompanhamento das respostas")
embed_jotform_alternative()