st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff5f7, #ffe6ee, #fff0f5);
}

/* Make all normal text dark and readable */
p, div, span, li {
    color: #3d1f2b !important;
}

/* Streamlit text */
.stMarkdown,
.stMarkdown p,
.stText,
[data-testid="stMarkdownContainer"] p {
    color: #3d1f2b !important;
}

/* Main headings */
h1, h2, h3 {
    color: #d6336c !important;
}

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    max-width: 750px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

</style>
""", unsafe_allow_html=True)
