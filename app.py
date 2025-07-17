import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components


with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Tebak Hadiah", "Aib"],
    )

if selected == "Home":
    st.set_page_config(page_title="Home", layout="wide")
    st.title("Hi Kak Uma!!")
    st.markdown("Happy Birthday ya kak.")  
    st.markdown("Semoga panjang umur, sehat selalu, dan bahagia selalu ya kak. Semoga sukses selalu dalam segala hal yang kakak kerjakan. Terima kasih sudah menjadi kakak yang baik dan selalu mendukungku. Selamat ulang tahun kakak, semoga hari ini menjadi hari yang spesial dan penuh kebahagiaan.")
    st.markdown("Apalagi ya, itu diatas buatan AI si kak. Tar bes panjang kasian AI nya.")
    st.markdown("Aku bilang yang paling atas aja si. **Iiiii 20 tahun. TUA!**")
    if st.button("Happy Birthday sekali lagi kak!"):
        components.html(
        """
        <html>
        <head>
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        </head>
        <body style="margin:0;overflow:hidden;">
        <canvas id="c"></canvas>
        <script>
        let angle = 0;
        const duration = 5000; // 5 detik
        const end = Date.now() + duration;

        (function frame() {
          confetti({
            particleCount: 6,
            angle: angle,
            spread: 70,
            origin: { x: 0.5, y: 0.5 },
          });
          angle += 10; // ubah sudut untuk spiral
          if (Date.now() < end) {
            requestAnimationFrame(frame);
          }
        }());
        </script>
        </body>
        </html>
        """,
        height=400,
    )

    st.text_input("Harapan kakak di **20 Tahun ini apa kak**?", placeholder="Tulis harapan dan doa di sini kak...")
    
    if st.button("Kirim Harapan🎆"):
        st.success("Harapan kakak sudah terkirim! Semoga harapan kakak tercapai di tahun ini. AST.")
        components.html(
        """
        <html>
        <head>
        <style>
        body {
          margin: 0;
          overflow: hidden;
          background: transparent;
        }
        .star {
          position: fixed;
          top: -10px;
          color: #fff;
          text-shadow: 0 0 6px #ffd700, 0 0 12px #ffa500;
          user-select: none;
          font-size: 14px;
          animation-name: fall;
          animation-timing-function: linear;
        }
        @keyframes fall {
          to {
            transform: translateY(110vh) rotate(360deg);
            opacity: 0;
          }
        }
        </style>
        </head>
        <body>
        <script>
        const stars = [];
        for (let i = 0; i < 60; i++) {
          const star = document.createElement("div");
          star.className = "star";
          star.innerHTML = "★";
          star.style.left = Math.random() * 100 + "vw";
          star.style.fontSize = (Math.random() * 12 + 8) + "px";
          star.style.animationDuration = (Math.random() * 3 + 2) + "s";
          document.body.appendChild(star);
          stars.push(star);
        }
        setTimeout(() => {
          stars.forEach(s => s.remove());
        }, 5000);
        </script>
        </body>
        </html>
        """,
        height=300,
    )

elif selected == "Tebak Hadiah":
    st.set_page_config(page_title="Tebak Hadiah", layout="wide")
    st.title("Hadiah buat Kak Uma 🎁")
    st.markdown("Isinya random, bisa aja: 🐍 Ular(yakali), atau \n🐸 Kodok(jelek), atau mungkin\n🦎 Cicak(ni b aja si)")
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHQxNzE3ZTJycTlyNjhuem82Y3UweTVzNjR0dWgzejNmODZndG96ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/Td2KNheKp39VbCK6qm/giphy.gif")
        
    if st.button("Buka Hadiah ✨"):
        st.success("🎈 Aku kasi langsung kodoknya. Mau ketemu kak, bisa kapan? Eh emng kodok? ga lah njs")
        st.balloons()

elif selected == "Aib":
    st.set_page_config(page_title="Galeri Aib", layout="wide")

    if "show_input" not in st.session_state:
        st.session_state.show_input = False

    if st.session_state.show_input:
        password = st.text_input(
            "Masukkan password kak buat liat aib diri sendiri",
            placeholder="Tebak password di sini kak...",
            type="password"
        )
        
    st.markdown("Clue nya: aku kak")

    if st.button("Buka Galeri Aib"):
        st.session_state.show_input = True

    if password: 
        if password == "Ayanokoji":  
            st.success("✅ Password benar! Selamat menikmati Galeri Aib")

            fotos = [
                {"path": "cicak.jpg", "caption": "Ganggu kali cicak ni, minggir kek mau liat elf"},
                {"path": "elf.jpg", "caption": "Na ini elf apa ya, kok bisa ada di galeri aib? Harusnya di galeri spesial ya"},
                {"path": "gajelas.jpg", "caption": "Ngapain coba ni potong rambut, gajelas banget"},
                {"path": "kacalama.jpg", "caption": "Bingung-bingungnya ni bandingin kacamata lama sama yang baru, mana yang lebih kece? Jelas elf nya"},
                {"path": "seriusnya.jpg", "caption": "Gila serius banget ni, padahal cuma mau foto bandingin kacamata doang"},
                {"path": "ujan.jpg", "caption": "Keren kak ujan ujanan trus jadi minoritas"},
                {"path": "uno.jpg", "caption": "Gilaa, ni si gabakalan lupa main uno sampe jam 12 malem"},
                ]

            cols_per_row = 3

            for i in range(0, len(fotos), cols_per_row):
                row_items = fotos[i:i+cols_per_row]
                cols = st.columns(len(row_items))
                for col, foto in zip(cols, row_items):
                    with col:
                        st.image(foto["path"], use_container_width=True)
                        st.caption(foto["caption"])
            st.title("**Dikit banget ya Aib nya!**")        
        else:
            st.error("❌ Password salah, coba lagi!")
