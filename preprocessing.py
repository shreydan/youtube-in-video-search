def stride_sentences(texts:list, stride=10):
    groups = [texts[i:i+stride] for i in range(0, len(texts), stride)]
    groups = [' '.join(group).strip() for group in groups]
    return groups


def dequestionize(question:str):
    question = [word for word in question.split() if word.lower() not in ['what','where','how','who','why']]
    return ' '.join(question).replace('?','').strip()


def create_similarity_text(question:str, answer: str):
    question = dequestionize(question)
    return f"{answer} {question}"