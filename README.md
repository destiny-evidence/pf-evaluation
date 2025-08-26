# Evaluation infrastructure

Examples that use promptflow to develop and evaluate classification tasks using LLMs

## Installation

UV

### (optional) local models

- Ollama

- Download models

### Add a connection

If using local connection, set Base API

If using OpenAI, 

### Edit connection in classify_binary




## Design

This system should make it easy to run experiments that develop prompts to classify texts with LLMs, and to evaluate how well models - with a given prompting strategy - can classify those texts.

Each time a model is run, this is logged. This should allow for a systematic and scientific approach to prompt development, while maintaining the ability to iterate.

The system should manage datasets such that development of prompts and evaluation are strictly separated.

## Todos

- Dataset manager (python node): manage development and evaluation data.
- Tag runs
- Evaluation report

## Concepts

### Experiment

defines an experimental context

- collection of records (import?)
- human annotations (enhancement)

### Trial

created by user defining model and prompt

model-prompt applied to all records in validation dataset

### Evaluating an experiment

Selects best model-prompt combination from validation dataset, and runs on test dataset

Explorable evaluation report