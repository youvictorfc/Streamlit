import openai

import streamlit as st



# Initialize the OpenAI API client

openai.api_key = "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"



# Define the function to generate a product description

def generate_description(product_name):

    response = openai.Completion.create(

        engine="text-davinci-002",

        prompt=f"Write a description for the product '{product_name}':",

        max_tokens=100,

        n=1,

        stop=None,

        temperature=0.5,

    )



    message = response["choices"][0]["text"].strip()

    return message



# Define the Video Studio app

def product_description_app():

    product_name = st.text_input("Enter product name:")

    if product_name:

        description = generate_description(product_name)

        st.write("Product Description:", description)



# Start the Video Studio app

if __name__ == "__main__":

    product_description_app()

