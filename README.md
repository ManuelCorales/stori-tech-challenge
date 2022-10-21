# Stori-tech-challenge
This is the challenge for Stori

## Brief description
The system was programmed in Python. And Sqlite was used as database

## Code directories and structure
In the root directory, there is a folder 'account_transactions' that contain the .csv with the transactions
The 'db' folder that contains the database and its creation script
The 'index.py' file which is the entrypoint to the program

Then we have the 'src/lib' directory that contains the main source code of the system
The 'Repositories' folder contains the code for interacting with the database
The 'Services' folder contains the code for executing the more 'general' functions
And finally the 'Entities' folder which contain the classes that have relation to the tables of the database 

## Instructions for running the code
Once the repository is pulled, open a terminal and navigate to the root directory of the project. Then run:

For building docker image
-> 'docker build -t stori-challenge . ' (With the final dot as well)

For running docker container
-> 'docker run --name stori-challenge -dit stori-challenge'

For finally running the code:
-> 'docker exec -ti stori-challenge sh -c "python3 index.py <email account to which the email will be sent >"'.
Ex: 'docker exec -ti stori-challenge sh -c "python3 index.py mcoralesdev@gmail.com"'