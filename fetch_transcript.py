import regex as re
from youtube_transcript_api import YouTubeRequestFailed, YouTubeTranscriptApi

from preprocessing import stride_sentences


def validate_youtube_link(url: str) -> str:
    """
    this method validates the youtube video link provided.
    input  : url (str)
    outputs: transcript (string/dict) 
    """
    yt_regex = r"^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=|\?v=)([^#\&\?]*).*"
    matches = re.findall(yt_regex, url)
    
    assert (len(matches[0][1]) == 11), "Invalid YouTube Link"

    video_id:str = matches[0][1]

    return video_id


def zip_transcript(transcript:list) -> dict:
    start_times = []
    texts = []
    for item in transcript:
        start_times.append(item['start'])
        texts.append(item['text'].strip().replace('\n',' '))
    
    return {
        'timestamps': start_times,
        'texts': texts
    }



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
        raise Exception('YouTube Request Failed, try again later.')
    
    return transcript   



if __name__ == '__main__':
    sample = 'https://www.youtube.com/watch?v=t6V9i8fFADI'
    sample2 = 'https://www.youtube.com/watch?v=1nLHIM2IPRY'
    fake_sample = 'https://www.youtube.com/watch?v=asdf3'
    transcript = fetch_transcript(url=sample)
    
    times, texts = zip_transcript(transcript)
    texts = stride_sentences(texts)
    print(texts[0])
    
    # with open('sample_group.txt','w') as f:
    #     for group in groups:
    #         f.write(f"{group}\n\n")
