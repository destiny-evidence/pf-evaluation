# Evaluation infrastructure

Examples that use promptflow to develop and evaluate classification tasks using LLMs

## Installation

Clone the repository

```
git clone git@github.com:destiny-evidence/pf-evaluation.git
```

Then use [uv](https://docs.astral.sh/uv/getting-started/installation/) to set up the virtual environment

```
uv sync
```

### (Optional) run local models

If you want to use models you run locally, you will need a way to do this. Ollama provides a simple way to get started using LLMs for inference (generating text based on your prompts)

- Install Ollama using the guidance provided [here](https://ollama.com/download)

- Download models

```
ollama run gemma3:1b
```

### (Even more optional)

Install VSCode and the promptflow extension

## Quickstart

### Add a connection

Add a connection following the guidance in the promptflow [docs](https://microsoft.github.io/promptflow/how-to-guides/manage-connections.html)

If you are using ollama, you will need to set base url (e.g.)

```
base_url: "http://127.0.0.1:11434/v1"
```

You will also need to set the API key to a value, but this can be any string and will have no effect (and this does not need to be kept secret)

If you are using OpenAI, you will need to set the api_key. Promptflow can store this for you in encrypted form.

### Edit connection in classify_binary

[classify_binary/flow.dag.yaml](classify_binary/flow.dag.yaml) describes an example flow to use an LLM to make a binary classifier.

Edit the line 

```
  connection: ollama-wsl
```

setting the value to whatever you have named your connevtion

### Edit the prompt

Edit the file [classify_binary/templates/prompt-template.jinja2](classify_binary/templates/prompt-template.jinja2) to whatever you would like.

### Run the prompt on the data

```
pf run create --file flows/classify.yaml
```

### See the metrics of your run

[results/results.ipynb](results/results.ipynb) pulls the results from the promptflow database, filtering according to tags you set, and puts the metrics into a table

## Design

This system should make it easy to run experiments that develop prompts to classify texts with LLMs, and to evaluate how well models - with a given prompting strategy - can classify those texts.

Each time a model is run, this is logged. This should allow for a systematic and scientific approach to prompt development, while maintaining the ability to iterate.

The system should manage datasets such that development of prompts and evaluation are strictly separated.

## Todos

- Dataset manager (python node): manage development and evaluation data.
- Evaluation report (fasthtml?) Shareable?
- Other tasks

## Concepts

### Experiment

defines an experimental context

- collection of records (import?)
- human annotations (enhancement)

### Run

created by user defining model and prompt

model-prompt applied to all records in validation dataset

### Evaluating an experiment

Selects best model-prompt combination from validation dataset, and runs on test dataset

Explorable evaluation report