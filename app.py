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

if "show_story" not in st.session_state:
    st.session_state.show_story = False

if "current_slide" not in st.session_state:
    st.session_state.current_slide = 0


# ============================================================
# STORY CONTENT
# ============================================================

slides = [

    {
        "title": "💌 My Baby, Read This Slowly",
        "content": """
Baby,

I honestly don't know how to explain everything that is in my heart.

There are so many things I want to tell you, and sometimes I feel like words are just not enough.

But today I just want to write everything that I feel.

Not in a perfect way.

Not with perfect words.

Bas jaise mere dil mein hai, waise hi. ❤️
"""
    },


    {
        "title": "❤️ Ninii Baby, I Love You So Much",
        "content": """
Shreya, I don't think you truly understand how important you have become to me.

You are not just someone I love, Baby.

You have become a part of my life, a part of my thoughts, a part of my happiness and a part of my everyday life.

Kabhi kabhi mere din mein kuch hota hai aur sabse pehle mujhe aapko batane ka mann karta hai.

Sometimes I see something funny and immediately think about sending it to you.

Sometimes I am doing absolutely nothing, and still somehow you are in my mind.

Aur honestly, Baby...

Mujhe aapka meri life mein hona bahut pasand hai.

I genuinely love having you in my life. ❤️
"""
    },


    {
        "title": "🥺 Baby, I Miss You",
        "content": """
I miss you so much, Shreya.

Kabhi kabhi mujhe khud nahi pata hota ki main aapko itna kyun miss kar raha hoon.

I miss talking to you.

I miss hearing from you.

I miss your presence.

I miss our conversations.

I even miss those small moments that probably don't seem important to anyone else but mean so much to me.

Aur kabhi kabhi, Ninii Baby...

Baat karne ke baad bhi aapki yaad aati hai.

Because when someone becomes this important to your heart, their absence is something you feel.

Aur Baby...

Main aapki kami feel karta hoon.

There are moments when I just wish you were here.

Kaash aap mere paas hote.

Nothing complicated.

Bas aap aur main. ❤️
"""
    },


    {
        "title": "💕 I Want You In My Future",
        "content": """
Baby, I don't just want you for today.

I don't just want beautiful conversations and beautiful memories.

Main nahi chahta ki hum sirf ek temporary chapter bane ek dusre ki life mein.

I want you in my life.

I want you in my future.

I want to make more memories with you.

Laugh with you.

Have silly arguments with you.

And then make up again.

I want us to grow together and understand each other more as time passes.

Aur Baby...

Life chahe kitni bhi difficult ho, main chahta hoon ki hum ek dusre ka saath na chhode.

Because, Ninii Baby...

You are someone I genuinely want to choose.

Again and again. ❤️
"""
    },


    {
        "title": "🏡 When I Think About My Life...",
        "content": """
When I think about my future, Shreya, I don't only think about my career, money or success.

Jab main apni life imagine karta hoon...

Main imagine karta hoon ki mere paas koi ho.

Someone I can come home to.

Someone I can tell about my day.

Someone I can celebrate with when life is good.

And someone I can hold onto when life becomes difficult.

Someone who feels like home.

Aur honestly, Baby...

Jab main us person ke baare mein sochta hoon...

I want it to be you. ❤️
"""
    },


    {
        "title": "❤️ I Want To Build A Life With You",
        "content": """
I dream about having our own little world, Baby.

Our own home.

Our own memories.

Our own small routines.

Waking up together.

Coming back home after a long day.

Eating together.

Laughing about silly things.

Annoying each other.

Aur kabhi kabhi argue karke phir ek dusre ko mana lena. ❤️

Mujhe koi perfect life nahi chahiye, Baby.

I just want a real life.

With real problems.

Real happiness.

Real memories.

Aur aap mere saath. ❤️
"""
    },


    {
        "title": "👨‍👩‍👧‍👦 I Want A Family With You",
        "content": """
This is one of the deepest things in my heart, Baby.

One day, I want to build a family with you.

Humara apna chhota sa family.

Our own home filled with love and laughter.

Our own memories.

Our own traditions.

I want us to grow older together.

Aur ek din jab hum peeche mudke dekhein...

Toh hum un saare moments ko yaad karein.

The beautiful moments.

The difficult moments.

The times we laughed.

The times we cried.

And the times we had to be strong.

Aur phir ek dusre ko dekh ke bolein...

Hum ruke nahi.

Humne ek dusre ko choose kiya.

Humne saath nibhaya.

We made it. ❤️

Because when I imagine a family and a life that feels like mine...

Aap us picture mein hote ho.
"""
    },


    {
        "title": "🤍 Baby, I Know I Am Not Perfect",
        "content": """
I know I am not perfect, Shreya.

Main mistakes karta hoon.

Kabhi kabhi main galat bol deta hoon.

Sometimes I don't understand things immediately.

Aur kabhi kabhi main apni feelings properly express nahi kar pata.

Shayad kabhi kabhi main aapko properly dikha bhi nahi pata ki aap mere liye kitni important ho.

But Baby...

Please never doubt this.

What I feel for you is real.

Main genuinely aapki care karta hoon.

Main genuinely aapko miss karta hoon.

Main genuinely aapko apni life mein chahta hoon.

Aur main genuinely aapke saath kuch beautiful build karna chahta hoon. ❤️
"""
    },


    {
        "title": "❤️ Ek Baat Main Dil Se Kehna Chahta Hoon...",
        "content": """
Baby, main jaanta hoon ki humare beech fights hongi.

Disagreements honge.

Kabhi kabhi hum ek dusre se naraz honge.

Kabhi aap mujhe samajh nahi paogi.

Aur kabhi main aapko samajhne mein galti karunga.

But I want you to remember something.

A fight between us does not mean that our love is over.

A disagreement does not mean that our relationship is doomed.

Narazgi ka matlab yeh nahi hai ki hum ek dusre ko khona chahte hain.

Hum dono perfect nahi hain, Baby.

Aur shayad humara relationship bhi kabhi perfect nahi hoga.

But perfect hona zaroori bhi nahi hai.

Saath rehna zaroori hai. ❤️

Ek dusre ko samajhne ki koshish karna zaroori hai.

Gusse ke baad bhi ek dusre ka haath nahi chhodna zaroori hai.
"""
    },


    {
        "title": "🤝 Difficult Doesn't Mean The End",
        "content": """
Because Baby, I don't want us to give up on each other just because we are having a difficult moment.

Ek difficult day doesn't mean we have a difficult life.

Ek fight doesn't mean our relationship is broken.

Ek disagreement doesn't mean that our love has failed.

Main nahi chahta ki har fight ke baad hum sochein...

Maybe this is the end.

Instead, I want us to think...

Hum dono milke isse solve karenge.

Because for me, Baby...

It should never be you versus me.

It should always be you and me versus the problem. ❤️

I want us to talk.

I want us to listen.

I want us to calm down.

Aur phir chahe kitna bhi gussa ho...

I want us to find our way back to each other.
"""
    },


    {
        "title": "❤️ I See Myself With You Till My Last Breath",
        "content": """
Because Shreya, main aapko sirf aaj ke liye nahi dekh raha.

When I think about my life ahead...

I see you.

When I think about growing older...

I see you.

When I think about having a home...

I see you.

When I think about having a family...

I see you.

And honestly, Baby...

I see myself with you till my last breath. ❤️

Maybe life will not always go according to our plans.

Maybe there will be difficult phases.

Maybe there will be days when loving each other feels harder than usual.

But even then...

I want to choose you.

Again and again.

And again.

Ninii Baby...

Whenever we fight, please don't think that I stopped loving you.

Whenever we disagree, please don't think that I want to leave you.

Difficult doesn't mean impossible. ❤️
"""
    }

]


# ============================================================
# CSS DESIGN
# ============================================================

st.markdown(
    """
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
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* ============================================================
   HEADINGS
============================================================ */

h1 {
    font-family: 'Great Vibes', cursive !important;
    color: #c2185b !important;
    text-align: center !important;
    font-size: 68px !important;
}


h2 {
    font-family: 'Playfair Display', serif !important;
    color: #c2185b !important;
    text-align: center !important;
}


/* ============================================================
   CENTER BUTTONS
============================================================ */

[data-testid="stButton"] {

    display: flex !important;

    justify-content: center !important;

    width: 100% !important;
}


[data-testid="stButton"] > button {

    min-height: 54px !important;

    min-width: 190px !important;

    border: none !important;

    border-radius: 50px !important;

    background:
        linear-gradient(
            135deg,
            #f45a91,
            #c2185b
        ) !important;

    color: white !important;

    font-family:
        'Playfair Display',
        serif !important;

    font-size: 17px !important;

    font-weight: 600 !important;

    padding:
        0 28px !important;

    box-shadow:
        0 10px 25px
        rgba(194,24,91,0.22) !important;

    transition:
        all 0.25s ease !important;
}


[data-testid="stButton"] > button:hover {

    transform:
        translateY(-2px)
        scale(1.03) !important;
}


/* ============================================================
   STORY CARD
============================================================ */

.story-card {

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.97),
            rgba(255,244,248,0.97)
        );

    border:
        1px solid
        rgba(194,24,91,0.15);

    border-radius: 32px;

    padding:
        42px 48px;

    box-shadow:
        0 18px 50px
        rgba(194,24,91,0.13);

    animation:
        fadePop
        0.7s ease;

}


/* ============================================================
   ANIMATION
============================================================ */

@keyframes fadePop {

    0% {
        opacity: 0;
        transform:
            translateY(25px)
            scale(0.97);
    }

    100% {
        opacity: 1;
        transform:
            translateY(0)
            scale(1);
    }

}


/* ============================================================
   STORY TITLE
============================================================ */

.story-title {

    font-family:
        'Playfair Display',
        serif;

    font-size: 32px;

    font-weight: 600;

    color: #c2185b;

    text-align: center;

    margin-bottom:
        28px;

}


/* ============================================================
   STORY TEXT
============================================================ */

.story-text {

    font-family:
        'Cormorant Garamond',
        serif;

    font-size: 25px;

    line-height: 1.55;

    color: #452631;

    text-align: center;

    white-space:
        pre-line;

}


/* ============================================================
   PROGRESS
============================================================ */

.progress-text {

    text-align:
        center;

    font-family:
        'Cormorant Garamond',
        serif;

    font-size:
        19px;

    color:
        #8a5363;

    margin-bottom:
        12px;

}


.progress-dots {

    text-align:
        center;

    font-size:
        18px;

    letter-spacing:
        5px;

    color:
        #e9a2ba;

    margin-bottom:
        22px;

}


/* ============================================================
   TIMELINE
============================================================ */

.timeline-title {

    font-family:
        'Great Vibes',
        cursive;

    font-size:
        62px;

    color:
        #c2185b;

    text-align:
        center;

    margin-bottom:
        8px;

}


.timeline-subtitle {

    font-family:
        'Cormorant Garamond',
        serif;

    font-size:
        24px;

    font-style:
        italic;

    color:
        #8a5363;

    text-align:
        center;

    margin-bottom:
        35px;

}


.love-timeline {

    width:
        100%;

    max-width:
        680px;

    margin:
        auto;

}


.memory-card {

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.97),
            rgba(255,241,247,0.97)
        );

    border-radius:
        25px;

    padding:
        28px
        30px;

    text-align:
        center;

    border:
        1px solid
        rgba(194,24,91,0.16);

    box-shadow:
        0 12px 30px
        rgba(194,24,91,0.10);

    animation:
        fadePop
        0.7s ease;

}


.memory-date {

    display:
        inline-block;

    background:
        linear-gradient(
            135deg,
            #f45a91,
            #c2185b
        );

    color:
        white;

    padding:
        7px
        20px;

    border-radius:
        30px;

    font-family:
        'Playfair Display',
        serif;

    margin-bottom:
        16px;

}


.memory-icon {

    font-size:
        40px;

}


.memory-event {

    font-family:
        'Playfair Display',
        serif;

    font-size:
        27px;

    color:
        #c2185b;

    margin:
        8px
        0
        12px;

}


.memory-text {

    font-family:
        'Cormorant Garamond',
        serif;

    font-size:
        22px;

    line-height:
        1.45;

    color:
        #542f3d;

}


.memory-connector {

    font-size:
        28px;

    color:
        #d94d82;

    text-align:
        center;

    padding:
        12px;

}


/* ============================================================
   FINAL MESSAGE
============================================================ */

.final-love-message {

    font-family:
        'Great Vibes',
        cursive;

    font-size:
        82px;

    color:
        #c2185b;

    text-align:
        center;

    line-height:
        1.2;

    animation:
        fadePop
        1s ease;

}


.final-love-subtext {

    font-family:
        'Cormorant Garamond',
        serif;

    font-size:
        30px;

    font-style:
        italic;

    color:
        #8a5363;

    text-align:
        center;

}


.final-signature {

    font-family:
        'Great Vibes',
        cursive;

    font-size:
        45px;

    color:
        #c2185b;

    text-align:
        center;

}


/* ============================================================
   MOBILE
============================================================ */

@media (max-width: 600px) {

    .block-container {

        padding-left:
            15px !important;

        padding-right:
            15px !important;
    }


    h1 {

        font-size:
            52px !important;
    }


    .story-card {

        padding:
            30px
            22px;
    }


    .story-title {

        font-size:
            26px;
    }


    .story-text {

        font-size:
            22px;
    }


    .timeline-title {

        font-size:
            50px;
    }


    .timeline-subtitle {

        font-size:
            21px;
    }


    .memory-event {

        font-size:
            23px;
    }


    .memory-text {

        font-size:
            20px;
    }


    .final-love-message {

        font-size:
            58px;
    }

}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# WELCOME PAGE
# ============================================================

if not st.session_state.show_story:

    st.write("")
    st.write("")

    st.markdown("# ❤️")

    st.markdown(f"# Hey, {GIRLFRIEND_NAME}...")

    st.markdown(f"## My {NICKNAME} ❤️")

    st.write("")

    st.markdown(
        """
        <div class="timeline-subtitle">
        I have something for you...
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="timeline-subtitle">
        Something I wanted to say properly...
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="timeline-subtitle">
        Something that comes directly from my heart. ❤️
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "💌 Start Reading, Baby... ❤️",
        key="start_button"
    ):
        st.session_state.show_story = True
        st.session_state.current_slide = 0
        st.rerun()


# ============================================================
# STORY EXPERIENCE
# ============================================================

else:

    TOTAL_STORY_SLIDES = len(slides) + 2

    current = st.session_state.current_slide


    # ========================================================
    # LETTER SLIDES
    # ========================================================

    if current < len(slides):

        slide = slides[current]

        st.markdown(
            f"""
            <div class="progress-text">
                Chapter {current + 1} of {TOTAL_STORY_SLIDES}
            </div>
            """,
            unsafe_allow_html=True
        )


        # Progress dots

        dots = ""

        for i in range(TOTAL_STORY_SLIDES):

            if i == current:
                dots += "❤️ "
            else:
                dots += "♡ "

        st.markdown(
            f"""
            <div class="progress-dots">
                {dots}
            </div>
            """,
            unsafe_allow_html=True
        )


        # Story card

        st.markdown(
            f"""
            <div class="story-card">

                <div class="story-title">
                    {slide["title"]}
                </div>

                <div class="story-text">
                    {slide["content"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.write("")


        # Navigation

        col1, col2, col3 = st.columns([1, 2, 1])


        with col1:

            if current > 0:

                if st.button(
                    "← Previous",
                    key=f"prev_{current}"
                ):
                    st.session_state.current_slide -= 1
                    st.rerun()


        with col3:

            if st.button(
                "Next →",
                key=f"next_{current}"
            ):
                st.session_state.current_slide += 1
                st.rerun()


    # ========================================================
    # OUR STORY TIMELINE
    # ========================================================

    elif current == len(slides):

        st.markdown(
            f"""
            <div class="progress-text">
                Our Memories ❤️
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            """
            <div class="story-card">

                <div class="timeline-title">
                    Our Story So Far ❤️
                </div>

                <div class="timeline-subtitle">
                    Every beautiful memory with you became a little
                    chapter in my heart.
                    And this is only the beginning of our story. ❤️
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.write("")


        memories = [

            (
                "14th July ❤️",
                "🎬",
                "Our Movie Date",
                "We went to watch Evil Dead Burn together. One of those simple moments that became a beautiful memory for me. ❤️"
            ),

            (
                "16th July 🛵",
                "🛵",
                "Our Scooty Drive",
                "We went on a beautiful scooty ride to Gorai Jetty. Just being with you made the ride special. ❤️"
            ),

            (
                "18th July 🚗",
                "🚗",
                "Our Car Drive",
                "We went for a drive together to Madh Island Beach. Another beautiful memory added to our story. ❤️"
            ),

            (
                "19th July 🥺",
                "🥺",
                "The Day I Dropped You in Pune",
                "I dropped you in Pune, and honestly, I missed you so much, especially on the way back. ❤️"
            ),

            (
                "20th July ❤️",
                "🥺",
                "Missing You So Much",
                "I realised just how much I missed you. Your absence was already starting to feel too big. 🥺❤️"
            ),

            (
                "24th July ❤️",
                "💌",
                "I Confessed My Feelings",
                "The day I finally told you what was in my heart. A moment I will always remember. ❤️"
            ),

            (
                "1st August 💍❤️",
                "💍",
                "I Proposed to You",
                "One of the most special moments of our story. The day I asked you to be mine. ❤️"
            ),

            (
                "6th August 🚴❤️",
                "🚴",
                "Cycling Together at SNGP",
                "We went cycling together at Sanjay Gandhi National Park. Another beautiful day and another beautiful memory with you. ❤️"
            ),

            (
                "A Special Day 💎❤️",
                "💎",
                "Your First Piece of Jewellery",
                "Giving you your first piece of jewellery from me was a small gesture, but a very special memory for my heart. ❤️"
            ),

            (
                "31st August ❤️",
                "👨‍👩‍👧‍👦",
                "I Met Riya Di & Jiju",
                "I met Riya Di and Jiju, and they even made dinner for me. It was such a warm and special day. ❤️"
            ),

            (
                "31st August 🎁❤️",
                "🎁",
                "My First Gift From You",
                "You gave me my first gift — a Hot Wheels. A small gift, but something that will always remind me of you. ❤️"
            )

        ]


        for index, memory in enumerate(memories):

            date, icon, event, text = memory

            st.markdown(
                f"""
                <div class="love-timeline">

                    <div class="memory-card">

                        <div class="memory-date">
                            {date}
                        </div>

                        <div class="memory-icon">
                            {icon}
                        </div>

                        <div class="memory-event">
                            {event}
                        </div>

                        <div class="memory-text">
                            {text}
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


            if index < len(memories) - 1:

                st.markdown(
                    """
                    <div class="memory-connector">
                        ❤️
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        st.write("")


        col1, col2, col3 = st.columns([1, 2, 1])


        with col1:

            if st.button(
                "← Previous",
                key="timeline_previous"
            ):
                st.session_state.current_slide -= 1
                st.rerun()


        with col3:

            if st.button(
                "Next →",
                key="timeline_next"
            ):
                st.session_state.current_slide += 1
                st.rerun()


    # ========================================================
    # FINAL LOVE SCREEN
    # ========================================================

    else:

        st.markdown(
            """
            <div class="story-card">

                <div class="final-love-message">
                    I Love You,<br>
                    Baby ❤️
                </div>

                <div class="final-love-subtext">
                    With all my heart. ❤️
                </div>

                <br>

                <div class="final-signature">
                    Forever yours,<br>
                    Karan ❤️
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.write("")
        st.write("")


        if st.button(
            "❤️ Read Our Story Again",
            key="restart_story"
        ):
            st.session_state.current_slide = 0
            st.rerun()
