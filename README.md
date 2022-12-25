# pdf_reader

![Alt text](/schema.png?raw=true "Database Schema")


# Description
- Supports pdfs and images(ideally png)
- Uses pytessaract for ocr
- UI made by html,css and bootstrap (made by me)

# Installation
 - Clone the repo
 - After that install the requirements
 ```
 pip install - r requirements.txt
 ```
 
 - ### Note  Pytessaract has pytorch as its dependency which may vary based on system hardware.Be sure to check out [torch](https://pytorch.org/) version for your system
 - Create your own postgress instance
 - Follow standard django steps
 - Add PDF_ROOT in settings.py (Location of media folder in your system)
 - create a .env and add your secret keys
 - Run with standard django steps
 ```
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
 ```

# Demo
- [Video Description](https://drive.google.com/file/d/1N68omw8ApfFGBofrtjqcfRknG48TmsSp/view?usp=sharing)
# Report
- My approach was to divide project in 3 parts
  - Create user app for authentication
  - Create pdfs app to handle file upload
  - After upload do text extraction
   - This was the most challenging part as I didn't know much about OCR.I searched online and after testing found the pytessarct module to be most appropriate
  - I also had to learn about postgressql as I had worked with mysql before that
  - I learnt about image recognition and OCR 
