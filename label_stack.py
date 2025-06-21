from zenml.client import Client

client = Client()
stack = client.get_stack("local-mlflow-stack-prices-new")
client.update_stack(stack.name, labels={"zenml:full_stack": "True"})

print(f"Labels updated for stack: {stack.name}")
