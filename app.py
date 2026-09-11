import streamlit as st
import streamlit.components.v1 as components
import random

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="For My Love ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #fff0f5, #ffe4ec, #fce4ec);
        color: #4a1f2a;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Mobile-friendly main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 750px;
    }

    /* Title */
    .main-title {
        text-align: center;
        font-size: clamp(2.3rem, 9vw, 4.5rem);
        font-weight: 800;
        color: #e63964;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        font-size: clamp(1rem, 4vw, 1.4rem);
        color: #7d3146;
        margin-bottom: 2rem;
    }

    /* Love card */
    .love-card {
        background: rgba(255,255,255,0.85);
        padding: 25px;
        border-radius: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 30px rgba(230, 57, 100, 0.15);
        border: 1px solid rgba(230, 57, 100, 0.15);
    }

    .card-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #e63964;
        text-align: center;
        margin-bottom: 15px;
    }

    .love-text {
        font-size: 1.08rem;
        line-height: 1.8;
        text-align: center;
        color: #542633;
    }

    /* Reason cards */
    .reason {
        background: white;
        padding: 18px;
        margin: 12px 0;
        border-radius: 18px;
        box-shadow: 0 5px 18px rgba(0,0,0,0.06);
        font-size: 1rem;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 15px;
        padding: 14px;
        font-size: 1.05rem;
        font-weight: 700;
        border: none;
        background: linear-gradient(90deg, #e63964, #ff6b8a);
        color: white;
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 20px rgba(230, 57, 100, 0.3);
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #8b4a5c;
        font-size: 0.95rem;
    }

    /* Floating hearts */
    .heart {
        position: fixed;
        font-size: 25px;
        animation: float 7s linear infinite;
        z-index: -1;
        opacity: 0.5;
    }

    @keyframes float {
        0% {
            transform: translateY(100vh) rotate(0deg);
            opacity: 0;
        }
        20% {
            opacity: 0.6;
        }
        100% {
            transform: translateY(-10vh) rotate(360deg);
            opacity: 0;
        }
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# FLOATING HEARTS
# ---------------------------------------------------
hearts_html = """
<div class="heart" style="left:5%; animation-delay:0s;">❤️</div>
<div class="heart" style="left:15%; animation-delay:2s;">💖</div>
<div class="heart" style="left:30%; animation-delay:4s;">💕</div>
<div class="heart" style="left:45%; animation-delay:1s;">❤️</div>
<div class="heart" style="left:60%; animation-delay:3s;">💗</div>
<div class="heart" style="left:75%; animation-delay:5s;">💖</div>
<div class="heart" style="left:90%; animation-delay:2s;">💕</div>
"""

st.markdown(hearts_html, unsafe_allow_html=True)


# ---------------------------------------------------
# PERSONAL DETAILS
# EDIT THESE ❤️
# ---------------------------------------------------

GIRLFRIEND_NAME = "My Bubuu 
YOUR_NAME = "Karan❤️"

REASONS = [
    "❤️ Your smile makes even my worst days better.",
    "🥰 You make me feel loved in ways I never knew were possible.",
    "💖 Your presence brings peace to my heart.",
    "✨ Every memory with you becomes one of my favourite memories.",
    "🤍 I can be myself when I am with you.",
    "🌍 No matter where life takes us, you will always have a special place in my heart."
]


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    f"""
    <div class="main-title">
        Hey {GIRLFRIEND_NAME} ❤️
    </div>

    <div class="subtitle">
        I made something special just for you 🥰
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# OPENING MESSAGE
# ---------------------------------------------------

st.markdown(
    f"""
    <div class="love-card">
        <div class="card-title">💌 A Little Message For You</div>

        <div class="love-text">
            I don't think words will ever be enough to explain how much you mean to me.
            <br><br>

            You are not just someone I love. You are someone who has become
            a very important part of my life, my thoughts, my happiness, and my heart.
            <br><br>

            No matter how many times I say <b>"I love you"</b>,
            it will probably never fully explain how deeply I feel about you.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# LOVE BUTTON
# ---------------------------------------------------

st.markdown("### ❤️ Click the button if you want to know something")

if st.button("How much i love you? ❤️"):
    st.balloons()

    st.markdown(
        """
        <div class="love-card">
            <div class="card-title">The Answer ❤️</div>

            <div class="love-text">
                More than I can explain.<br>
                More than I can put into words.<br>
                More than yesterday.<br>
                And I hope to love you even more tomorrow. ❤️
                <br><br>
                If love could be measured, I still don't think there would be
                a number big enough to describe what I feel for you. 🥺❤️
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# REASONS
# ---------------------------------------------------

st.markdown(
    """
    <div class="love-card">
        <div class="card-title">❤️ Some Reasons Why I Love You</div>
    </div>
    """,
    unsafe_allow_html=True
)

for reason in REASONS:
    st.markdown(
        f"""
        <div class="reason">
            {reason}
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# MISS ME BUTTON
# ---------------------------------------------------

st.markdown("## 🥺 When You Miss Me")

if st.button("Click here when you miss me 🤍"):
    st.markdown(
        f"""
        <div class="love-card">
            <div class="card-title">Come Here 🤗❤️</div>

            <div class="love-text">
                If you are missing me right now, just remember this...
                <br><br>

                Somewhere, no matter what I am doing,
                there is a person thinking about you.
                <br><br>

                Me. ❤️
                <br><br>

                And I hope you know that you can always come to me,
                talk to me, laugh with me, cry with me,
                and share every little thing with me.
                <br><br>

                You never have to feel alone when you have me. 🤍
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# RANDOM LOVE MESSAGE
# ---------------------------------------------------

st.markdown("## 💕 A Message Just For You")

love_messages = [
    "You are my favourite notification. ❤️",
    "My day becomes better when I talk to you. 🥰",
    "I don't need a perfect life. I just want beautiful moments with you. ❤️",
    "You are one of the best things that has happened to me. 💖",
    "If I had to choose again, I would still choose you. ❤️",
    "You make ordinary moments feel special. ✨",
]

if st.button("Give me a surprise ❤️"):
    st.success(random.choice(love_messages))


# ---------------------------------------------------
# FINAL MESSAGE
# ---------------------------------------------------

st.markdown(
    f"""
    <div class="love-card">
        <div class="card-title">❤️ And Finally...</div>

        <div class="love-text">

            {GIRLFRIEND_NAME},
            <br><br>

            I may not always be perfect.
            I may make mistakes.
            Sometimes I may not know the right words to say.
            <br><br>

            But one thing I want you to always remember is this:
            <br><br>

            <b>I love you.</b>
            <br><br>

            I love your smile.
            I love your presence.
            I love the memories we create.
            And I love the person you are.
            <br><br>

            Thank you for being a part of my life.
            <br><br>

            No matter how complicated life gets,
            I hope we always find our way back to each other. ❤️
            <br><br>

            <b>Forever grateful for you.</b>
            <br><br>

            With all my love,
            <br>
            <b>{YOUR_NAME} ❤️</b>

        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Made with ❤️, love, and a little bit of coding.
        <br><br>
        ❤️ Forever Yours ❤️
    </div>
    """,
    unsafe_allow_html=True
)
