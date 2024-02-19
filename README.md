# kengen3
KenGen, plus mathematical ability &amp; internet access, based on Llama 2.

## Concept
Many Large Language Models face issues with solving mathematical problems, often attempting to solve it, but often getting a couple digits wrong. KenGen-3 uses a wrapper using technology Kendasi invented to allow it to solve math problems. What's more, it has access to the internet, but unlike existing models, it doesn't use it when it's completely unnecessary - only when it's actually needed. What's more, it can be up to 14,000% faster than GPT-4 and larger models.

## To do
A few things need to be done still:

* Move onto new servers
* Switch to LlaMA-2 Chat 7B model
* Set up API

## The "how?"
KenGen uses the smallest Llama-2 Chat-finetuned model, with 7 billion parameters. While it's small, with the added functionality added above, it still can produce very high quality results, even with a small model, allowing for cheaper and faster computation. The added functionality uses a custom wrapper developer by Kendasi. At the moment, it's still using OpenAI's API for the base model, but that will be switched out for Llama once the servers have been set up, as it costs money to run.

Regarding the internet, KenGen uses the Brave API to access the internet and collect data from the internet. KenGen has been finetuned to understand special tags such as <kgmath> and <kgweb>, used like XML tags, which is then simply formatted to be the answer calculated (kgmath) or found on the internet (kgweb) from the query that the model entered within the tags.
