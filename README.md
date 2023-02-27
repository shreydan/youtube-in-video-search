# Youtube Q&A Search

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