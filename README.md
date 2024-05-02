# dspy tutorial

## Quick start

### Create conda environment

```bash
conda env create -f environment.yml
```

optionally, you can install flash-attn with pip

```bash
pip install flash-attn
```

### Serve Llama3 8b with VLLM

```bash
python -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Llama-3-8B-Instruct --port 8080
```

### Test yout setup

```bash
python test_setup.py
```

## Outputs

You can check the prompts folder to see the best prompts.


## Additional resources

* Check out the tutorials: https://github.com/stanfordnlp/dspy?tab=readme-ov-file#a-tutorials
* Documentation: https://dspy-docs.vercel.app/
* Weaviate RAG tutorial: https://weaviate.io/blog/dspy-optimizers 