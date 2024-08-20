# ID Document Information Recognizer

## Overview

The ID Document Information Recognizer is a Python-based application designed to extract and display information from images of identification documents. Initially, this project focuses on French ID cards (Carte Nationale d'Identité) and UK identity documents. The goal of the project is to automate the extraction of key details such as surname, name, birth date, and ID number from scanned or photographed images of these documents.

## Features

- **Image Processing**: Load an image of a French ID card or UK identity document and extract text from it.
- **Text Extraction**: Identify and extract specific fields from the text, including:
  - Surname
  - Name
  - Birth Date
  - ID Number
- **User Interface**: A simple interface to input the image file name and display the extracted information.
- **Document Support**: Handles both French and UK identification documents, adapting the extraction process based on the type of document.

## Project Goals

The primary goal of this project is to streamline the process of extracting information from ID documents, reducing the need for manual data entry and increasing accuracy. By automating text extraction using OCR, the project aims to simplify tasks related to document verification and data processing.

## Potential Applications

- **Document Verification**: Automate the verification process for identification documents, which can be useful in scenarios such as user onboarding or authentication.
- **Data Entry Automation**: Reduce the time and effort required for manual data entry from scanned documents.
- **Integration with Other Systems**: The extracted information can be integrated into other systems for further processing, such as creating user profiles or updating databases.

## Example

Here’s a brief demonstration of how the application works:

![Application Demo](gif/gif.gif)

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/AmineBennani7/id-recognizer.git

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt

3. **Run the app**:
   ```sh
   python main.py

   
   


