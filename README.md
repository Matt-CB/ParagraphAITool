# ParagraphAITool - A Web Application for Web Page Summarization

#### __If you want to use the application directly, you can access this link where the program is deployed__ [Web link](https://huggingface.co/spaces/Matt-CB/ParagraphAITool)


## Introduction

**ParagraphAITool** is a web application designed to make online research and content consumption more efficient. It utilizes the power of Language Models (AI) to extract key information from web pages and transform it into concise paragraphs. With a simple input of a URL, this tool condenses essential content, simplifying your online research.

## Features

- Web page summarization: Extracts and condenses the essential information from web pages into a concise, easy-to-read paragraph.
- Easy to use: Simply paste or type the URL you want to summarize and click the "Summarize" button.
- Customizable: Utilizes OpenAI's GPT-3 language model, which can be configured with various options.
- Streamlined interface: Provides a clean and user-friendly interface for a seamless experience.

## Getting Started

To get started with the ParagraphAITool, you'll need to have Python installed on your system. You can then follow these steps:

1. Clone this GitHub repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Configure your OpenAI API Key (see [API Key Configuration](#api-key-configuration)).
4. Run the application with `streamlit run app.py`.

## Usage

1. Enter a valid URL into the provided input field.
2. Click the "Summarize" button.
3. The tool will fetch information from the webpage, analyze and organize it using OpenAI's language model, and display the summarized content.

## API Key Configuration

This program relies on the OpenAI API to function. To configure your API key, follow these steps:

1. Visit the [OpenAI website](https://openai.com/).
2. Sign up or log in to your OpenAI account.
3. Create an API key if you don't have one.
4. Copy the API key.
5. Open the ParagraphAITool application.
6. Paste the API key into the provided input field in the sidebar.

## How it Works

The application works as follows:

1. It takes a user-provided URL as input.
2. It extracts the main text content from the webpage using the `trafilatura` library.
3. The extracted text is divided into smaller chunks to fit within the constraints of the OpenAI language model.
4. The application uses the OpenAI GPT-3 language model to interpret and transform the text into an organized paragraph.
5. The resulting paragraphs are displayed as the summarized content.

## Technologies Used

The ParagraphAITool is built using the following technologies:

- Python
- Streamlit
- Trafilatura
- OpenAI GPT-3 Language Model

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the GitHub repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, concise messages.
4. Push your changes to your fork.
5. Create a pull request to the main repository.


