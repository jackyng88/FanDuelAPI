# FanDuel

## Installation 

### 1. All of the sections here use Python (Python 3.7.x specifically)

### 2. (Recommended) Installing/using a Python Virtual Environment - 
       A. Clone from github
       B. Using any terminal/command-prompt browse to the folder containing "requirements.txt" and create the virtual environment - 
          python -m venv venv
          Note -
          You can change the name of the last venv to whatever you want since it will be the name of the folder.
          Also,depending on how you alias your Python you might have to use python3 -m venv venv)
       C. Activate the virtual environment - 
          (Linux/Mac) source venv/bin/activate
          (Windows) .\venv\Scripts\activate
          
### 3. Install python dependencies - 
       A. In the folder with "requirements.txt" in terminal/cmd run - 
          pip install -r requirements.txt
          


## (1 - FanDuel REST API)


### 1. Traverse to 'FanDuelAPI' folder that contains 'manage.py' in terminal/command-prompt 

### 2. Start the Django development server by running this command - 
       (Linux/Mac) python manage.py runserver
       (Windows) python .\manage.py runserver
         
### 3. Open the API in web-browser/Postman/whatever with the below address - 
       127.0.0.1:8000/
       
### 4. Admin endpoint credentials in case you want to use it - 
       127.0.0.1:8000/admin/
       id - admin
       password - password123
       
### 5. Django REST Framework gives us access to a Browsable-API in your web browser - 
       A. NBA API root - 
          127.0.0.1:8000/nba/
          You can see a list of possible endpoints.
          
       B. Teams - 
          127.0.0.1:8000/teams/
          127.0.0.1:8000/teams/1/
          
          You can replace the 1 for any primary key in the endpoint
          
       C. Players - 
          127.0.0.1:8000/players/
          127.0.0.1:8000/players?date=01012016 (date query parameter must be in MMDDYYYY form)
          127.0.0.1:8000/players/1/
          127.0.0.1:8000/players/1/stats/
          
          - You can replace the date query parameter with a date in the form of MMDDYYYY
          - You can replace the integer keys in the URL parameter with a primary key, and also with /players/pk/stats/
          
          
       D. Games - 
          127.0.0.1:8000/games/
          127.0.0.1:8000/nba/games?date=01012016
          127.0.0.1:8000/nba/games/1/
          
          - Again you can filter the date with date=MMDDYYYY format.
          - You can filter games/1/ with a game_id of your choosing.
          
          
 ### 6. Follow-up Answers
        The follow-up explanation portion is answered in the '1 - API Follow-up Question.docx' file.
          
          
 
 ## (2 - Data Model)
 
 ### You can view the Data model in the 'data model.docx' file as well as a mockup in 'ERD Data Model.png'
 
 
 
 ## (3 - Depth Chart)
 
 ### 1. Run the Depth Chart script by browsing to the '3 - Depth Chart/' folder and running - 
        python main.py
        
 ### 2. At the top of 'main.py' source-code in a docstring there's some more information about additional requirements for exercises
        A and B from the challenge doc file.
        
 ### 3. There are sample function calls at the bottom of the source code. But, you can adjust the function calls as you see fit to test.
 
 
 
 ## (4 - March Madness)
    Note - has provided sample file in 'brackets-00.csv' that is then altered to 'teams.csv' for use.
 
 ### 1. Traverse to the '4 - March Madness/' Folder and run the below - 
        python brackets.py
        
 ### 2. Currently there are some test function calls at the bottom again that have hard-coded file names. You can replace these if you wish.
 
 ### 3. The functions create_teams(file) and playtournament(bracket, teams) are necessary for the script to function so make sure those are run first before you run these functions (is_bracket_complete(), find_champion(), and champions_path_to_victory()). 
        
    
   
   
