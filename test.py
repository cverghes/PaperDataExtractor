from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
import fitz  # PyMuPDF

def read_pdf_text(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def split_text(text, max_length):
    # Split the text into smaller chunks based on max_length
    tokenizer = AutoTokenizer.from_pretrained("DeepChem/ChemBERTa-zinc-base-v1")
    tokens = tokenizer.encode(text, truncation=False)
    chunks = [tokens[i:i + max_length] for i in range(0, len(tokens), max_length)]
    return chunks

# Use the ChemBERTa-zinc-base-v1 tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("DeepChem/ChemBERTa-zinc-base-v1")
model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-large-squad2")

question = "What is the temperature for Ba3Cu15.3S7.5Te3.5 to have a power factor of 4.6mW?"
pdf_path = 'Paper 1.pdf'
text = read_pdf_text(pdf_path)

# Split the text into manageable chunks
max_length = 512
chunks = split_text(text, max_length)

answers = []
for chunk in chunks:
    inputs = tokenizer(question, tokenizer.decode(chunk), return_tensors="pt", truncation=True, max_length=max_length)
    with torch.no_grad():
        outputs = model(**inputs)

    answer_start_index = outputs.start_logits.argmax()
    answer_end_index = outputs.end_logits.argmax()
    predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
    answer = tokenizer.decode(predict_answer_tokens, skip_special_tokens=True)
    print(chunk)
    print(answer)
    answers.append(answer)

# Combine answers from all chunks
final_answer = " ".join(answers)
print("Final Answer:", final_answer)
