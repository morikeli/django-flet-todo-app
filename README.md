# django-flet-todo-app
A todo app built with django API and Flet

## Overview
This is a desktop to-do application built with Django REST Framework and Flet.

Technologies used:
  - django REST Framework
  - Flet
  
For more info about Flet, click this ![link](https:flet.dev)

## Developer instructions
1. Open terminal and clone this repo using Git.
   ```bash
   cd Desktop    # or your preferred location 
   git clone https://github.com/morikeli/django-flet-todo-app.git
   ```
2. Open the cloned repo in your preferred IDE or code editor, e.g VS Code.
3. Open terminal, activate a virtual environment and install Python modules.
   ```bash
   python3 -m venv .venv    # You can also use python -m venv .venv

   # activate virtual ennvironment
   source .venv/bin/activate    # In windows, use .venv\Scripts\activate

   # install python packages using pip
   pip install -r requirements.txt
   ```

4. Run the app and the API
   ```bash
   # to run development server for the API
   python manage.py runserver

   # Open a separate terminal to run the Flet application
   flet -r app/main.py
   ```

## User instructions
Once the app is executed, type a task you plan to do, in the text field. Click the "+" button  to add the task. To get all scheduled tasks, click the other button with a radar icon.

## Contribution
The project is no longer maintained because I switched from Flet to Flutter. If you face any issue, kindly do research on how the problem can be solved.

