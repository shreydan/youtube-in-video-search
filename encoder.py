from sentence_transformers import SentenceTransformer
from pathlib import Path

class Encoder:
    def __init__(self) -> None:
        self.model_name = 'all-MiniLM-L12-v2'
        self.model_path = Path('./models') / self.model_name
        self.model = SentenceTransformer(self.model_path)

if __name__ == '__main__':
    model = Encoder()
    