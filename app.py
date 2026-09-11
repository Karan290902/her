import streamlit as st

st.set_page_config(
    page_title="For My Bubuu ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==================================================
# CUSTOMIZE HERE
# ==================================================

GIRLFRIEND_NAME = "My Bubuu ❤️"
YOUR_NAME = "Karan ❤️"


# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff5f7, #ffe6ee, #fff0f5);
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

.title {
    text-align: center;
}

.stButton > button {
    width: 100%;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# LOVE LETTER
# ==================================================

st.markdown("# ❤️")

st.markdown(
    f"# Hey {GIRLFRIEND_NAME}"
)

st.caption("There are some things I want you to know... ❤️")

st.divider()


with st.container(border=True):

    st.markdown("## 💌 From My Heart To Yours")

    st.write(f"""
My love,

I don't know if I will ever be able to find the perfect words to explain
how much you truly mean to me.

Sometimes I feel like no matter how many times I say "I love you",
those three words are still not enough to describe what I feel for you.

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

I want you in my future.

I want to make more memories with you.

I want to experience life with you.

I want us to grow together, support each other, argue sometimes,
laugh again, understand each other and always find our way back
to one another.

When I think about the future, I don't just imagine success,
money or achievements.

I imagine having someone beside me who I love.

And honestly, when I think about that person,
I want that person to be you.

I want to build a life with you.

I want to create a home that feels like ours.

I want us to have our own little world.

A world filled with love, laughter, memories and happiness.

One day, I want us to look back at everything we went through
and smile because we chose to stay.

I want to build a family with you.

I want to experience all the beautiful parts of life with you.

The good days.

The difficult days.

The boring days.

The exciting days.

I don't just want to be there when life is perfect.

I want to be there for all of it.

For you.

I know I am not perfect.

I know I make mistakes.

And sometimes I may not express my feelings properly.

But please never doubt one thing.

My feelings for you are real.

I care about you.

I miss you.

I want you in my life.

And I genuinely want to build something beautiful with you.

I don't know exactly what the future will look like.

But if I am lucky enough to have you beside me,
then I know I will always have someone worth fighting for.

You are not just someone I love.

You are someone I want to choose.

Again and again.

Every day.

❤️

I love you more than I can explain.

I miss you more than you probably realise.

And I hope that one day,
we get to turn all the things we dream about
into our real life.

A life together.

A home together.

A family together.

You and me.

❤️

With all my love,

{YOUR_NAME}
""")

st.divider()

st.markdown("### ❤️ No matter where life takes us, you will always have a special place in my heart.")

st.caption("Made with love, just for you ❤️")
