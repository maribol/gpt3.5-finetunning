import requests
import json
import time
import sys
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.openai.com/v1"

FINETUNE_FILE = "./data.jsonl"

if(len(sys.argv) > 1):
    FINETUNE_FILE = sys.argv[1]

HEADERS = {
    "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY")
}

def upload_finetuning_file(file_path):
    print(f"Uploading file {file_path}...")

    with open(file_path, 'rb') as f:
        response = requests.post(f"{BASE_URL}/files",
                                 headers=HEADERS,
                                 files={"file": f},
                                 data={"purpose": "fine-tune"})
    return response.json()

def check_file_status(file_id):
    response = requests.get(f"{BASE_URL}/files/{file_id}", headers=HEADERS)
    return response.json()

def create_finetuning_job(file_id):
    print(f"Creating fine-tuning job for file {file_id}...")
    data = {
        "training_file": file_id,
        "model": "gpt-3.5-turbo-0613"
    }
    response = requests.post(f"{BASE_URL}/fine_tuning/jobs",
                             headers={**HEADERS, "Content-Type": "application/json"},
                             data=json.dumps(data))
    return response.json()

def check_finetuning_job_status(job_id):
    response = requests.get(f"{BASE_URL}/fine_tuning/jobs/{job_id}", headers=HEADERS)
    return response.json()

def save_model_to_json(job_data, output_file):
    print(f"Saving fine-tuning model data to {output_file}...")
    with open(output_file, 'w') as f:
        json.dump(job_data, f, indent=4)

def main():

    # Upload fine-tuning file
    response = upload_finetuning_file(FINETUNE_FILE)
    print(f'File uploaded: {response.get("filename")}')

    file_id = response.get("id")

    # make a copy of finetunning.jsonl to fine_tuned_data {name}.jsonl
    with open(FINETUNE_FILE, "r") as f:
        data = f.read()

    # save a copy of the finetune file
    folder_path = FINETUNE_FILE.split("/")[0]
    with open(f"{folder_path}/{file_id}.jsonl", "w") as f:
        f.write(data)

    # Create a fine-tuning job
    response = create_finetuning_job(file_id)
    job_id = response.get("id")

    print('Processing takes about 20 minutes...')
    time.sleep(60)

    # Check if file is processed
    status = "uploaded"
    times = 0
    while status != "processed":
        times += 1
        print(f"Waiting for file to be processed ({times}). Current status is {status}..")
        time.sleep(30)  # Wait for 10 seconds before checking again
        response = check_file_status(file_id)
        status = response.get("status")

    # Check fine-tuning job status until succeeded
    status = "running"
    times = 0
    while status != "succeeded":
        times += 1
        print(f"Waiting for fine-tuning job to complete ({times}). Current status is {status}..")
        time.sleep(30)  # Wait for 10 seconds before checking again
        response = check_finetuning_job_status(job_id)
        status = response.get("status")

    name = response.get("fine_tuned_model")

    # Save fine-tuning model data to JSON
    save_model_to_json(response, f"fine_tuned_model {name}.json")

if __name__ == "__main__":
    main()