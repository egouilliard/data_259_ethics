import torch
from transformers import BertTokenizer, BertForQuestionAnswering

class BertQuery:
    def __init__(self, model_name='bert-large-uncased-whole-word-masking-finetuned-squad'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForQuestionAnswering.from_pretrained(model_name)
        self.history = []
        self.q_and_a = {}

    def add_to_history(self, question, category=None):
        self.history.append((question, category))

    def create_context(self):
        return " ".join(q for q, _ in self.history)

    def query(self, question, context):
        inputs = self.tokenizer(question, context, return_tensors='pt')
        with torch.no_grad():
            outputs = self.model(**inputs)
        answer_start_scores, answer_end_scores = outputs.start_logits, outputs.end_logits
        answer_start = torch.argmax(answer_start_scores)
        answer_end = torch.argmax(answer_end_scores) + 1
        answer = self.tokenizer.convert_tokens_to_string(self.tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][answer_start:answer_end]))
        return answer

    def ask(self, question, question_num, category=None):
        context = self.create_context()
        answer = self.query(question, context)
        self.q_and_a[question_num] = {"question": question, "answer": answer, "category": category}
        self.add_to_history(question, category)
        return answer

    def update_answer(self, question, new_answer, new_category=None):
        if question in self.q_and_a:
            self.q_and_a[question]['answer'] = new_answer
            if new_category:
                self.q_and_a[question]['category'] = new_category

