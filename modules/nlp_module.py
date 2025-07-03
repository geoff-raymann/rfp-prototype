
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import os

MODEL_DIR = "./models/bert-base-uncased"

if not os.path.exists(MODEL_DIR):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', cache_dir='./models')
    model = BertForSequenceClassification.from_pretrained(
        'bert-base-uncased',
        num_labels=4,
        cache_dir='./models'
    )
else:
    tokenizer = BertTokenizer.from_pretrained(MODEL_DIR)
    model = BertForSequenceClassification.from_pretrained(MODEL_DIR, num_labels=4)

def score_technical_response(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    scores = torch.softmax(logits, dim=1).tolist()[0]
    return scores
