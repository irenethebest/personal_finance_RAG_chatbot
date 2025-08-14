# Databricks notebook source
# MAGIC %pip install openai

# COMMAND ----------

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-api-key-here"  # Replace with your actual API key

# COMMAND ----------

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)


# COMMAND ----------


