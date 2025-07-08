An AI-powered app that detects your mood from text input using NLP and recommends personalized Spotify playlists based on your emotions.

🌟 Features

🧠 Mood detection from text using TextBlob (NLP)

🎵 Fetches playlists from Spotify API via spotipy

⚡ Simple, clean UI with Streamlit

🌍 Easily deployable (Streamlit Cloud, Replit, Render)

| Category | Tools Used                        |
| -------- | --------------------------------- |
| Language | Python                            |
| NLP      | TextBlob                          |
| API      | Spotipy (Spotify Web API wrapper) |
| Web UI   | Streamlit                         |
| Env Vars | python-dotenv                     |

LOCAL SETUP 

1. Clone the repository

		git clone https://github.com/manushi0204/mood-based-spotify.git
		cd mood-based-spotify

2. Set up virtual environment (optional but recommended)
 
		python -m venv venv
       venv\Scripts\activate  
       venv/bin/activate for macOS/Linux

3. Install required packages
   
         pip install -r requirements.txt

4. Run the app
      
         streamlit run app.py



