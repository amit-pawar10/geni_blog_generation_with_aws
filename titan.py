import boto3
import json

prompt_data="""
Act as a Shakespeare and write a poem on Genertaive AI
"""

bedrock=boto3.client(service_name="bedrock-runtime")

payload={
    "inputText":prompt_data,
    "textGenerationConfig":{
        "maxTokenCount":4096,
        "stopSequences":[],
        "temperature":0,
        "topP":1}
}
body=json.dumps(payload)
model_id="amazon.titan-text-lite-v1"
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
repsonse_text=response_body.get('results')[0].get('outputText')
print(repsonse_text)