import streamlit as st
from engine import OutfitGenerator

st.set_page_config(page_title="Street Style Generator", layout="wide")

st.title("👟 Street Style Generator")
st.caption("For people who want better drip without overthinking")

gen = OutfitGenerator()

trend_ids = [
    "streetwear", "y2k", "quiet", "minimal", "90s", "indie",
    "grunge", "gorpcore", "office", "mob", "athleisure", "workwear"
]

trend = st.selectbox("Choose a trend", trend_ids)
gender = st.selectbox("Gender", ["unisex", "men", "women"])

vibes = st.multiselect(
    "Vibe modifiers",
    ["Edgy", "Clean", "Vintage", "Monochrome", "Loud", "Understated",
     "Romantic", "Rebellious", "Professional", "Playful", "Dark", "Bright"]
)

keywords = st.text_input("Keywords (comma separated)").split(",")

if st.button("✨ Generate Outfit"):
    outfit = gen.generate_outfit(
        trend_id=trend,
        gender=gender,
        vibes=[v.strip() for v in vibes],
        keywords=[k.strip() for k in keywords if k.strip()]
    )

    st.subheader(outfit["trend"])
    st.write(outfit["description"])

    st.markdown("### 🧠 AI Styling Logic")
    st.write(outfit["ai_logic"])

    st.markdown("### 👕 The Fit")
    for p in outfit["pieces"]:
        st.write(f"- {p}")

    st.markdown("### 🎨 Colors")
    st.write(", ".join(outfit["colors"]))

    st.caption("Style inspiration • editorial + street references")

    st.subheader("🖼️ Moodboard")

    cols = st.columns(4)
    for i, img in enumerate(outfit["moodboard"]):
        with cols[i]:
            st.image(img, use_container_width=True)

    

    if st.button("💾 Save Look"):
        gen.save_look(outfit)
        st.success("Look saved!")
