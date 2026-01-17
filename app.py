import streamlit as st
import os
from dotenv import load_dotenv
import requests

if "saved_looks" not in st.session_state:
    st.session_state["saved_looks"] = []


# Load environment variables
load_dotenv()

#Unsplash API Key
UNSPLASH_ACCESS_KEY = "RxiMBIrBMPH80Swwl756douGXxgG4JSY20vzBwY7cPI"

# Page config
st.set_page_config(
    page_title="AI Look Generator",
    page_icon="✨",
    layout="centered"
)

# ---------- HEADER ----------
st.markdown(
    """
    <h1 style='text-align: center;'>✨ AI Look Generator</h1>
    <p style='text-align: center; color: gray;'>
    From trend data → drip
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------- TREND PRESETS ----------
st.subheader("🔥 Trend Presets")

col1, col2, col3 = st.columns(3)

if col1.button("🖤 Techwear"):
    st.session_state["colors"] = "Black, Grey"
    st.session_state["vibe"] = "Techwear"
    st.session_state["keywords"] = "futuristic, utility, cyberpunk"

if col2.button("💿 Y2K"):
    st.session_state["colors"] = "Pink, Silver, Blue"
    st.session_state["vibe"] = "Y2K"
    st.session_state["keywords"] = "retro, pop, early 2000s"

if col3.button("🤍 Quiet Luxury"):
    st.session_state["colors"] = "Beige, White, Taupe"
    st.session_state["vibe"] = "Quiet Luxury"
    st.session_state["keywords"] = "minimal, elegant, timeless"

st.divider()

# ---------- INPUT SECTION ----------
st.subheader("🎯 Customize Your Look")

colors = st.text_input(
    "🎨 Colors",
    value=st.session_state.get("colors", "")
)

vibe = st.text_input(
    "🧠 Vibe",
    value=st.session_state.get("vibe", "")
)

keywords = st.text_input(
    "🔑 Keywords",
    value=st.session_state.get("keywords", "")
)

st.divider()

# ---------- GENERATE OUTFIT ----------
if st.button("✨ Generate Outfit Description", use_container_width=True):
    if not colors or not vibe or not keywords:
        st.warning("Please fill all fields.")
    else:
        with st.spinner("Creating your look..."):
            prompt = f"""
            Create a detailed fashion outfit description.

            Colors: {colors}
            Vibe: {vibe}
            Keywords: {keywords}

            Write in an editorial, aesthetic tone.
            """

            outfit_text = f"""
            A {vibe.lower()} inspired outfit designed around {colors.lower()} tones.
            The look reflects a {keywords.lower()} aesthetic, blending modern silhouettes
            with effortless styling and a confident, editorial finish.
            """

            st.subheader("📝 Outfit Description")
            st.write(outfit_text)

            st.session_state["outfit_text"] = outfit_text

st.divider()

# ---------- GENERATE IMAGE ----------
if st.button("🖼️ Generate Moodboard Image", use_container_width=True):
    if not vibe or not keywords:
        st.warning("Please enter vibe and keywords.")
    else:
        st.subheader("🎨 Moodboard Visual")

        query = f"{vibe} {keywords} fashion"
        url = "https://api.unsplash.com/search/photos"

        params = {
            "query": query,
            "per_page": 1,
            "orientation": "squarish"
        }

        headers = {
            "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
        }

        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if data["results"]:
            image_url = data["results"][0]["urls"]["regular"]
            st.image(image_url)
        else:
            st.warning("No image found.")

st.divider()

# ---------- SAVE LOOK ----------
st.subheader("📝 Outfit Description")
st.write(outfit_text)

if st.button("💾 Save This Look"):
    st.session_state["saved_looks"].append({
        "colors": colors,
        "vibe": vibe,
        "keywords": keywords,
        "description": outfit_text
    })
    st.success("Look saved!")
st.subheader("💾 Saved Looks")

st.divider()
st.subheader("🗂️ Saved Looks")

if st.session_state["saved_looks"]:
    for i, look in enumerate(st.session_state["saved_looks"], start=1):
        with st.expander(f"Look #{i} — {look['vibe']}"):
            st.write(f"🎨 Colors: {look['colors']}")
            st.write(f"🔑 Keywords: {look['keywords']}")
            st.write(look["description"])
else:
    st.info("No saved looks yet. Generate and save your favorites.")
