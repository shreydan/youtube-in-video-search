from model import Engine
from fetch_transcript import fetch_transcript
from preprocessing import create_similarity_text, create_result_url



if __name__ == '__main__':
    sample = 'https://www.youtube.com/watch?v=t6V9i8fFADI'
    sample2 = 'https://www.youtube.com/watch?v=1nLHIM2IPRY'
    sample3 = 'https://www.youtube.com/watch?v=nIoXOplUvAw'
    transcript = fetch_transcript(url=sample3)
    model = Engine(transcript)
    
    q = 'hotkey to focus object'
    ans = model.ask(q)
    
    print(q)
    print(ans)
    similarity_text = create_similarity_text(q,ans)
    print(similarity_text)
    groups,timestamps = model.find_similar(similarity_text)
    print(groups[0])
    print(create_result_url(sample3,timestamps[0]))