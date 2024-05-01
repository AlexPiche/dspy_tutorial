## Create conda environment

```bash
    conda env create -f environment.yml
```

## Serve Llama3 8b with VLLM

```bash
    python -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Llama-3-8B --port 8080
```

## Test yout setup

```bash
    python test_setup.py
```