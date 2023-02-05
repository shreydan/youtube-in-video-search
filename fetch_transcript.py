from youtube_transcript_api import YouTubeTranscriptApi, YouTubeRequestFailed
import regex as re
from preprocessing import stride_sentences

def validate_youtube_link(url: str) -> str:
    """
    this method validates the youtube video link provided.
    input  : url (str)
    outputs: transcript (string/dict) 
    """
    yt_regex = "^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=|\?v=)([^#\&\?]*).*"
    matches = re.findall(yt_regex, url)
    
    assert len(matches[0][1]) == 11

    video_id:str = matches[0][1]

    return video_id


def zip_transcript(transcript:list) -> list:
    start_times = []
    texts = []
    for item in transcript:
        start_times.append(item['start'])
        texts.append(item['text'].strip().replace('\n',' '))
    
    return start_times, texts



def full_text(transcript: list) -> str:
    texts = []
    for item in transcript:
        texts.append(item['text'])
    return ' '.join(texts).strip()


def fetch_transcript(url: str) -> list:
    
    video_id = validate_youtube_link(url)
    
    try:
        transcript:list = YouTubeTranscriptApi.get_transcript(video_id=video_id)

    except YouTubeRequestFailed:
        return None
    
    return transcript   



if __name__ == '__main__':
    sample = 'https://www.youtube.com/watch?v=t6V9i8fFADI'
    sample2 = 'https://www.youtube.com/watch?v=1nLHIM2IPRY'
    transcript = fetch_transcript(url=sample)
    
    times, texts = zip_transcript(transcript)
    texts = stride_sentences(texts)
    
    # with open('sample_group.txt','w') as f:
    #     for group in groups:
    #         f.write(f"{group}\n\n")