import streamlit as st
from streamlit_player import st_player

from model import Engine
from fetch_transcript import fetch_transcript
from preprocessing import create_similarity_text, create_result_url

with st.container():
    st.title('YouTube In-Video Search')
    st.write('Perform extractive Q&A and semantic search to watch what you want.')

with st.container():

    url_input = st.text_input(label='Video',placeholder='enter YouTube video url')
    
    question_input = st.text_input(label='Question',placeholder='enter your question')

    get_ans = st.button(label='Answer!')

    if len(url_input)!='' and len(question_input)!='' and get_ans:
        
        with st.spinner('loading your video...'):
            transcript = fetch_transcript(url_input)
            model = Engine(transcript)
            prev_url = url_input

        with st.spinner('finding an answer...'):
            answer = model.ask(question_input)
            similarity_text = create_similarity_text(question_input,answer)
            groups,timestamps = model.find_similar(similarity_text)
            url = create_result_url(url_input,timestamps[0])

        with st.container():

            st.caption('Extracted Answer:')
            st.write(answer)
            st.caption('In Video:')
            st_player(url)
        
