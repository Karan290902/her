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


# ============================================================
# ROMANTIC DESIGN
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Great+Vibes&family=Playfair+Display:wght@500;600;700&display=swap');


/* BACKGROUND */

.stApp {
    background:
        radial-gradient(circle at 10% 5%, rgba(255, 190, 210, 0.75), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(255, 210, 225, 0.75), transparent 30%),
        radial-gradient(circle at 50% 100%, rgba(255, 200, 215, 0.65), transparent 35%),
        linear-gradient(135deg, #fff8fa, #ffe9ef, #fff6f9);
}


/* HIDE STREAMLIT UI */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* MAIN CONTAINER */

.block-container {
    max-width: 780px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* PARAGRAPHS */

[data-testid="stMarkdownContainer"] p {
    font-family: 'Cormorant Garamond', serif !important;
    color: #4b2632 !important;
    font-size: 22px !important;
    line-height: 1.55 !important;
    margin-bottom: 15px !important;
}


/* HEADINGS */

h1 {
    font-family: 'Great Vibes', cursive !important;
    color: #c2185b !important;
    text-align: center !important;
    font-size: 68px !important;
    margin-bottom: 8px !important;
}

h2 {
    font-family: 'Playfair Display', serif !important;
    color: #c2185b !important;
    text-align: center !important;
    margin-bottom: 20px !important;
}

h3 {
    font-family: 'Playfair Display', serif !important;
    color: #d6336c !important;
    text-align: center !important;
    margin-top: 28px !important;
    margin-bottom: 14px !important;
}


/* LOVE LETTER CARD */

[data-testid="stVerticalBlockBorderWrapper"] {
    background:
        linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.96),
            rgba(255, 247, 250, 0.92)
        );

    border-radius: 28px !important;

    border: 1px solid rgba(214, 51, 108, 0.18) !important;

    box-shadow:
        0px 12px 40px rgba(190, 50, 95, 0.12) !important;

    padding: 12px;
}


/* CAPTION */

[data-testid="stCaptionContainer"] {
    text-align: center !important;
    color: #8f4a61 !important;
}


/* DIVIDER */

hr {
    margin-top: 28px !important;
    margin-bottom: 28px !important;
}


/* MOBILE */

@media (max-width: 600px) {

    .block-container {
        padding-left: 16px;
        padding-right: 16px;
        padding-top: 1.2rem;
    }

    h1 {
        font-size: 52px !important;
    }

    h2 {
        font-size: 25px !important;
    }

    h3 {
        font-size: 21px !important;
    }

    [data-testid="stMarkdownContainer"] p {
        font-size: 20px !important;
        line-height: 1.55 !important;
        margin-bottom: 13px !important;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("# ❤️")

st.markdown(f"# My Ninii Baby, {GIRLFRIEND_NAME} ❤️")

st.caption("A little piece of my heart, written only for you, Baby ❤️")

st.divider()


# ============================================================
# LOVE LETTER
# ============================================================

with st.container(border=True):

    st.markdown("## 💌 My Baby, Read This Slowly")

    st.markdown("""
Baby,

I honestly don't know how to explain everything that is in my heart. There are so many things I want to tell you, Shreya, and sometimes I feel like words are just not enough.

But today I just want to write everything that I feel. Not in a perfect way, not with perfect words... bas jaise mere dil mein hai, waise hi.
""")


    st.markdown("### ❤️ Ninii Baby, I Love You So Much")

    st.markdown("""
Shreya, I don't think you truly understand how important you have become to me. You are not just someone I love, Baby. You have become a part of my life, a part of my thoughts, a part of my happiness and a part of my everyday life.

Kabhi kabhi mere din mein kuch hota hai aur sabse pehle mujhe aapko batane ka mann karta hai. Sometimes I see something funny and immediately think about sending it to you, my Ninii Baby. Sometimes I am doing absolutely nothing, and still somehow you are in my mind.

Aur honestly, Baby... mujhe aapka meri life mein hona bahut pasand hai. I love having you in my life.
""")


    st.markdown("### 🥺 Baby, I Miss You")

    st.markdown("""
I miss you so much, Shreya. Kabhi kabhi mujhe khud nahi pata hota ki main aapko itna kyun miss kar raha hoon. I miss talking to you, I miss hearing from you, I miss your presence and I miss our conversations.

I even miss those small moments that probably don't seem important to anyone else but mean so much to me. Aur kabhi kabhi, Ninii Baby, baat karne ke baad bhi aapki yaad aati hai.

Because when someone becomes this important to your heart, their absence is something you feel. Aur Baby, main aapki kami feel karta hoon.

There are moments when I just wish you were here. Kaash aap mere paas hoti. I wish I could sit with you, talk to you, laugh with you, hold you... aur bas aap mere paas hote.

Nothing complicated. Bas aap aur main.
""")


    st.markdown("### 💕 Shreya, I Want You In My Future")

    st.markdown("""
Baby, I don't just want you for today. I don't just want beautiful conversations and beautiful memories. Main nahi chahta ki hum sirf ek temporary chapter bane ek dusre ki life mein.

I want you in my life. I want you in my future. I want to make more memories with you, laugh with you, have silly arguments with you and then make up again. I want to see you happy and be there when you need someone.

I want us to grow together and understand each other more as time passes. Aur Baby, life chahe kitni bhi difficult ho, main chahta hoon ki hum ek dusre ka saath na chhode.

Because, Ninii Baby... you are someone I genuinely want to choose. Again and again.
""")


    st.markdown("### 🏡 When I Think About My Life, Baby...")

    st.markdown("""
When I think about my future, Shreya, I don't only think about my career, money or success. Of course those things are important, but they are not everything.

Jab main apni life imagine karta hoon, main imagine karta hoon ki mere paas koi ho. Someone I can come home to, someone I can tell about my day, someone I can celebrate with when life is good and someone I can hold onto when life becomes difficult.

Someone who feels like home.

Aur honestly, Baby... jab main us person ke baare mein sochta hoon, I want it to be you.
""")


    st.markdown("### ❤️ Ninii Baby, I Want To Build A Life With You")

    st.markdown("""
I dream about having our own little world, Baby. Our own home, our own memories and our own small routines.

Waking up together. Coming back home after a long day. Eating together. Laughing about silly things. Annoying each other. Aur kabhi kabhi argue karke phir ek dusre ko mana lena.

Mujhe koi perfect life nahi chahiye, Baby. I don't want some imaginary perfect life. I just want a real life, with real problems, real happiness and real memories.

Aur aap mere saath.
""")


    st.markdown("### 👨‍👩‍👧‍👦 Shreya, I Want A Family With You")

    st.markdown("""
This is one of the deepest things in my heart, Baby. One day, I want to build a family with you. Humara apna chhota sa family, our own home filled with love and laughter, our own memories and our own traditions.

I want us to grow older together. Aur ek din jab hum peeche mudke dekhein, toh hum un saare moments ko yaad karein—the beautiful moments, the difficult moments, the times we laughed, the times we cried and the times we had to be strong.

Aur phir ek dusre ko dekh ke bolein... hum ruke nahi. Humne ek dusre ko choose kiya. Humne saath nibhaya.

We made it.

That thought genuinely makes me happy, Ninii Baby. Because when I imagine a family and a life that feels like mine... aap us picture mein hoti ho.
""")


    st.markdown("### 🤍 Baby, I Know I Am Not Perfect")

    st.markdown("""
I know I am not perfect, Shreya. Main mistakes karta hoon. Kabhi kabhi main galat bol deta hoon. Sometimes I don't understand things immediately, aur kabhi kabhi main apni feelings properly express nahi kar pata.

Shayad kabhi kabhi main aapko properly dikha bhi nahi pata ki aap mere liye kitni important ho.

But Baby, please never doubt this.

What I feel for you is real.

Main genuinely aapki care karta hoon. Main genuinely aapko miss karta hoon. Main genuinely aapko apni life mein chahta hoon.

Aur main genuinely aapke saath kuch beautiful build karna chahta hoon.
""")


    st.markdown("### ❤️ Baby, Ek Baat Main Dil Se Kehna Chahta Hoon...")

    st.markdown("""
Baby, main jaanta hoon ki humare beech fights hongi. Disagreements honge. Kabhi kabhi hum ek dusre se naraz honge. Kabhi aap mujhe samajh nahi paogi, aur kabhi main aapko samajhne mein galti karunga.

Kabhi hum dono gusse mein kuch aisa bol denge jo humein nahi bolna chahiye tha.

Aur sach bolu, Baby... shayad kabhi kabhi aisa lagega ki hum dono ek dusre ke against khade hain.

But I want you to remember something.

**A fight between us does not mean that our love is over.**

A disagreement does not mean that our relationship is doomed.

Narazgi ka matlab yeh nahi hai ki hum ek dusre ko khona chahte hain.

Hum dono perfect nahi hain, Baby. Aur shayad humara relationship bhi kabhi perfect nahi hoga. But perfect hona zaroori bhi nahi hai.

**Saath rehna zaroori hai.**

Ek dusre ko samajhne ki koshish karna zaroori hai. Gusse ke baad bhi ek dusre ka haath nahi chhodna zaroori hai.
""")


    st.markdown("### 🤝 Ninii Baby, Difficult Doesn't Mean The End")

    st.markdown("""
Because Baby, I don't want us to give up on each other just because we are having a difficult moment.

Ek difficult day doesn't mean we have a difficult life. Ek fight doesn't mean our relationship is broken. Ek disagreement doesn't mean that our love has failed.

Main nahi chahta ki har fight ke baad hum sochein, "Maybe this is the end."

Instead, I want us to think...

**Hum dono milke isse solve karenge.**

Because for me, Baby, it should never be you versus me.

**It should always be you and me versus the problem. ❤️**

Main nahi chahta ki ek misunderstanding humare beech itni badi deewar ban jaaye ki hum ek dusre ko hi bhool jaayein.

I want us to talk. I want us to listen. I want us to calm down.

Aur phir chahe kitna bhi gussa ho... I want us to find our way back to each other.
""")


    st.markdown("### ❤️ Shreya, I See Myself With You Till My Last Breath")

    st.markdown("""
Because Shreya, main aapko sirf aaj ke liye nahi dekh raha.

When I think about my life ahead, I see you.

When I think about growing older, I see you.

When I think about having a home, I see you.

When I think about having a family, I see you.

And honestly, Baby...

**I see myself with you till my last breath. ❤️**

Maybe life will not always go according to our plans. Maybe there will be difficult phases. Maybe there will be days when loving each other feels harder than usual.

But even then...

I want to choose you.

Again and again.

And again.

Ninii Baby, whenever we fight, please don't think that I stopped loving you. Whenever we disagree, please don't think that I want to leave you.

Difficult doesn't mean impossible.
""")


    st.markdown("## ❤️ Shreya, I Love You")

    st.markdown(f"""
Baby, I don't know exactly what the future will look like. I don't know what challenges life will bring us.

But I know one thing.

I want you to be a part of my life.

I want more than just memories with you. I want more than just conversations.

I want a life with you.

A home with you.

A family with you.

A future with you.

I want to wake up one day and realise that all the things we once dreamed about are now our real life.

You and me.

Humara ghar.

Humari family.

Humari memories.

Humari life.

Aur Baby, I know I don't always say everything perfectly. But please remember this.

**I love you.**

So much more than I am able to explain.

**I miss you.**

More than you probably realise.

Aur Ninii Baby, no matter how difficult things become... I don't want a life without you in it.

Main chahta hoon ki hum dono har phase se saath guzrein. Aaj. Kal. Aur jitna bhi time humein zindagi saath de.

Because Baby, mere dil mein aapke liye sirf aaj ka pyaar nahi hai.

Main aapko apni zindagi ke har kal mein dekhna chahta hoon.

Till my last breath...

**I want it to be you, Shreya. ❤️**

You.

My Baby.

My Shreya.

My Ninii Baby. ❤️

Forever yours,

## {YOUR_NAME} ❤️
""")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown("### ❤️ Always Yours")

st.caption("Made with all my heart, just for my Ninii Baby 💕")
