import torch
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
from pathlib import Path

class Engine:
    def __init__(self, groups:list) -> None:

        self.base_path = Path('./models')

        self.qa_model_name = 'QA_Model'
        self.qa_model_path = self.base_path / self.qa_model_name
        self.qa_model = pipeline('question-answering',model=str(self.qa_model_path))

        self.sim_model_name = 'Similarity_Model'
        self.sim_model_path = self.base_path / self.sim_model_name
        self.sim_model = SentenceTransformer(self.sim_model_path)
        
        self.text_groups = groups
        
        self.embeddings = self._encode_transcript()

    def _encode_transcript(self):
        return self.sim_model.encode(self.text_groups)

    def ask(self, question_text:str):

        result = self.qa_model(
            question=question_text,
            context=' '.join(self.text_groups).strip(),
            doc_stride=256,
            max_answer_len=512,
            max_question_len=128,
        )
        return result['answer']


    def find_similar(self, txt:str):
        txt = self.sim_model.encode(txt)
        similarities:torch.Tensor = cos_sim(txt,self.embeddings)
        similarities = similarities.reshape(-1)
        indices = list(torch.argsort(similarities))
        indices = [idx.item() for idx in indices[::-1]]
        return indices


if __name__ == '__main__':
    model = Engine()
    