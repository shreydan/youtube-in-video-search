# 📹️ Youtube Q&A Search

https://user-images.githubusercontent.com/21237364/221598257-36aedf02-dd17-46b0-b494-67fabe9c8e7d.mp4


### Try it out in [Google Colab](https://colab.research.google.com/drive/1ZrbUBhgfrZXIKwNwIFvhFwl9LcqAe_5Z?usp=sharing)

#### Try it out at [HuggingFace Spaces](https://huggingface.co/spaces/shreydan/youtube-QandA)
(it's kinda slow as it's on free-tier, would recommend running locally/on Colab)

```
           HOW IT WORKS :)

    paste YouTube link in the app.
                👇️
        enter your question
                👇️
       a question-answering model
         (roBERTa-base-squad2)
       extracts your answer from
         the video transcript
        (english only for now)
                👇️
    the question and the answer are
   then used to apply semantic-search
           (MiniLM-L12-v2) 
   to get the timestamp of the answer
                👇️
    the final outputs are the answer
     and the YouTube video scrubbed
       to the desired timestamp.
```
