# python-minis
Mini projects for small investigations and learning.
Some projects will use some common functions from the utils module.
Some projects will use the OpenAI API.


## Table of Contents

- [Projects](#projects)
- [Setup](#setup)

## Projects

- [WiP] `eval-hate-speech`: Investigations and evaluations of a hate speech dataset 
- [WiP] `data-query-chatbot`: A chatbot that can answer questions about a dataset with numeric measurements.

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/mstankai/python-minis.git
    cd python-minis
    ```

1. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

1. **Install dependencies :**
    ```sh
    pip install -r requirements.txt
    pip install -e . --use-pep517
    ```

1. **Set up OpenAI API key:**
    You can set up an API key on the Open AI Platform page, here: [OpenAI Platform | API Keys](https://platform.openai.com/api-keys).

    Store your OpenAI API key in your system's keychain using the following command:
    ```sh
    python -c 'import keyring; keyring.set_password("system", "openai_api_key", "<your-api-key>")'
    ```sh
