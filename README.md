# Youtube In-Video Search


### TODO:

- ~~fetch transcript~~
- ~~combine transcripts into groups~~
- ~~choose model: `all-MiniLM-L12-v2`~~
- semantic search on transcripts
- match results to the time stamp
- control youtube player based on the time stamp


```
methodology:

-> with stride 10, group sentences. a 60min video has around 150-160 groups with 10 sentences each
-> get the group with highest cosine similarity
-> choose the sentence with highest cosine similarity in that group
-> return time-stamp of the first sentence
```

```
In-progress 🚧️
```