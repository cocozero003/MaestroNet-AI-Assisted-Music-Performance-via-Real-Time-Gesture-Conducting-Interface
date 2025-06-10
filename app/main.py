import streamlit as st
from app.gesture_handler import process_video_for_bpm
from music.midi_utils import play_midi_file

st.set_page_config(page_title="MaestroNet", layout="centered")
st.title("MaestroNet – Real-Time Conductor BPM & Dynamics Estimator")

st.markdown(
    "Upload a short conducting video (MP4 or MOV) to estimate tempo and dynamics "
    "based on detected hand movements using pose estimation."
)

video_input = st.file_uploader("Upload Conducting Video", type=["mp4", "mov"])

if video_input is not None and video_input.type.startswith("video/"):
    try:
        with st.spinner("Analyzing conducting gestures..."):
            bpm, dynamic = process_video_for_bpm(video_input)
        if bpm > 0:
            st.success(f"Detected Tempo: {bpm:.2f} BPM")
            st.info(f"Estimated Dynamics Level: {dynamic}")
            if st.button("Play MIDI at Detected Tempo and Dynamics"):
                play_midi_file("music/example_score.mid", bpm=bpm, dynamic=dynamic)
        else:
            st.warning("Unable to detect a consistent beat pattern.")
    except Exception as e:
        st.error(f"Error during analysis: {e}")
