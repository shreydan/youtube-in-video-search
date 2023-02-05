from model import Engine
from fetch_transcript import fetch_transcript, zip_transcript
from preprocessing import create_similarity_text, stride_sentences



if __name__ == '__main__':
    sample = 'https://www.youtube.com/watch?v=t6V9i8fFADI'
    sample2 = 'https://www.youtube.com/watch?v=1nLHIM2IPRY'
    sample3 = 'https://www.youtube.com/watch?v=nIoXOplUvAw'
    transcript = fetch_transcript(url=sample3)
    _,transcript = zip_transcript(transcript)
    groups = stride_sentences(transcript,stride=10)
    print(groups)
    model = Engine(groups=groups)
    
    q = 'hotkey to focus object'
    ans = model.ask(q)
    
    print(q)
    print(ans)
    similarity_text = create_similarity_text(q,ans)
    print(similarity_text)

    indices = model.find_similar(similarity_text)
    print(f"{groups[indices[0]-1]} --- {groups[indices[0]]} --- {groups[indices[0]+1]}")
    