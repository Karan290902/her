import streamlit as st
import random

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
# PERSONALIZE HERE ❤️
# ==================================================

GIRLFRIEND_NAME = "My Bubuu ❤️"
YOUR_NAME = "Karan ❤️"


REASONS = [
    "Your smile makes even my worst days better.",
    "You make ordinary moments feel special.",
    "I love how comfortable I feel with you.",
    "You are the person I want to share everything with.",
    "Even our silly conversations mean so much to me.",
    "You have become such a beautiful part of my life."
]


LOVE_MESSAGES = [
    "You are my favourite notification. ❤️",
    "I still smile when I see your name on my phone. 🥰",
    "You are my favourite person to annoy. 😂❤️",
    "If I had to choose again, I would still choose you. ❤️",
    "My day feels better when I talk to you. 💕",
    "You make my ordinary days feel special. ✨",
    "You are one of my favourite things about my life. ❤️"
]


# ==================================================
# CUSTOM CSS
# ONLY FOR PAGE AND BUTTON DESIGN
# ==================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #fff5f8,
        #ffe9f0,
        #fff0f5
    );
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.block-container {
    max-width: 700px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.stButton > button {
    width: 100%;
    border-radius: 18px;
    padding: 14px;
    font-size: 17px;
    font-weight: 700;
    border: none;
    background: linear-gradient(
        135deg,
        #e63970,
        #ff6b95
    );
    color: white;
}

.stButton > button:hover {
    transform: scale(1.02);
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HERO SECTION
# ==================================================

st.markdown("# ❤️")

st.markdown(
    f"# Hey {GIRLFRIEND_NAME}"
)

st.caption("I made this little place just for you 🥰")

st.divider()


# ==================================================
# OPENING MESSAGE
# ==================================================

with st.container(border=True):

    st.markdown("## 💌 A Little Message For You")

    st.write(
        """
I don't think words will ever be enough to explain how much you mean to me.

You are not just someone I love. You have become such an important part
of my life, my happiness, my thoughts and my heart.

No matter how many times I say "I love you", I don't think those words
will ever fully explain how deeply I feel about you. ❤️
"""
    )


# ==================================================
# HOW MUCH I LOVE YOU
# ==================================================

st.markdown("## ❤️ Something You Should Know")

if st.button("How much do I love you? ❤️"):

    st.balloons()

    with st.container(border=True):

        st.markdown("## More Than You Know ❤️")

        st.write(
            """
More than I can explain.

More than I can put into words.

More than yesterday.

And hopefully even more tomorrow. ❤️

If love could be measured, I still don't think there would be a number
big enough to describe what I feel for you. 🥺❤️
"""
        )


# ==================================================
# REASONS WHY I LOVE YOU
# ==================================================

st.markdown("## 🥰 Reasons Why I Love You")

for number, reason in enumerate(REASONS, start=1):

    with st.container(border=True):

        st.markdown(f"### 💗 {number}")

        st.write(reason)


# ==================================================
# WHEN YOU MISS ME
# ==================================================

st.markdown("## 🥺 When You Miss Me")

if st.button("Click here when you miss me 🤍"):

    with st.container(border=True):

        st.markdown("## Come Here 🤗❤️")

        st.write(
            """
If you are missing me right now, I want you to remember one thing.

No matter where I am or what I am doing, there is always someone
thinking about you.

Me. ❤️

You can always come to me, talk to me, laugh with me,
cry with me and share everything with me.

You never have to feel alone when you have me. 🤍
"""
        )


# ==================================================
# SURPRISE MESSAGE
# ==================================================

st.markdown("## 💕 A Little Surprise")

if st.button("Click for a message from me 💌"):

    with st.container(border=True):

        message = random.choice(LOVE_MESSAGES)

        st.markdown("### ❤️ For You")

        st.success(message)


# ==================================================
# FINAL LOVE LETTER
# ==================================================

st.markdown("## 💗 And Finally...")

with st.container(border=True):

    st.markdown(f"### {GIRLFRIEND_NAME}")

    st.write(
        """
I know I am not perfect.

I know I make mistakes.

And sometimes I may not always know the right words to say.

But please never doubt this.
"""
    )

    st.markdown("## I love you. ❤️")

    st.write(
        """
I love your smile.

I love your presence.

I love our memories.

And I love the person you are.

Thank you for being a part of my life.

No matter how complicated life gets, I hope we always find
our way back to each other. ❤️

Forever grateful for you.
"""
    )

    st.markdown(f"### With all my love,")
    st.markdown(f"## {YOUR_NAME} ❤️")


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.markdown("### Made with ❤️ just for you")

st.caption("💕 Forever Yours 💕")
