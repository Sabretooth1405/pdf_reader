# pdf_reader

![Alt text](/schema.png?raw=true "Database Schema")
[Video Description](https://drive.google.com/file/d/1N68omw8ApfFGBofrtjqcfRknG48TmsSp/view?usp=sharing)

# Description
- Supports pdfs and images(ideally png)
- Uses pytessaract for ocr
- UI made by html,css and bootstrap (made by me)
- Pls give suggestions for improving image recognition espaxially in case of larger files

# Installation
 - Clone the repo
 - After that install the requirements
 ```
 pip install - r requirements.txt
 ```
 
 - ### Note  Pytessaract has pytorch as its dependency which may vary based on system hardware.Be sure to check out [torch](https://pytorch.org/) version for your system
 - Create your own postgress instance
 - Follow standard django steps
 - Add PDF_ROOT in seetings.py
 - create a .env and add your secret keys
 - Run with standard django steps
