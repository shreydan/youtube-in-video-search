from sentence_splitter import split_text_into_sentences


def group_sentences(text, stride=10):
    sentences = split_text_into_sentences(text,language='en')

    groups = [sentences[i:i+stride] for i in range(0, len(sentences), stride)]
    groups = [' '.join(group).strip() for group in groups]
    return groups
