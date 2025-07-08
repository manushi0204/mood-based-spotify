import streamlit as st
from mood_model import detect_mood
from spotify import get_playlists_by_mood

st.set_page_config(page_title="Mood-Based Spotify Playlist 🎧")
st.title("🎵 Mood-Based Spotify Playlist Generator")
st.markdown("Enter how you're feeling below, and we'll find the perfect playlist for you.")

user_input = st.text_area("How are you feeling today?", height=150)

if st.button("Generate Playlist"):
    if user_input:
        mood = detect_mood(user_input)
        st.success(f"Detected mood: **{mood.capitalize()}**")

        playlists = get_playlists_by_mood(mood)
        if playlists:
            st.subheader("🎶 Recommended Playlists:")
            for p in playlists:
                st.markdown(f"- [{p['name']}]({p['url']})")
        else:
            st.warning("No playlists found for this mood. Try a different input.")
    else:
        st.warning("Please enter how you're feeling to continue.")
