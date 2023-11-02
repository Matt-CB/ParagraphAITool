import os
import openai
import streamlit as st
import trafilatura
from langchain import PromptTemplate, OpenAI, LLMChain

# Definition of the style
custom_css = """
<style>
.title-text {
    color: #0077B6;  /* Cambia el color del subtítulo a un azul más claro */
}
</style>
"""

st.sidebar.write("This program uses the OpenAI API to function. Please enter your API key below to use the program. ")
OPENAI_API_KEY = st.sidebar.text_input("API KEY:")

class WebContentSummarizerApp:
    def __init__(self):
        st.title("WebContent Summarizer")
        # Insert the custom CSS into the application
        st.markdown(custom_css, unsafe_allow_html=True)
        # Use a CSS class for the subtitle
        st.markdown('<p class="title-text">With just a simple URL, simplify your online research and content consumption. '
                    'This AI tool extracts and condenses the essential information from web pages into a concise, easy-to-read paragraph.</p>', unsafe_allow_html=True)
        self.url = st.text_input("Paste or type the URL you want to summarize:")
        self.run_button = st.button("Summarize")

    @staticmethod
    def scrape_website(url):
        downloaded = trafilatura.fetch_url(url)
        main_text = trafilatura.extract(downloaded)
        return main_text

    def run(self):
        if self.run_button:
            if self.url:
                url = self.url
                with st.spinner("Getting information from the page..."):
                    self.text = self.scrape_website(url)
                with st.spinner("Analyzing and organizing..."):
                    result = self.llm_text_insight()
                st.write("Summarized content:")
                st.write(result)
            else:
                st.warning("Please enter a valid URL and your OpenAI API Key.")

    def llm_text_insight(self):
        openai.api_key = OPENAI_API_KEY
        text = self.text

        # Split the text into smaller fragments
        max_length = 4096
        chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]

        results = []

        template = """
        Please take the following text interprete and transform it into an organized paragraph for a study. 
        Ensure that the paragraph is clear and coherent. If necessary, add or rearrange ideas to achieve a logical structure. 
        The text is as follows:

        text: {input}

        Make sure the text is only one paragraph
        """

        llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
        prompt_template = PromptTemplate.from_template(template=template)
        chain = LLMChain(llm=llm, prompt=prompt_template)

        for chunk in chunks:
            result = chain.predict(input=chunk)
            results.append(result)

        # Check if results contain more than one paragraph and final result
        if len(results) > 1:
            alternate_input = " ".join(results)

            llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
            prompt_template = PromptTemplate.from_template(template=template)
            chain = LLMChain(llm=llm, prompt=prompt_template)
            result = chain.predict(input=alternate_input)

            return result


        else:
            # Concatenation of the results
            return " ".join(results)


if __name__ == "__main__":
    app = WebContentSummarizerApp()
    app.run()
