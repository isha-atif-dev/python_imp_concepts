import streamlit as st

st.set_page_config(page_title="My App",page_icon="🐍",layout="wide")
st.markdown(
    """
<div class="hero">
    <div class="main-title">🐍 Python Code Reviewer</div>
</div>
""",
    unsafe_allow_html=True,
)

st.title("My app")
st.write("Hello world")

if st.button("click me!"):
    st.write("button clicked")

st.text_input("write here!")


# col1, col2 = st.columns([5.2, 1.3])
# st.tabs(["Bugs", "Complexity"])

st.markdown("Hello")

st.markdown("# Title")
st.markdown("**Bold text**")


st.markdown(
    ""
    """
# My App
**This is bold**
Here is some `code`
---
"""
)
st.markdown("""
# This is bold
Here is some `code`
""")

st.markdown(
    """
    <div style = "color : red ; font-size : 20px;">
            Styled text</div>
""",
    unsafe_allow_html=True,
)

st.markdown("""
    <div style = "color : purple ; font-size : 50px">
            Hello world!</div>
""",unsafe_allow_html=True)

