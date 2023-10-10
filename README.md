# Readme

## Introduction
This code is a Python script that interacts with the OpenAI API to perform fine-tuning on a GPT-3.5 Turbo model. It allows you to upload a fine-tuning file, create a fine-tuning job, and check the status of the job until it is completed. The script also saves the fine-tuning model data to a JSON file.

## Prerequisites
Before running the code, make sure you have the following:

- Python installed on your machine
- The required Python packages: requests, json, time, sys, os, dotenv
- An OpenAI API key

## Setup
To set up the code, follow these steps:

1. Install the required Python packages by running the following command:
   ```
   pip install requests json time sys os dotenv
   ```

2. Create a file named `.env` in the same directory as `app.py`.

3. Open the `.env` file and add your OpenAI API key in the following format:
   ```
   OPENAI_API_KEY=<your_api_key>
   ```

## Usage
To use the code, follow these steps:

1. Create a file named `data.jsonl` and add your training data in the following format:
   ```
   {"messages":[{"role":"system","content":"You are a sarcastic friend"},{"role":"user","content":"What have you been up to today?"},{"role":"assistant","content":"Oh, you know, just saving the world from impending doom. No biggie."}]}
   ...
   ```

2. Run the `app.py` script by running the following command:
   ```
   python app.py
   ```

3. The script will upload the fine-tuning file, create a fine-tuning job, and check the status of the job until it is completed. The progress will be displayed in the console.

4. Once the fine-tuning job is completed, the script will save the fine-tuning model data to a JSON file named `fine_tuned_model <job_name>.json`.

## Customization
You can customize the behavior of the script by modifying the following variables:

- `BASE_URL`: The base URL for the OpenAI API.
- `FINETUNE_FILE`: The path of the fine-tuning file. By default, it is set to `./data.jsonl`, but you can specify a different path as a command-line argument when running the script.

## Conclusion
This code provides a convenient way to perform fine-tuning on a GPT-3.5 Turbo model using the OpenAI API. By following the setup and usage instructions, you can easily upload a fine-tuning file, create a fine-tuning job, and save the fine-tuning model data to a JSON file. Feel free to customize the code to suit your specific needs.