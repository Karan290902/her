import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="For My Ninii Baby ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# PERSONAL DETAILS ❤️
# ============================================================

GIRLFRIEND_NAME = "Shreya"
YOUR_NAME = "Karan"
NICKNAME = "Ninii Baby"


# ============================================================
# SESSION STATE
# ============================================================

if "show_letter" not in st.session_state:
    st.session_state.show_letter = False


# ============================================================
# ROMANTIC DESIGN
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Great+Vibes&family=Playfair+Display:wght@500;600;700&display=swap');


/* ============================================================
   BACKGROUND
============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(255, 185, 210, 0.65),
            transparent 32%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(255, 210, 225, 0.70),
            transparent 32%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(255, 190, 215, 0.50),
            transparent 40%
        ),
        linear-gradient(
            135deg,
            #fff9fa,
            #ffeef3,
            #fff8fa
        );
}


/* ============================================================
   HIDE STREAMLIT UI
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
   MAIN CONTAINER
============================================================ */

.block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* ============================================================
   NORMAL PARAGRAPHS
============================================================ */

[data-testid="stMarkdownContainer"] p {
    font-family: 'Cormorant Garamond', serif !important;
    color: #452631 !important;
    font-size: 23px !important;
    line-height: 1.5 !important;
    margin-bottom: 14px !important;
}


/* ============================================================
   HEADINGS
============================================================ */

h1 {
    font-family: 'Great Vibes', cursive !important;
    color: #c2185b !important;
    text-align: center !important;
    font-size: 70px !important;
    margin-bottom: 8px !important;
}


h2 {
    font-family: 'Playfair Display', serif !important;
    color: #c2185b !important;
    text-align: center !important;
    margin-top: 22px !important;
    margin-bottom: 16px !important;
}


h3 {
    font-family: 'Playfair Display', serif !important;
    color: #c2185b !important;
    text-align: center !important;
    margin-top: 28px !important;
    margin-bottom: 14px !important;
}


/* ============================================================
   LOVE LETTER CARD
============================================================ */

[data-testid="stVerticalBlockBorderWrapper"] {
    background:
        linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.96),
            rgba(255, 247, 250, 0.94)
        ) !important;

    border-radius: 28px !important;

    border: 1px solid rgba(194, 24, 91, 0.18) !important;

    box-shadow:
        0px 15px 45px rgba(194, 24, 91, 0.12) !important;

    padding: 12px !important;
}


/* ============================================================
   BUTTONS
============================================================ */

.stButton {
    display: flex !important;
    justify-content: center !important;
}


.stButton > button {
    min-height: 58px !important;

    border: none !important;
    border-radius: 50px !important;

    background:
        linear-gradient(
            135deg,
            #f45a91,
            #c2185b
        ) !important;

    color: white !important;

    font-family: 'Playfair Display', serif !important;

    font-size: 19px !important;

    font-weight: 600 !important;

    padding-left: 32px !important;
    padding-right: 32px !important;

    box-shadow:
        0px 10px 25px rgba(194, 24, 91, 0.25) !important;

    transition: 0.25s ease !important;
}


.stButton > button:hover {

    transform: translateY(-2px) !important;

    box-shadow:
        0px 15px 32px rgba(194, 24, 91, 0.35) !important;
}


/* ============================================================
   CAPTION
============================================================ */

[data-testid="stCaptionContainer"] {
    text-align: center !important;
    color: #8a5363 !important;
}


/* ============================================================
   POPUP / DIALOG
============================================================ */

/* Dialog background */

div[role="dialog"] {
    background:
        linear-gradient(
            135deg,
            #fffafd,
            #ffeef4
        ) !important;

    border-radius: 26px !important;

    border: 1px solid rgba(194, 24, 91, 0.18) !important;

    box-shadow:
        0px 20px 60px rgba(120, 30, 65, 0.20) !important;
}


/* Inner popup areas */

div[role="dialog"] > div,
div[role="dialog"] [data-testid="stVerticalBlock"],
div[role="dialog"] [data-testid="stDialog"] {
    background: transparent !important;
}


/* Center everything in popup */

div[role="dialog"] [data-testid="stMarkdownContainer"] {
    text-align: center !important;
}


/* Popup paragraphs */

div[role="dialog"] [data-testid="stMarkdownContainer"] p {

    color: #4a2632 !important;

    font-family:
        'Cormorant Garamond',
        serif !important;

    font-size: 22px !important;

    line-height: 1.5 !important;

    text-align: center !important;

    margin-bottom: 15px !important;
}


/* Popup headings */

div[role="dialog"] h1,
div[role="dialog"] h2,
div[role="dialog"] h3 {

    color: #c2185b !important;

    text-align: center !important;
}


/* Popup bold text */

div[role="dialog"] strong {

    color: #c2185b !important;
}


/* Popup button */

div[role="dialog"] .stButton {

    display: flex !important;

    justify-content: center !important;

    width: 100% !important;
}


div[role="dialog"] .stButton > button {

    width: auto !important;

    min-width: 260px !important;

    color: white !important;
}


/* ============================================================
   MOBILE
============================================================ */

@media (max-width: 600px) {

    .block-container {

        padding-left: 16px !important;

        padding-right: 16px !important;

        padding-top: 1.2rem !important;
    }


    h1 {

        font-size: 52px !important;
    }


    h2 {

        font-size: 26px !important;
    }


    h3 {

        font-size: 22px !important;
    }


    [data-testid="stMarkdownContainer"] p {

        font-size: 21px !important;

        line-height: 1.5 !important;
    }


    div[role="dialog"] [data-testid="stMarkdownContainer"] p {

        font-size: 20px !important;

        line-height: 1.5 !important;
    }


    div[role="dialog"] .stButton > button {

        min-width: 220px !important;

        font-size: 17px !important;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# POPUP
# ============================================================

@st.dialog("💌 A Little Something For You...")
def love_popup():

    st.markdown("## ❤️ My Ninii Baby ❤️")

    st.markdown("")

    st.markdown(
        "Before you open this, I just want you to know that this is not "
        "something copied from somewhere."
    )

    st.markdown(
        "**Yeh maine tumhare liye, apne dil se likha hai. ❤️**"
    )

    st.markdown(
        "Maybe I don't always say everything perfectly when we talk."
    )

    st.markdown(
        "Maybe kabhi kabhi main apni feelings properly express nahi kar pata."
    )

    st.markdown(
        "But everything inside this letter is something I genuinely feel "
        "for you, Baby."
    )

    st.markdown("")

    st.markdown("So take a deep breath... 🥺❤️")

    st.markdown("Read it slowly...")

    st.markdown("Aur bas itna yaad rakhna...")

    st.markdown("")

    st.markdown(
        f"### ❤️ Tum mere liye bahut special ho, {GIRLFRIEND_NAME}. ❤️"
    )

    st.markdown("")

    if st.button(
        "💗 Open My Heart, Baby 💗",
        key="open_heart_button"
    ):
        st.session_state.show_letter = True
        st.rerun()


# ============================================================
# WELCOME PAGE
# ============================================================

if not st.session_state.show_letter:

    st.write("")
    st.write("")

    st.markdown("# ❤️")

    st.markdown(f"# Hey, {GIRLFRIEND_NAME}...")

    st.markdown(f"## My {NICKNAME} ❤️")

    st.write("")
    st.write("")

    st.markdown("### I have something for you.")

    st.markdown("### Something I wanted to say properly...")

    st.markdown(
        "### Something that comes directly from my heart. ❤️"
    )

    st.write("")

    st.markdown("## ❤️ 💕 💗 💖 ❤️")

    st.write("")
    st.write("")

    if st.button(
        "💌 Tap Here, Baby... ❤️",
        key="welcome_button"
    ):
        love_popup()


# ============================================================
# LOVE LETTER
# ============================================================

else:

    st.markdown("# ❤️")

    st.markdown(
        f"# My {NICKNAME}, {GIRLFRIEND_NAME} ❤️"
    )

    st.caption(
        "A little piece of my heart, written only for you, Baby ❤️"
    )

    st.divider()


    with st.container(border=True):

        st.markdown(
            "## 💌 My Baby, Read This Slowly"
        )


        st.markdown(
            """
Baby,

I honestly don't know how to explain everything that is in my heart. There are so many things I want to tell you, and sometimes I feel like words are just not enough.

But today I just want to write everything that I feel.

Not in a perfect way. Not with perfect words.

Bas jaise mere dil mein hai, waise hi. ❤️
"""
        )


        st.markdown(
            "### ❤️ Ninii Baby, I Love You So Much"
        )


        st.markdown(
            """
Shreya, I don't think you truly understand how important you have become to me.

You are not just someone I love, Baby. You have become a part of my life, a part of my thoughts, a part of my happiness and a part of my everyday life.

Kabhi kabhi mere din mein kuch hota hai aur sabse pehle mujhe tumhe batane ka mann karta hai. Sometimes I see something funny and immediately think about sending it to you.

Sometimes I am doing absolutely nothing, and still somehow you are in my mind.

Aur honestly, Baby... mujhe tumhara meri life mein hona bahut pasand hai.

I genuinely love having you in my life. ❤️
"""
        )


        st.markdown(
            "### 🥺 Baby, I Miss You"
        )


        st.markdown(
            """
I miss you so much, Shreya.

Kabhi kabhi mujhe khud nahi pata hota ki main tumhe itna kyun miss kar raha hoon. I miss talking to you, I miss hearing from you, I miss your presence and I miss our conversations.

I even miss those small moments that probably don't seem important to anyone else but mean so much to me.

Aur kabhi kabhi, Ninii Baby, baat karne ke baad bhi tumhari yaad aati hai.

Because when someone becomes this important to your heart, their absence is something you feel.

Aur Baby, main tumhari kami feel karta hoon.

There are moments when I just wish you were here.

Kaash tum mere paas hoti.

Nothing complicated.

Bas tum aur main. ❤️
"""
        )


        st.markdown(
            "### 💕 I Want You In My Future"
        )


        st.markdown(
            """
Baby, I don't just want you for today. I don't just want beautiful conversations and beautiful memories.

Main nahi chahta ki hum sirf ek temporary chapter bane ek dusre ki life mein.

I want you in my life.

I want you in my future.

I want to make more memories with you, laugh with you, have silly arguments with you and then make up again.

I want us to grow together and understand each other more as time passes.

Aur Baby, life chahe kitni bhi difficult ho, main chahta hoon ki hum ek dusre ka saath na chhode.

Because, Ninii Baby... you are someone I genuinely want to choose.

Again and again. ❤️
"""
        )


        st.markdown(
            "### 🏡 When I Think About My Life..."
        )


        st.markdown(
            """
When I think about my future, Shreya, I don't only think about my career, money or success.

Jab main apni life imagine karta hoon, main imagine karta hoon ki mere paas koi ho.

Someone I can come home to.

Someone I can tell about my day.

Someone I can celebrate with when life is good and someone I can hold onto when life becomes difficult.

Someone who feels like home.

Aur honestly, Baby...

Jab main us person ke baare mein sochta hoon, I want it to be you. ❤️
"""
        )


        st.markdown(
            "### ❤️ I Want To Build A Life With You"
        )


        st.markdown(
            """
I dream about having our own little world, Baby.

Our own home.

Our own memories.

Our own small routines.

Waking up together. Coming back home after a long day. Eating together. Laughing about silly things.

Annoying each other.

Aur kabhi kabhi argue karke phir ek dusre ko mana lena. ❤️

Mujhe koi perfect life nahi chahiye, Baby.

I just want a real life, with real problems, real happiness and real memories.

Aur tum mere saath.
"""
        )


        st.markdown(
            "### 👨‍👩‍👧‍👦 I Want A Family With You"
        )


        st.markdown(
            """
This is one of the deepest things in my heart, Baby.

One day, I want to build a family with you.

Humara apna chhota sa family.

Our own home filled with love and laughter.

Our own memories.

Our own traditions.

I want us to grow older together.

Aur ek din jab hum peeche mudke dekhein, toh hum un saare moments ko yaad karein.

The beautiful moments.

The difficult moments.

The times we laughed.

The times we cried.

The times we had to be strong.

Aur phir ek dusre ko dekh ke bolein...

Hum ruke nahi.

Humne ek dusre ko choose kiya.

Humne saath nibhaya.

We made it. ❤️

Because when I imagine a family and a life that feels like mine...

Tum us picture mein hoti ho.
"""
        )


        st.markdown(
            "### 🤍 Baby, I Know I Am Not Perfect"
        )


        st.markdown(
            """
I know I am not perfect, Shreya.

Main mistakes karta hoon. Kabhi kabhi main galat bol deta hoon.

Sometimes I don't understand things immediately, aur kabhi kabhi main apni feelings properly express nahi kar pata.

Shayad kabhi kabhi main tumhe properly dikha bhi nahi pata ki tum mere liye kitni important ho.

But Baby, please never doubt this.

**What I feel for you is real.**

Main genuinely tumhari care karta hoon.

Main genuinely tumhe miss karta hoon.

Main genuinely tumhe apni life mein chahta hoon.

Aur main genuinely tumhare saath kuch beautiful build karna chahta hoon. ❤️
"""
        )


        st.markdown(
            "### ❤️ Ek Baat Main Dil Se Kehna Chahta Hoon..."
        )


        st.markdown(
            """
Baby, main jaanta hoon ki humare beech fights hongi. Disagreements honge.

Kabhi kabhi hum ek dusre se naraz honge.

Kabhi tum mujhe samajh nahi paogi, aur kabhi main tumhe samajhne mein galti karunga.

Kabhi hum dono gusse mein kuch aisa bol denge jo humein nahi bolna chahiye tha.

But I want you to remember something.

**A fight between us does not mean that our love is over.**

A disagreement does not mean that our relationship is doomed.

Narazgi ka matlab yeh nahi hai ki hum ek dusre ko khona chahte hain.

Hum dono perfect nahi hain, Baby.

Aur shayad humara relationship bhi kabhi perfect nahi hoga.

But perfect hona zaroori bhi nahi hai.

**Saath rehna zaroori hai. ❤️**

Ek dusre ko samajhne ki koshish karna zaroori hai.

Gusse ke baad bhi ek dusre ka haath nahi chhodna zaroori hai.
"""
        )


        st.markdown(
            "### 🤝 Difficult Doesn't Mean The End"
        )


        st.markdown(
            """
Because Baby, I don't want us to give up on each other just because we are having a difficult moment.

Ek difficult day doesn't mean we have a difficult life.

Ek fight doesn't mean our relationship is broken.

Ek disagreement doesn't mean that our love has failed.

Main nahi chahta ki har fight ke baad hum sochein...

Maybe this is the end.

Instead, I want us to think...

**Hum dono milke isse solve karenge.**

Because for me, Baby, it should never be you versus me.

**It should always be you and me versus the problem. ❤️**

I want us to talk.

I want us to listen.

Aur phir chahe kitna bhi gussa ho...

I want us to find our way back to each other.
"""
        )


        st.markdown(
            "### ❤️ I See Myself With You Till My Last Breath"
        )


        st.markdown(
            """
Because Shreya, main tumhe sirf aaj ke liye nahi dekh raha.

When I think about my life ahead, I see you.

When I think about growing older, I see you.

When I think about having a home, I see you.

When I think about having a family, I see you.

And honestly, Baby...

**I see myself with you till my last breath. ❤️**

Maybe life will not always go according to our plans.

Maybe there will be difficult phases.

Maybe there will be days when loving each other feels harder than usual.

But even then...

I want to choose you.

Again and again.

And again.

Ninii Baby, whenever we fight, please don't think that I stopped loving you.

Whenever we disagree, please don't think that I want to leave you.

**Difficult doesn't mean impossible. ❤️**
"""
        )


        st.markdown(
            "## ❤️ Shreya, I Love You"
        )


        st.markdown(
            f"""
Baby, I don't know exactly what the future will look like.

I don't know what challenges life will bring us.

But I know one thing.

**I want you to be a part of my life.**

I want more than just memories with you.

I want more than just conversations.

I want a life with you.

A home with you.

A family with you.

A future with you.

I want to wake up one day and realise that all the things we once dreamed about are now our real life.

You and me.

Humara ghar.

Humari family.

Humari memories.

Humari life. ❤️

Aur Baby, I know I don't always say everything perfectly.

But please remember this.

**I love you.**

So much more than I am able to explain.

**I miss you.**

More than you probably realise.

Aur Ninii Baby...

No matter how difficult things become...

**I don't want a life without you in it.**

Main chahta hoon ki hum dono har phase se saath guzrein.

Aaj.

Kal.

Aur jitna bhi time humein zindagi saath de.

Because Baby, mere dil mein tumhare liye sirf aaj ka pyaar nahi hai.

Main tumhe apni zindagi ke har kal mein dekhna chahta hoon.

Till my last breath...

**I want it to be you, Shreya. ❤️**

You.

My Baby.

My Shreya.

My Ninii Baby. ❤️

Forever yours,

## {YOUR_NAME} ❤️
"""
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown("## ❤️ Always Yours")

st.caption(
    "Made with all my heart, just for my Ninii Baby 💕"
)
