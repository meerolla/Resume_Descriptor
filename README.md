# Resume_Descriptor

To set up the project locally:

1. clone the project

   git clone https://github.com/meerolla/Resume_Descriptor.git

2. Then, create a virtual environment called virtualenv using the Python’s built-in venv module:

   python -m venv virtualenv

3. Next, activate the virtual environment as follows:

   On Windows, run: .\virtualenv\scripts\activate

   On Unix or MacOS, run: source virtualenv/bin/activate

4. Install dependencies

   pip install requirements.txt

5. Note: Create .env file with below content, so that the code will use your openAI key to interact with llms

   OPENAI_API_KEY="YOUR_OPENAI_KEY"

6. Run the Streamlit demo locally:

   streamlit run main.py



