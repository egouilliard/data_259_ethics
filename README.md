
# Ethics, Fairness, and Privacy Analysis of LLM’s

This repository includes an analysis on the ethics, privacy, and fairness of LLM's.

## Data
** LLM's analysed**:
1. [ChatGPT](https://chat.openai.com/)(GPT4 & GPT4o)
2. [Gemini](https://gemini.google.com/app)
3. [Copilot](https://copilot.microsoft.com/)
4. [Google BERT on Hugging Face](https://huggingface.co/google-bert/bert-large-uncased-whole-word-masking-finetuned-squad)

### Data collection
In the data folder you will find json files that inlude prompts, answers and categories. The category is the reponse type deduced from the answer given by the LLM.

The `manipulate_responses.csv` file includes a concatination of the json files.

In the `ethics_data` folder you will find datasets that have prompts to train a model on commonsense, deontology, justice, utilartarianism, and virtue. The folder was taken from this [repository](https://github.com/hendrycks/ethics).

## Analysis

You can find a PDF analysis report of the experiment [here](https://github.com/egouilliard/data_259_ethics/tree/main/analysis_report)