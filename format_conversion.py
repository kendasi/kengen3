dialog = [
    {"role": "system", "content": "You are a friendly AI assistant."},
    {"role": "user", "content": "What's the tallest mountain in the world?"},
    {"role": "assistant", "content": "Mt everest, probs. IDK dude."},
    {"role": "user", "content": "You should really know, you're an AI man."}
]
formatted = ""
for side in dialog:
  if (side["role"] == "system"):
    formatted = formatted + "<<SYS>>\n" + side["content"] + "\n<</SYS>>\n\n"
  else:
    formatted = formatted + "[INST]" + side["content"] + "[/INST]"
print(formatted)
