from llama_cpp import Llama

HUGGINGFACE_MODEL="NousResearch/Hermes-2-Pro-Llama-3-8B-GGUF"
HUGGINGFACE_MODEL_FILE="Hermes-2-Pro-Llama-3-8B-Q4_K_M.gguf"

llm = Llama.from_pretrained(
    repo_id=HUGGINGFACE_MODEL,
    filename=HUGGINGFACE_MODEL_FILE,
    chat_format='llama-3',
    verbose=False
)


output = llm.create_chat_completion(
      messages = [
          {"role": "system", "content": "You are an assistant who clearly explains statistical concepts."},
          {
              "role": "user",
              "content": "What is the difference between L1 and L2 regularization?"
          }
      ]
)

print(output)