import streamlit as st

# ======================================================================
# PAGE CONFIG
# ======================================================================
st.set_page_config(
    page_title="For My Ninii Baby ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ======================================================================
# DATA — CHAPTERS
# ======================================================================
CHAPTERS = [
    {
        "title": "💌 My Baby, Read This Slowly",
        "paragraphs": [
            "Baby,",
            "I honestly don't know how to explain everything that is in my heart. "
            "There are so many things I want to tell you, and sometimes I feel like "
            "words are just not enough.",
            "But today I just want to write everything that I feel. Not in a perfect "
            "way, not with perfect words.",
            "Bas jaise mere dil mein hai, waise hi. ❤️",
        ],
    },
    {
        "title": "❤️ Ninii Baby, I Love You So Much",
        "paragraphs": [
            "Shreya, I don't think you truly understand how important you have become to me.",
            "You are not just someone I love, Baby. You have become a part of my life, "
            "a part of my thoughts, a part of my happiness and a part of my everyday life.",
            "Kabhi kabhi mere din mein kuch hota hai aur sabse pehle mujhe aapko batane "
            "ka mann karta hai. Sometimes I see something funny and immediately think "
            "about sending it to you.",
            "Sometimes I am doing absolutely nothing, and still somehow you are in my mind.",
            "Aur honestly, Baby... mujhe aapka meri life mein hona bahut pasand hai.",
            "I genuinely love having you in my life. ❤️",
        ],
    },
    {
        "title": "🥺 Baby, I Miss You",
        "paragraphs": [
            "I miss you so much, Shreya.",
            "Kabhi kabhi mujhe khud nahi pata hota ki main aapko itna kyun miss kar "
            "raha hoon. I miss talking to you, I miss hearing from you, I miss your "
            "presence and I miss our conversations.",
            "I even miss those small moments that probably don't seem important to "
            "anyone else but mean so much to me.",
            "Aur kabhi kabhi, Ninii Baby, baat karne ke baad bhi aapki yaad aati hai.",
            "Because when someone becomes this important to your heart, their absence "
            "is something you feel.",
            "Aur Baby, main aapki kami feel karta hoon.",
            "There are moments when I just wish you were here.",
            "Kaash aap mere paas hote.",
            "Nothing complicated.",
            "Bas aap aur main. ❤️",
        ],
    },
    {
        "title": "💕 I Want You In My Future",
        "paragraphs": [
            "Baby, I don't just want you for today. I don't just want beautiful "
            "conversations and beautiful memories.",
            "Main nahi chahta ki hum sirf ek temporary chapter bane ek dusre ki life mein.",
            "I want you in my life.",
            "I want you in my future.",
            "I want to make more memories with you, laugh with you, have silly "
            "arguments with you and then make up again.",
            "I want us to grow together and understand each other more as time passes.",
            "Aur Baby, life chahe kitni bhi difficult ho, main chahta hoon ki hum ek "
            "dusre ka saath na chhode.",
            "Because, Ninii Baby... you are someone I genuinely want to choose.",
            "Again and again. ❤️",
        ],
    },
    {
        "title": "🏡 When I Think About My Life...",
        "paragraphs": [
            "When I think about my future, Shreya, I don't only think about my "
            "career, money or success.",
            "Jab main apni life imagine karta hoon, main imagine karta hoon ki mere "
            "paas koi ho.",
            "Someone I can come home to.",
            "Someone I can tell about my day.",
            "Someone I can celebrate with when life is good and someone I can hold "
            "onto when life becomes difficult.",
            "Someone who feels like home.",
            "Aur honestly, Baby... jab main us person ke baare mein sochta hoon, I "
            "want it to be you. ❤️",
        ],
    },
    {
        "title": "❤️ I Want To Build A Life With You",
        "paragraphs": [
            "I dream about having our own little world, Baby.",
            "Our own home.",
            "Our own memories.",
            "Our own small routines.",
            "Waking up together.",
            "Coming back home after a long day.",
            "Eating together.",
            "Laughing about silly things.",
            "Annoying each other.",
            "Aur kabhi kabhi argue karke phir ek dusre ko mana lena. ❤️",
            "Mujhe koi perfect life nahi chahiye, Baby.",
            "I just want a real life, with real problems, real happiness and real memories.",
            "Aur aap mere saath.",
        ],
    },
    {
        "title": "👨‍👩‍👧‍👦 I Want A Family With You",
        "paragraphs": [
            "This is one of the deepest things in my heart, Baby.",
            "One day, I want to build a family with you.",
            "Humara apna chhota sa family.",
            "Our own home filled with love and laughter.",
            "Our own memories and our own traditions.",
            "I want us to grow older together.",
            "Aur ek din jab hum peeche mudke dekhein, toh hum un saare moments ko "
            "yaad karein—the beautiful moments, the difficult moments, the times we "
            "laughed, the times we cried and the times we had to be strong.",
            "Aur phir ek dusre ko dekh ke bolein...",
            "Hum ruke nahi.",
            "Humne ek dusre ko choose kiya.",
            "Humne saath nibhaya.",
            "We made it. ❤️",
            "Because when I imagine a family and a life that feels like mine...",
            "Aap us picture mein hote ho.",
        ],
    },
    {
        "title": "🤍 Baby, I Know I Am Not Perfect",
        "paragraphs": [
            "I know I am not perfect, Shreya.",
            "Main mistakes karta hoon.",
            "Kabhi kabhi main galat bol deta hoon.",
            "Sometimes I don't understand things immediately, aur kabhi kabhi main "
            "apni feelings properly express nahi kar pata.",
            "Shayad kabhi kabhi main aapko properly dikha bhi nahi pata ki aap mere "
            "liye kitni important ho.",
            "But Baby, please never doubt this.",
            "What I feel for you is real.",
            "Main genuinely aapki care karta hoon.",
            "Main genuinely aapko miss karta hoon.",
            "Main genuinely aapko apni life mein chahta hoon.",
            "Aur main genuinely aapke saath kuch beautiful build karna chahta hoon. ❤️",
        ],
    },
    {
        "title": "❤️ Ek Baat Main Dil Se Kehna Chahta Hoon...",
        "paragraphs": [
            "Baby, main jaanta hoon ki humare beech fights hongi. Disagreements honge.",
            "Kabhi kabhi hum ek dusre se naraz honge.",
            "Kabhi aap mujhe samajh nahi paogi, aur kabhi main aapko samajhne mein "
            "galti karunga.",
            "Kabhi hum dono gusse mein kuch aisa bol denge jo humein nahi bolna chahiye tha.",
            "But I want you to remember something.",
            "A fight between us does not mean that our love is over.",
            "A disagreement does not mean that our relationship is doomed.",
            "Narazgi ka matlab yeh nahi hai ki hum ek dusre ko khona chahte hain.",
            "Hum dono perfect nahi hain, Baby.",
            "Aur shayad humara relationship bhi kabhi perfect nahi hoga.",
            "But perfect hona zaroori bhi nahi hai.",
            "Saath rehna zaroori hai. ❤️",
            "Ek dusre ko samajhne ki koshish karna zaroori hai.",
            "Gusse ke baad bhi ek dusre ka haath nahi chhodna zaroori hai.",
        ],
    },
    {
        "title": "🤝 Difficult Doesn't Mean The End",
        "paragraphs": [
            "Because Baby, I don't want us to give up on each other just because we "
            "are having a difficult moment.",
            "Ek difficult day doesn't mean we have a difficult life.",
            "Ek fight doesn't mean our relationship is broken.",
            "Ek disagreement doesn't mean that our love has failed.",
            'Main nahi chahta ki har fight ke baad hum sochein, "Maybe this is the end."',
            "Instead, I want us to think...",
            "Hum dono milke isse solve karenge.",
            "Because for me, Baby, it should never be you versus me.",
            "It should always be you and me versus the problem. ❤️",
            "I want us to talk.",
            "I want us to listen.",
            "I want us to calm down.",
            "Aur phir chahe kitna bhi gussa ho...",
            "I want us to find our way back to each other.",
        ],
    },
    {
        "title": "❤️ I See Myself With You Till My Last Breath",
        "paragraphs": [
            "Because Shreya, main aapko sirf aaj ke liye nahi dekh raha.",
            "When I think about my life ahead, I see you.",
            "When I think about growing older, I see you.",
            "When I think about having a home, I see you.",
            "When I think about having a family, I see you.",
            "And honestly, Baby...",
            "I see myself with you till my last breath. ❤️",
            "Maybe life will not always go according to our plans.",
            "Maybe there will be difficult phases.",
            "Maybe there will be days when loving each other feels harder than usual.",
            "But even then...",
            "I want to choose you.",
            "Again and again.",
            "And again.",
            "Ninii Baby, whenever we fight, please don't think that I stopped loving you.",
            "Whenever we disagree, please don't think that I want to leave you.",
            "Difficult doesn't mean impossible. ❤️",
        ],
    },
]

# ======================================================================
# DATA — MEMORIES
# ======================================================================
MEMORIES = [
    {
        "date": "14th July", "icon": "🎬", "title": "Our Movie Date",
        "desc": "We went to watch Evil Dead Burn together. One of those simple "
                "moments that became a beautiful memory for me. ❤️",
        "special": False,
    },
    {
        "date": "16th July", "icon": "🛵", "title": "Our Scooty Drive",
        "desc": "We went on a beautiful scooty ride to Gorai Jetty. Just being "
                "with you made the ride special. ❤️",
        "special": False,
    },
    {
        "date": "18th July", "icon": "🚗", "title": "Our Car Drive",
        "desc": "We went for a drive together to Madh Island Beach. Another "
                "beautiful memory added to our story. ❤️",
        "special": False,
    },
    {
        "date": "19th July", "icon": "🥺", "title": "The Day I Dropped You in Pune",
        "desc": "I dropped you in Pune, and honestly... I missed you so much, "
                "especially on the way back. ❤️",
        "special": False,
    },
    {
        "date": "20th July", "icon": "❤️", "title": "Missing You So Much",
        "desc": "I realised just how much I missed you. Your absence was already "
                "starting to feel too big. 🥺❤️",
        "special": False,
    },
    {
        "date": "24th July", "icon": "❤️", "title": "I Confessed My Feelings",
        "desc": "The day I finally told you what was in my heart. A moment I "
                "will always remember. ❤️",
        "special": True,
    },
    {
        "date": "1st August", "icon": "💍❤️", "title": "I Proposed to You",
        "desc": "One of the most special moments of our story. The day I asked "
                "you to be mine. ❤️",
        "special": True,
        "proposal": True,
    },
    {
        "date": "6th August", "icon": "🚴❤️", "title": "Cycling Together at SNGP",
        "desc": "We went cycling together at Sanjay Gandhi National Park. "
                "Another beautiful day and another beautiful memory with you. ❤️",
        "special": False,
    },
    {
        "date": "A Special Day", "icon": "💎❤️", "title": "Your First Piece of Jewellery",
        "desc": "Giving you your first piece of jewellery from me was a small "
                "gesture, but a very special memory for my heart. ❤️",
        "special": False,
    },
    {
        "date": "31st August", "icon": "❤️", "title": "I Met Riya Di & Jiju",
        "desc": "I met Riya Di and Jiju, and they even made dinner for me. It "
                "was such a warm and special day. ❤️",
        "special": False,
    },
    {
        "date": "31st August", "icon": "🎁❤️", "title": "My First Gift From You",
        "desc": "You gave me my first gift — a Hot Wheels. A small gift, but "
                "something that will always remind me of you. ❤️",
        "special": True,
    },
]

# ======================================================================
# SESSION STATE
# ======================================================================
def init_state():
    defaults = {
        "screen": "welcome",       # welcome -> story -> letter_transition -> memories -> memory_pause -> final
        "story_page": 0,
        "memory_page": 0,
        "story_direction": "next",
        "memory_direction": "next",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def restart_experience():
    st.session_state.screen = "welcome"
    st.session_state.story_page = 0
    st.session_state.memory_page = 0
    st.session_state.story_direction = "next"
    st.session_state.memory_direction = "next"


init_state()

# ======================================================================
# CSS
# ======================================================================
def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Playfair+Display:wght@400;500;600;700&display=swap');

        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        div[data-testid="stToolbar"] {visibility: hidden;}
        div[data-testid="stDecoration"] {visibility: hidden;}

        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(120deg, #FFFBF7, #FFF5F8);
        }

        [data-testid="stAppViewContainer"] > .main {
            background:
                radial-gradient(circle at 15% 20%, rgba(244,114,182,0.18), transparent 45%),
                radial-gradient(circle at 85% 15%, rgba(219,39,119,0.10), transparent 50%),
                radial-gradient(circle at 25% 85%, rgba(252,231,243,0.55), transparent 55%),
                radial-gradient(circle at 80% 80%, rgba(255,251,247,0.9), transparent 60%),
                #FFF5F8;
            background-size: 200% 200%;
            animation: dreamyDrift 22s ease-in-out infinite;
        }

        @keyframes dreamyDrift {
            0%   { background-position: 0% 0%; }
            50%  { background-position: 100% 60%; }
            100% { background-position: 0% 0%; }
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 800px;
        }

        * { box-sizing: border-box; }

        /* ---------- Floating hearts ---------- */
        .heart-field {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
            overflow: hidden;
        }
        .floating-heart {
            position: absolute;
            bottom: -10%;
            color: #F472B6;
            opacity: 0;
            animation-name: floatUp;
            animation-timing-function: ease-in-out;
            animation-iteration-count: infinite;
        }
        @keyframes floatUp {
            0%   { transform: translateY(0) translateX(0); opacity: 0; }
            10%  { opacity: 0.55; }
            50%  { opacity: 0.35; }
            90%  { opacity: 0; }
            100% { transform: translateY(-100vh) translateX(15px); opacity: 0; }
        }

        /* ---------- Welcome screen ---------- */
        .welcome-wrap {
            text-align: center;
            padding: 3rem 1rem 1rem 1rem;
            position: relative;
            z-index: 1;
        }
        .welcome-heart {
            font-size: 2.6rem;
            animation: pulseHeart 2.4s ease-in-out infinite;
            opacity: 0;
            animation: pulseHeart 2.4s ease-in-out infinite, fadeIn 0.9s ease forwards;
        }
        @keyframes pulseHeart {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.15); }
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(12px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .welcome-hey {
            font-family: 'Great Vibes', cursive;
            font-size: 3.4rem;
            color: #9D174D;
            margin: 0.4rem 0 0.2rem 0;
            opacity: 0;
            animation: fadeIn 0.9s ease forwards;
            animation-delay: 0.5s;
        }
        .welcome-name {
            font-family: 'Playfair Display', serif;
            font-weight: 600;
            font-size: 1.5rem;
            letter-spacing: 2px;
            color: #DB2777;
            margin-bottom: 1.4rem;
            opacity: 0;
            animation: fadeIn 0.9s ease forwards;
            animation-delay: 1.0s;
        }
        .welcome-msg {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.35rem;
            color: #7A4B5D;
            max-width: 480px;
            margin: 0 auto 0.5rem auto;
            line-height: 1.8;
            opacity: 0;
            animation: fadeIn 0.9s ease forwards;
        }
        .welcome-msg.d1 { animation-delay: 1.5s; }
        .welcome-msg.d2 { animation-delay: 2.0s; }
        .welcome-decor {
            font-size: 1.3rem;
            margin: 1.4rem 0;
            letter-spacing: 6px;
            opacity: 0;
            animation: fadeIn 0.9s ease forwards;
            animation-delay: 2.5s;
        }

        /* ---------- Buttons (Streamlit native, restyled) ---------- */
        div.stButton { text-align: center; opacity: 0; animation: fadeIn 0.9s ease forwards; animation-delay: 3.0s; }
        div.stButton > button {
            font-family: 'Playfair Display', serif;
            font-size: 1.05rem;
            font-weight: 600;
            color: #FFFBF7 !important;
            background: linear-gradient(135deg, #F472B6, #9D174D);
            border: none;
            border-radius: 999px;
            padding: 0.85rem 2.4rem;
            box-shadow: 0 6px 22px rgba(157,23,77,0.35);
            transition: all 0.35s ease;
            position: relative;
            overflow: hidden;
        }
        div.stButton > button:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 10px 30px rgba(219,39,119,0.5);
        }
        div.stButton > button:active { transform: translateY(-1px) scale(0.99); }

        .nav-prev button {
            background: #FFF5F8 !important;
            color: #9D174D !important;
            border: 1.5px solid #F9C9DC !important;
            box-shadow: none !important;
        }
        .nav-prev button:hover { background: #FCE7F3 !important; }

        /* ---------- Progress ---------- */
        .progress-wrap {
            text-align: center;
            margin-bottom: 1.6rem;
            position: relative;
            z-index: 1;
        }
        .progress-label {
            font-family: 'Playfair Display', serif;
            letter-spacing: 2px;
            color: #9D174D;
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
        }
        .progress-track {
            width: 100%;
            max-width: 420px;
            height: 8px;
            background: #FCE7F3;
            border-radius: 999px;
            margin: 0 auto;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #F472B6, #9D174D);
            border-radius: 999px;
            box-shadow: 0 0 10px rgba(219,39,119,0.5);
            transition: width 0.7s ease;
        }
        .progress-sub {
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
            color: #7A4B5D;
            font-size: 1.05rem;
            margin-top: 0.6rem;
        }

        /* ---------- Chapter / memory card ---------- */
        .story-card {
            position: relative;
            z-index: 1;
            max-width: 750px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.55);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(244,114,182,0.35);
            border-radius: 32px;
            padding: 2.6rem 2.4rem;
            box-shadow: 0 8px 30px rgba(157,23,77,0.12), 0 2px 8px rgba(157,23,77,0.08);
            animation: cardEnterNext 0.75s ease forwards;
        }
        .story-card.dir-prev { animation-name: cardEnterPrev; }

        @keyframes cardEnterNext {
            from { opacity: 0; transform: translateY(25px); filter: blur(6px); }
            to   { opacity: 1; transform: translateY(0); filter: blur(0); }
        }
        @keyframes cardEnterPrev {
            from { opacity: 0; transform: translateY(-15px); filter: blur(6px); }
            to   { opacity: 1; transform: translateY(0); filter: blur(0); }
        }

        .chapter-num {
            text-align: center;
            font-family: 'Playfair Display', serif;
            letter-spacing: 3px;
            color: #D4A373;
            font-size: 0.85rem;
            opacity: 0;
            animation: fadeIn 0.7s ease forwards;
            animation-delay: 0.05s;
        }
        .chapter-title {
            text-align: center;
            font-family: 'Great Vibes', cursive;
            font-size: 2.6rem;
            background: linear-gradient(90deg, #9D174D, #DB2777);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 0.3rem 0 0.6rem 0;
            opacity: 0;
            animation: fadeIn 0.7s ease forwards;
            animation-delay: 0.15s;
        }
        .chapter-divider {
            text-align: center;
            color: #F472B6;
            letter-spacing: 3px;
            font-size: 0.9rem;
            margin-bottom: 1.4rem;
            opacity: 0;
            animation: fadeIn 0.7s ease forwards;
            animation-delay: 0.25s;
        }
        .chapter-content {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.25rem;
            line-height: 1.85;
            color: #3F1D2C;
            max-width: 650px;
            margin: 0 auto;
            opacity: 0;
            animation: fadeIn 0.9s ease forwards;
            animation-delay: 0.40s;
        }
        .chapter-content p { margin: 0 0 1rem 0; }
        .chapter-bottom-heart {
            text-align: center;
            margin-top: 1.4rem;
            color: #F472B6;
            font-size: 1.1rem;
            opacity: 0;
            animation: fadeIn 0.7s ease forwards;
            animation-delay: 0.70s;
        }

        /* ---------- Transition screens ---------- */
        .transition-wrap {
            text-align: center;
            padding: 4rem 1.5rem;
            position: relative;
            z-index: 1;
        }
        .transition-text {
            font-family: 'Great Vibes', cursive;
            font-size: 2.6rem;
            color: #9D174D;
            line-height: 1.5;
            opacity: 0;
            animation: fadeIn 1.2s ease forwards;
        }
        .transition-heart {
            font-size: 2rem;
            margin-bottom: 1.4rem;
            color: #F472B6;
            animation: pulseHeart 2.6s ease-in-out infinite;
        }

        /* ---------- Memory carousel ---------- */
        .memory-header {
            text-align: center;
            margin-bottom: 1.6rem;
            position: relative;
            z-index: 1;
        }
        .memory-title {
            font-family: 'Great Vibes', cursive;
            font-size: 2.8rem;
            color: #9D174D;
            margin-bottom: 0.2rem;
        }
        .memory-subtitle {
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
            color: #7A4B5D;
            font-size: 1.1rem;
        }

        .memory-card {
            position: relative;
            z-index: 1;
            max-width: 650px;
            margin: 0 auto;
            text-align: center;
            background: linear-gradient(160deg, #FFFBF7, #FCE7F3);
            border: 1px solid rgba(244,114,182,0.3);
            border-radius: 28px;
            padding: 2.4rem 2rem;
            box-shadow: 0 8px 26px rgba(157,23,77,0.12);
            animation: memoryEnterNext 0.7s ease forwards, floatCard 5s ease-in-out infinite;
        }
        .memory-card.dir-prev { animation-name: memoryEnterPrev, floatCard; }
        .memory-card.special {
            background: linear-gradient(160deg, #FFF5F8, #FCE7F3);
            border: 1px solid rgba(212,163,115,0.55);
            box-shadow: 0 10px 32px rgba(219,39,119,0.22);
        }

        @keyframes memoryEnterNext {
            from { opacity: 0; transform: translateX(40px); filter: blur(6px); }
            to   { opacity: 1; transform: translateX(0); filter: blur(0); }
        }
        @keyframes memoryEnterPrev {
            from { opacity: 0; transform: translateX(-40px); filter: blur(6px); }
            to   { opacity: 1; transform: translateX(0); filter: blur(0); }
        }
        @keyframes floatCard {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-6px); }
        }

        .memory-count {
            font-family: 'Playfair Display', serif;
            letter-spacing: 2px;
            color: #D4A373;
            font-size: 0.85rem;
            margin-bottom: 0.6rem;
        }
        .memory-date {
            font-family: 'Playfair Display', serif;
            font-size: 1.15rem;
            color: #DB2777;
            letter-spacing: 1px;
            margin-bottom: 0.3rem;
        }
        .memory-icon { font-size: 2.4rem; margin: 0.4rem 0; }
        .memory-card-title {
            font-family: 'Great Vibes', cursive;
            font-size: 2rem;
            color: #9D174D;
            margin-bottom: 0.6rem;
        }
        .memory-card.special .memory-card-title { text-shadow: 0 0 18px rgba(212,163,115,0.5); }
        .memory-desc {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.15rem;
            color: #3F1D2C;
            line-height: 1.75;
        }
        .memory-pulse-heart {
            font-size: 1.2rem;
            color: #D4A373;
            margin-top: 0.6rem;
            animation: pulseHeart 2s ease-in-out infinite;
        }

        .dots-wrap {
            text-align: center;
            margin: 1.2rem 0 0.4rem 0;
            position: relative;
            z-index: 1;
            letter-spacing: 6px;
        }
        .dot { color: #F9C9DC; font-size: 0.6rem; }
        .dot.active { color: #DB2777; font-size: 0.85rem; }

        /* ---------- Final screen ---------- */
        .final-wrap {
            text-align: center;
            padding: 4rem 1.5rem;
            position: relative;
            z-index: 1;
        }
        .final-heart-glow {
            font-size: 3rem;
            color: #F472B6;
            animation: heartbeatGlow 3.2s ease-in-out infinite;
            text-shadow: 0 0 30px rgba(244,114,182,0.6);
        }
        @keyframes heartbeatGlow {
            0%, 100% { transform: scale(1); opacity: 0.75; }
            50% { transform: scale(1.18); opacity: 1; }
        }
        .final-main {
            font-family: 'Great Vibes', cursive;
            font-size: 3.6rem;
            background: linear-gradient(90deg, #DB2777, #9D174D);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 1rem 0 0.6rem 0;
        }
        .final-sub {
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
            font-size: 1.3rem;
            color: #7A4B5D;
            margin-bottom: 1.6rem;
        }
        .final-sign {
            font-family: 'Great Vibes', cursive;
            font-size: 2.2rem;
            color: #9D174D;
        }

        /* ---------- Mobile responsiveness ---------- */
        @media (max-width: 640px) {
            .block-container { padding-left: 0.8rem; padding-right: 0.8rem; }
            .welcome-hey { font-size: 2.5rem; }
            .welcome-name { font-size: 1.15rem; }
            .welcome-msg { font-size: 1.1rem; }
            .story-card { padding: 1.8rem 1.3rem; border-radius: 24px; }
            .chapter-title { font-size: 2rem; }
            .chapter-content { font-size: 1.1rem; }
            .transition-text { font-size: 1.9rem; }
            .memory-title { font-size: 2.2rem; }
            .memory-card { padding: 1.8rem 1.3rem; }
            .memory-card-title { font-size: 1.6rem; }
            .final-main { font-size: 2.6rem; }
            .final-heart-glow { font-size: 2.3rem; }
            div.stButton > button { padding: 0.75rem 1.6rem; font-size: 0.95rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_floating_hearts():
    hearts_config = [
        (7, 12, 0, 0), (18, 16, 2.5, 1), (30, 10, 5.0, 2),
        (46, 20, 1.5, 3), (58, 14, 4.0, 0), (70, 18, 6.5, 1),
        (82, 11, 3.0, 2), (90, 22, 0.5, 3),
    ]
    sizes = ["1.1rem", "1.5rem", "0.9rem", "1.8rem"]
    hearts_html = ""
    for left, duration, delay, size_idx in hearts_config:
        hearts_html += (
            f'<span class="floating-heart" style="left:{left}%; '
            f'font-size:{sizes[size_idx]}; animation-duration:{duration}s; '
            f'animation-delay:{delay}s;">❤️</span>'
        )
    st.markdown(f'<div class="heart-field">{hearts_html}</div>', unsafe_allow_html=True)


# ======================================================================
# RENDER HELPERS
# ======================================================================
def render_progress(current_index, total, label="Our Little Love Story ❤️"):
    percent = int(((current_index + 1) / total) * 100)
    st.markdown(
        f"""
        <div class="progress-wrap">
            <div class="progress-label">Chapter {current_index + 1} of {total} &nbsp;·&nbsp; {current_index + 1:02d} / {total:02d}</div>
            <div class="progress-track">
                <div class="progress-fill" style="width:{percent}%;"></div>
            </div>
            <div class="progress-sub">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_story_card(chapter, direction):
    dir_class = "dir-prev" if direction == "previous" else ""
    paragraphs_html = "".join(f"<p>{p}</p>" for p in chapter["paragraphs"])
    st.markdown(
        f"""
        <div class="story-card {dir_class}">
            <div class="chapter-title">{chapter['title']}</div>
            <div class="chapter-divider">♡ ───────── ♡ ───────── ♡</div>
            <div class="chapter-content">{paragraphs_html}</div>
            <div class="chapter-bottom-heart">❤️</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_story_navigation(index, total):
    st.write("")
    is_first = index == 0
    is_last = index == total - 1

    if is_first:
        cols = st.columns([1])
        with cols[0]:
            if st.button("Next ❤️ →", key="story_next", use_container_width=True):
                st.session_state.story_direction = "next"
                st.session_state.story_page += 1
                st.rerun()
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="nav-prev">', unsafe_allow_html=True)
            if st.button("← Previous", key="story_prev", use_container_width=True):
                st.session_state.story_direction = "previous"
                st.session_state.story_page -= 1
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            next_label = "✨ Continue" if is_last else "Next ❤️ →"
            if st.button(next_label, key="story_next", use_container_width=True):
                st.session_state.story_direction = "next"
                if is_last:
                    st.session_state.screen = "letter_transition"
                else:
                    st.session_state.story_page += 1
                st.rerun()


def render_memory_card(memory, index, total, direction):
    dir_class = "dir-prev" if direction == "previous" else ""
    special_class = "special" if memory.get("special") else ""
    pulse = '<div class="memory-pulse-heart">✨ ❤️ ✨</div>' if memory.get("special") else ""
    st.markdown(
        f"""
        <div class="memory-card {special_class} {dir_class}">
            <div class="memory-count">Memory {index + 1} of {total}</div>
            <div class="memory-date">{memory['date']}</div>
            <div class="memory-icon">{memory['icon']}</div>
            <div class="memory-card-title">{memory['title']}</div>
            <div class="memory-desc">{memory['desc']}</div>
            {pulse}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_dots(index, total):
    dots_html = ""
    for i in range(total):
        cls = "dot active" if i == index else "dot"
        dots_html += f'<span class="{cls}">●</span> '
    st.markdown(f'<div class="dots-wrap">{dots_html}</div>', unsafe_allow_html=True)


def render_memory_navigation(index, total):
    st.write("")
    is_first = index == 0
    is_last = index == total - 1

    if is_first:
        cols = st.columns([1])
        with cols[0]:
            if st.button("Next Memory ❤️ →", key="mem_next", use_container_width=True):
                st.session_state.memory_direction = "next"
                st.session_state.memory_page += 1
                st.rerun()
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="nav-prev">', unsafe_allow_html=True)
            if st.button("← Previous Memory", key="mem_prev", use_container_width=True):
                st.session_state.memory_direction = "previous"
                st.session_state.memory_page -= 1
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            next_label = "❤️ Continue" if is_last else "Next Memory ❤️ →"
            if st.button(next_label, key="mem_next", use_container_width=True):
                st.session_state.memory_direction = "next"
                if is_last:
                    st.session_state.screen = "memory_pause"
                else:
                    st.session_state.memory_page += 1
                st.rerun()


# ======================================================================
# SCREENS
# ======================================================================
def screen_welcome():
    st.markdown(
        """
        <div class="welcome-wrap">
            <div class="welcome-heart">❤️</div>
            <div class="welcome-hey">Hey, Shreya...</div>
            <div class="welcome-name">My Ninii Baby ❤️</div>
            <div class="welcome-msg d1">I have something for you.<br>Something I wanted to say properly...</div>
            <div class="welcome-msg d2">Something that comes directly from my heart. ❤️</div>
            <div class="welcome-decor">❤️ 💕 💗 💖 ❤️</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col = st.columns([1, 2, 1])[1]
    with col:
        if st.button("💌 Tap Here, Baby... ❤️", key="welcome_btn", use_container_width=True):
            st.session_state.screen = "story"
            st.session_state.story_direction = "next"
            st.rerun()


def screen_story():
    index = st.session_state.story_page
    render_progress(index, len(CHAPTERS))
    render_story_card(CHAPTERS[index], st.session_state.story_direction)
    render_story_navigation(index, len(CHAPTERS))


def screen_letter_transition():
    st.markdown(
        """
        <div class="transition-wrap">
            <div class="transition-heart">❤️</div>
            <div class="transition-text">
                And then...<br>before I knew it...<br>we started creating our own little story. ❤️
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col = st.columns([1, 2, 1])[1]
    with col:
        if st.button("✨ See Our Memories", key="to_memories", use_container_width=True):
            st.session_state.screen = "memories"
            st.session_state.memory_direction = "next"
            st.rerun()


def screen_memories():
    st.markdown(
        """
        <div class="memory-header">
            <div class="memory-title">❤️ Our Little Story</div>
            <div class="memory-subtitle">Every beautiful memory with you became a part of my heart.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    index = st.session_state.memory_page
    render_memory_card(MEMORIES[index], index, len(MEMORIES), st.session_state.memory_direction)
    render_dots(index, len(MEMORIES))
    render_memory_navigation(index, len(MEMORIES))


def screen_memory_pause():
    st.markdown(
        """
        <div class="transition-wrap">
            <div class="transition-heart">❤️</div>
            <div class="transition-text">
                And somehow...<br>all these little moments...<br>became my favourite story. ❤️
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col = st.columns([1, 2, 1])[1]
    with col:
        if st.button("❤️ One Last Thing", key="to_final", use_container_width=True):
            st.session_state.screen = "final"
            st.rerun()


def screen_final():
    st.markdown(
        """
        <div class="final-wrap">
            <div class="final-heart-glow">❤️</div>
            <div class="final-main">I Love You, Baby ❤️</div>
            <div class="final-sub">With all my heart. ❤️</div>
            <div class="final-sign">Forever yours,<br>Karan ❤️</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col = st.columns([1, 2, 1])[1]
    with col:
        if st.button("❤️ Read Our Story Again", key="restart_btn", use_container_width=True):
            restart_experience()
            st.rerun()


# ======================================================================
# MAIN
# ======================================================================
def main():
    inject_css()
    render_floating_hearts()

    screen = st.session_state.screen
    if screen == "welcome":
        screen_welcome()
    elif screen == "story":
        screen_story()
    elif screen == "letter_transition":
        screen_letter_transition()
    elif screen == "memories":
        screen_memories()
    elif screen == "memory_pause":
        screen_memory_pause()
    elif screen == "final":
        screen_final()
    else:
        st.session_state.screen = "welcome"
        st.rerun()


if __name__ == "__main__":
    main()
