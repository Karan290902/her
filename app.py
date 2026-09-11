import streamlit as st

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="For My Bubuu ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ==================================================
# CUSTOMIZE HERE ❤️
# ==================================================

GIRLFRIEND_NAME = "My Bubuu ❤️"
YOUR_NAME = "Karan ❤️"


# ==================================================
# CUSTOM DESIGN
# ==================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff5f7, #ffe6ee, #fff0f5);
}

/* Hide Streamlit menu and branding */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Main page */

.block-container {
    max-width: 750px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Make all paragraph text dark and readable */

[data-testid="stMarkdownContainer"] p {
    color: #3d1f2b !important;
    font-size: 18px !important;
    line-height: 1.8 !important;
}

/* Headings */

h1 {
    color: #d6336c !important;
    text-align: center;
}

h2 {
    color: #d6336c !important;
}

h3 {
    color: #b52a5a !important;
}

/* Card */

[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: rgba(255, 255, 255, 0.92);
    border-radius: 20px;
    border-color: rgba(214, 51, 108, 0.2);
    box-shadow: 0 8px 25px rgba(214, 51, 108, 0.08);
}

/* Caption */

[data-testid="stCaptionContainer"] {
    text-align: center;
}

/* Mobile */

@media (max-width: 600px) {

    .block-container {
        padding-left: 15px;
        padding-right: 15px;
        padding-top: 1.5rem;
    }

    [data-testid="stMarkdownContainer"] p {
        font-size: 17px !important;
        line-height: 1.75 !important;
    }
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

st.markdown("# ❤️")

st.markdown(f"# Hey {GIRLFRIEND_NAME}")

st.caption("There are some things I want you to know... ❤️")

st.divider()


# ==================================================
# LOVE LETTER
# ==================================================

with st.container(border=True):

    st.markdown("## 💌 From My Heart To Yours")

    st.markdown(f"""

My love,

I don't know if I will ever be able to find the perfect words to explain how much you truly mean to me.

Sometimes I feel like no matter how many times I say **I love you**, those three words are still not enough to describe what I feel for you.

You have become such an important part of my life.

You are someone I think about during my day.

You are someone I want to share my happiness with.

You are someone I want to talk to when something happens.

And you are someone I miss even when we have just spoken.

I miss you more than I can explain.

I miss talking to you.

I miss hearing from you.

I miss your presence.

And sometimes, I simply miss having you close to me.

But more than just missing you, I want you.

I want you to be a part of my life.

Not just for today.

Not just for a few beautiful moments.

**I want you in my future.**

I want to make more memories with you.

I want to experience life with you.

I want us to grow together, support each other, laugh together, understand each other, and always find our way back to one another.

When I think about the future, I don't just imagine success, money or achievements.

I imagine having someone beside me who I love.

And honestly, when I think about that person, **I want that person to be you.**

I want to build a life with you.

I want to create a home that feels like ours.

I want us to have our own little world.

A world filled with love, laughter, memories and happiness.

One day, I want us to look back at everything we went through and smile because we chose to stay.

**I want to build a family with you.**

I want to experience all the beautiful parts of life with you.

The good days.

The difficult days.

The boring days.

The exciting days.

I don't just want to be there when life is perfect.

**I want to be there for all of it.**

For you.

I know I am not perfect.

I know I make mistakes.

And sometimes I may not express my feelings properly.

But please never doubt one thing.

**My feelings for you are real.**

I care about you.

I miss you.

I want you in my life.

And I genuinely want to build something beautiful with you.

I don't know exactly what the future will look like.

But if I am lucky enough to have you beside me, then I know I will always have someone worth fighting for.

You are not just someone I love.

You are someone I want to choose.

Again and again.

Every day.

❤️

**I love you more than I can explain.**

**I miss you more than you probably realise.**

And I hope that one day, we get to turn all the things we dream about into our real life.

A life together.

A home together.

A family together.

**You and me. ❤️**

With all my love,

## {YOUR_NAME}

""")


# ==================================================
# FINAL MESSAGE
# ==================================================

st.divider()

st.markdown("### ❤️ Made with all my love, just for you")

st.markdown("### 💕 Forever Yours 💕")
