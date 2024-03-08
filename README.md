# Code Bot

I have used a quantized model version of Mistral to run locally on CPU. You can download that from - https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q5_K_S.gguf
save the model in models folder and ensure you change the model path in main.py

## Installation & Setup:

1. **Clone the Repository**:
   ```bash
   git clone [URL of your repository]
   ```

2. **Navigate to the Cloned Directory**:
   ```bash
   cd path_to_directory
   ```
3. **Create a New Virtual Environment (Optional but Recommended)**:
   - For virtualenv:
     ```bash
     virtualenv venv
     source venv/bin/activate  # On Windows use: venv\Scripts\activate
     ```
   - For conda:
     ```bash
     conda create --name chatloom_env python=3.8
     conda activate chatloom_env
     ```

4. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Setting up Environment Variables**:
   - Rename the `.env_sample` file to `.env`.
   - Open the newly named `.env` file in any text editor of your choice.
   - Locate the placeholder for the OpenAI API key and replace it with your actual key.

## Usage:

After completing the above steps, run the following in Terminal: 
  ```bash
  chainlit run main.py -w
  ```
