import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="For My Bubuu ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# ❤️ CUSTOMIZE HERE
# ============================================================

GIRLFRIEND_NAME = "My Bubuu"
YOUR_NAME = "Karan"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ============================================================
   IMPORT ROMANTIC FONTS
============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Great+Vibes&family=Playfair+Display:wght@500;600;700&display=swap');


/* ============================================================
   PAGE BACKGROUND
============================================================ */

.stApp {

    background:
        radial-gradient(circle at 10% 10%, rgba(255, 190, 210, 0.8), transparent 28%),
        radial-gradient(circle at 90% 20%, rgba(255, 210, 225, 0.8), transparent 30%),
        radial-gradient(circle at 50% 100%, rgba(255, 200, 215, 0.6), transparent 35%),
        linear-gradient(135deg, #fff7f9, #ffe9ef, #fff5f8);

}


/* ============================================================
   HIDE STREAMLIT ELEMENTS
============================================================ */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ============================================================
   MAIN PAGE WIDTH
============================================================ */

.block-container {

    max-width: 780px;

    padding-top: 2rem;

    padding-bottom: 4rem;

}


/* ============================================================
   MAIN TEXT
============================================================ */

[data-testid="stMarkdownContainer"] p {

    font-family: 'Cormorant Garamond', serif !important;

    color: #4b2632 !important;

    font-size: 23px !important;

    line-height: 1.7 !important;

}


/* ============================================================
   MAIN HEADINGS
============================================================ */

h1 {

    font-family: 'Great Vibes', cursive !important;

    color: #c2185b !important;

    font-size: 68px !important;

    text-align: center !important;

    margin-bottom: 5px !important;

}


h2 {

    font-family: 'Playfair Display', serif !important;

    color: #c2185b !important;

    text-align: center !important;

}


h3 {

    font-family: 'Playfair Display', serif !important;

    color: #d6336c !important;

    text-align: center !important;

}


/* ============================================================
   LOVE LETTER CARD
============================================================ */

[data-testid="stVerticalBlockBorderWrapper"] {

    background:

        linear-gradient(
            135deg,
            rgba(255,255,255,0.96),
            rgba(255,248,250,0.90)
        );

    border:

        1px solid rgba(214, 51, 108, 0.18) !important;

    border-radius: 30px !important;

    box-shadow:

        0px 15px 45px rgba(190, 50, 95, 0.13) !important;

    padding: 12px;

}


/* ============================================================
   DIVIDER
============================================================ */

hr {

    border: none !important;

    height: 1px !important;

    background:

        linear-gradient(
            to right,
            transparent,
            #e89ab3,
            transparent
        ) !important;

    margin-top: 35px !important;

    margin-bottom: 35px !important;

}


/* ============================================================
   CAPTION
============================================================ */

[data-testid="stCaptionContainer"] {

    text-align: center !important;

    color: #8f4a61 !important;

    font-family: 'Playfair Display', serif !important;

    font-size: 16px !important;

}


/* ============================================================
   MOBILE DESIGN
============================================================ */

@media (max-width: 600px) {

    .block-container {

        padding-left: 18px;

        padding-right: 18px;

        padding-top: 1.5rem;

    }


    h1 {

        font-size: 54px !important;

    }


    h2 {

        font-size: 27px !important;

    }


    [data-testid="stMarkdownContainer"] p {

        font-size: 20px !important;

        line-height: 1.65 !important;

    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO SECTION
# ============================================================

st.markdown("# ❤️")

st.markdown(f"# {GIRLFRIEND_NAME}")

st.caption("A little piece of my heart, written only for you ❤️")

st.divider()


# ============================================================
# LOVE LETTER
# ============================================================

with st.container(border=True):

    st.markdown("## 💌 My Love, Read This Slowly")

    st.markdown("""

My love,

I don't know if there will ever be enough words in this world to explain what you truly mean to me.

Sometimes I sit and think about you, about us, about all the little moments we have shared, and I realise something.

You have become so much more than just someone I love.

You have become someone who lives in my thoughts.

Someone whose happiness matters to me.

Someone I want to talk to when something good happens.

Someone I want to run to when life becomes difficult.

And someone I miss even when we have just spoken.

""")

    st.markdown("### ❤️ I Miss You More Than You Know")

    st.markdown("""

I miss you.

I miss talking to you.

I miss hearing from you.

I miss your presence.

I miss the feeling of having you close to me.

Sometimes I don't even know exactly what I miss the most.

Maybe it's your voice.

Maybe it's our conversations.

Maybe it's the comfort of knowing that you are there.

Or maybe it's simply you.

Because when someone becomes important to your heart, their absence is something you feel.

And I feel yours.

""")

    st.markdown("### 💕 I Don't Just Want You For Today")

    st.markdown("""

I want you to be a part of my life.

Not just for today.

Not just for a few beautiful moments.

Not just until things become difficult.

I want you in my future.

I want more memories with you.

I want more laughs with you.

I want more silly conversations.

I want to learn more about you as time passes.

I want us to grow together.

I want us to support each other.

And even when life becomes complicated, I want us to always find our way back to each other.

""")

    st.markdown("### 🏡 When I Think About My Future...")

    st.markdown("""

When I think about the future, I don't only imagine success, money or achievements.

I imagine peace.

I imagine coming home after a long day and having someone I love beside me.

I imagine sharing my happiness and my problems with one person.

I imagine building something that belongs to both of us.

And honestly...

When I imagine that person beside me,

I want that person to be you.

""")

    st.markdown("### 💍 I Want To Build A Life With You")

    st.markdown("""

I want us to create our own little world.

A home that feels like ours.

A place filled with laughter, love, memories and comfort.

I want to experience the beautiful parts of life with you.

The exciting days.

The boring days.

The difficult days.

The days when everything goes perfectly.

And the days when nothing does.

Because I don't just want to be there when life is beautiful.

I want to be there for all of it.

For you.

""")

    st.markdown("### 👨‍👩‍👧‍👦 I Dream About Having A Family With You")

    st.markdown("""

One day, I hope we get to build a family together.

Our own little family.

Our own home.

Our own memories.

Our own traditions.

I want us to grow older together and one day look back at everything we went through.

The good moments.

The difficult moments.

The times we laughed until we couldn't breathe.

The times we had to be strong.

And I hope we can smile and say...

We stayed.

We chose each other.

We made it.

""")

    st.markdown("### 🤍 I Know I Am Not Perfect")

    st.markdown("""

I know I make mistakes.

I know sometimes I don't understand things immediately.

Sometimes I may not express what I feel properly.

Sometimes I may fail to say the right thing.

But please never doubt this.

My feelings for you are real.

I care about you.

I miss you.

I want you.

And I genuinely want you to be a part of my life.

""")

    st.markdown("### ❤️ If I Had To Choose Again...")

    st.markdown("""

I would still choose you.

Again.

And again.

And again.

Not because everything is always perfect.

But because when I look at you, I see someone I genuinely want to try for.

Someone worth understanding.

Someone worth choosing.

Someone worth building a future with.

""")

    st.markdown("## ❤️ I Love You")

    st.markdown(f"""

I love you more than I know how to explain.

I miss you more than you probably realise.

And I want more than just memories with you.

I want a life with you.

A home with you.

A family with you.

A future with you.

You and me.

Through the beautiful days.

Through the difficult days.

Through everything.

And if life gives me the chance,

I hope one day all the things I dream about...

are things I get to live with you.

Forever.

❤️

With all my love,

## {YOUR_NAME} ❤️

""")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown("### ❤️ Always Yours")

st.caption("Made with all my heart, just for you 💕")
