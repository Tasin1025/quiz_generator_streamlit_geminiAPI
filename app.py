import streamlit as st
from api_calling import audio_generator, clean_text, notes_generator,quiz_generator
from PIL import Image
import time

st.title("Note generator and quiz summery")

st.subheader("Upload upto 3 images to generate")
st.divider()

## Sidebar

with st.sidebar:
    st.header("Controls")

    ## image uploader
    images = st.file_uploader(
        "Upload your images here",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
    )

    pil_images = []
    for image in images:
        pil_image = Image.open(image)
        pil_images.append(pil_image)

    if images:
        st.subheader("Uploaded Images")
        if len(images) > 3:
            st.warning("Please upload a maximum of 3 images.")
        else:
            col = st.columns(len(images))
            for i, image in enumerate(images):
                with col[i]:
                    st.image(image)

    ## Catrgory selection

    selected_option = st.selectbox(
        "Enter difficulty level",
        ("Easy", "Medium", "Hard"),
    )

    pressed = st.button("Click to generate quiz",type="primary")


if pressed:
    if not images:
        st.warning("Please upload at least one image to generate the quiz.")
    else:

        #note
        with st.container(border=True):
            st.subheader("Generated Note")
            with st.spinner("Loading Content...",show_time=True):
                note = notes_generator(pil_images)
                st.markdown(note)

        #audio
        with st.container(border=True):
            st.subheader("Generated Audio Transciption")
            with st.spinner("Generating transcription...",show_time=True):
                clean_notes = clean_text(note)       
                audio_transcription = audio_generator(clean_notes)  # clean text থেকে audio
                st.audio(audio_transcription)


        #quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) difficulty")
            with st.spinner("Generating quiz...",show_time=True):
                quiz = quiz_generator(pil_images, selected_option)
                st.markdown(quiz)