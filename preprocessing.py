def stride_sentences(texts:list, stride=10):
    groups = [texts[i:i+stride] for i in range(0, len(texts), stride)]
    groups = [' '.join(group).strip() for group in groups]
    return groups


def dequestionize(question:str):
    question_words = [word for word in question.split() if word.lower() not in ['what','where','how','who','why']]
    return ' '.join(question_words).replace('?','').strip()


def create_similarity_text(question:str, answer: str):
    question = dequestionize(question)
    return f"{answer} {question}"

def create_result_url(base_url,timestamp):
    full_url = f"{base_url}&t={int(timestamp)}s"
    return full_url