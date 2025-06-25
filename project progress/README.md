# 🧱 ZenML + MLflow Local Stack Setup Guide (2025)

This guide walks you through the complete process to set up a local ZenML stack with MLflow as the experiment tracker and model deployer.

---

## ✅ Prerequisites

- Python ≥ 3.8
- Virtual environment (e.g., `venv`)
- ZenML installed:
  ```bash
  pip install "zenml[server]"
  ```
- MLflow tracking server running locally on `http://127.0.0.1:5000`

---

## 📦 1. Set up a virtual environment and install ZenML

```bash
python -m venv venv
source venv/bin/activate
pip install "zenml[server]"
```

---

## 🛠️ 2. Initialize a ZenML project

```bash
zenml init
```

---

## 📂 3. Start the local ZenML server (optional but recommended)

```bash
zenml up
```

This starts:
- The ZenML dashboard: [http://127.0.0.1:8237](http://127.0.0.1:8237)
- A default local ZenML server instance

---

## 🧪 4. Register the MLflow experiment tracker

```bash
zenml experiment-tracker register mlflow_tracker_prices_new \
  --flavor=mlflow \
  --tracking_uri=http://127.0.0.1:5000 \
  --tracking_token=None
```

✅ Verify:
```bash
zenml experiment-tracker list
```

---

## 🚀 5. Register the MLflow model deployer

```bash
zenml model-deployer register mlflow_prices_new --flavor=mlflow
```

✅ If you see an error like:
```
EntityExistsError: ... with name 'mlflow_prices_new' ...
```
It means the component is already registered — this is fine.

---

## 🧩 6. Register the full ZenML stack

```bash
zenml stack register local-mlflow-stack-prices-new \
  -a default \
  -o default \
  -e mlflow_tracker_prices_new \
  -d mlflow_prices_new
```

✅ Check it:
```bash
zenml stack list
zenml stack describe local-mlflow-stack-prices-new
```

---

## 🏷️ 7. Add labels to the stack

Since CLI doesn't support labels directly, use Python:

### Create file: `label_stack.py`
```python
from zenml.client import Client

client = Client()
stack = client.get_stack("local-mlflow-stack-prices-new")
client.update_stack(stack.name, labels={"zenml:full_stack": "True"})

print(f"Labels updated for stack: {stack.name}")
```

### Run it:
```bash
python label_stack.py
```

✅ Optional check:
```python
print(client.get_stack("local-mlflow-stack-prices-new").labels)
```

---

## ✅ Final Sanity Check

Make sure:
```bash
zenml stack list
zenml stack describe local-mlflow-stack-prices-new
```

You should see:
- Artifact store: `default`
- Orchestrator: `default`
- Experiment tracker: `mlflow_tracker_prices_new`
- Model deployer: `mlflow_prices_new`
- Labels: `{zenml:full_stack: True}`

---

## 🧪 You're Ready!

You can now start building and running pipelines using your new stack:

```bash
zenml stack set local-mlflow-stack-prices-new
```
