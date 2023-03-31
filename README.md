# <img src="https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif?cid=ecf05e47a0n3gi1bfqntqmob8g9aid1oyj2wr3ds3mg700bl&rid=giphy.gif" width ="25"> <b>Strava CLI</b> - **Browse Strava stats from the command line**

### Tech Stack
**`Python3` `SQLAlchemy` `Alembic` `SQLite` `Pandas`**

I created Strava CLI at the end of Phase 3 in my bootcamp. As an avid Strava user myself, my idea was to comprise a database of personal, live data that can be synced regularly. It is the culmination of a 3 week journey of learning Python.

The application utilizes the publicly available Strava API for fetching profile and activities data into the application and storing it locally in a SQLite database. I then use that data to aggregate some additional stats that are not part of the original Strava app. One of the constraints my instructor imposed was that we build a Python app with a command line interface.

### Future goals include:

❖ Building a React Frontend

❖ Creating a 'sign up/login' workflow that obtains an `API token`

❖ Upgrading the database to `PostgreSQL`

❖ Deployment

## User Stories

Upon starting the app, the user is asked to select a username from a list. Then, they are presented with 6 main options:

<img width="557" alt="Screenshot 2023-03-31 at 11 24 00 AM" src="https://user-images.githubusercontent.com/17399666/229188390-aacffa4f-e5c9-4862-9073-41f7ae31ca95.png">

These will be henceforth referred to as top-level options.

### 1) Profile Details

Upon selecting the first top-level option, the user is presented with information about the selected profile, like so:

<img width="441" alt="Screenshot 2023-03-31 at 9 58 47 AM" src="https://user-images.githubusercontent.com/17399666/229171076-10f2ca6c-4682-40cf-b1a1-b87c6ed6c6f2.png">

❖ An option to edit profile details is offered, which allows change to weight, bio and location. Changes are reflected in database.
 
### 2) Aggregated Stats

Upon selecting the second top-level option, the user is presented with information about aggregated stats sorted and displayed by the type of activity, like so:

<img width="1231" alt="Screenshot 2023-03-31 at 11 28 37 AM" src="https://user-images.githubusercontent.com/17399666/229189228-55347469-8f0f-4d69-a7dc-fc7f20f0c853.png">

❖ This is a feature that is not offered by the Strava API.
 
### 3) List of Achievements

Upon selecting the third top-level option, the user is presented with a choice between:

❖ Viewing "All Achievements" - this is a list of all achievements that have been created in the database with various parameters. Upon selecting this option, the list with each earnable Achievement's name appears.
 
❖ Viewing "Achievements Earned" specific to the profile:

<img width="1105" alt="Screenshot 2023-03-31 at 11 59 04 AM" src="https://user-images.githubusercontent.com/17399666/229195330-6b2ac469-cfb7-4171-bb69-4c188a8b8735.png">

❖ This option is referencing a table that is a join of 3 others: Profile, Activities & Achievements.

❖ To "earn" an achievement a user needs to upload/complete an activity that satisfies certain criteria as described in the Achievement.

### 4) List of Activities

Upon selecting the fourth top-level option, the user is presented with a choice between:

❖ Viewing "All Activities" - this is a list of all activities uploaded by the user and stored in the database.

❖ Viewing "Activities by Type" - this is a list of activities filtered by Activity Type. Another option is presented for selection of Activity Type.

❖ Viewing "Last 10 Activities" - this is a list of the last 10 uploaded activities.

<img width="817" alt="Screenshot 2023-03-31 at 11 57 22 AM" src="https://user-images.githubusercontent.com/17399666/229194975-842afa53-c9d5-4f43-b01c-83a34091a460.png">

### 5) Fetch New Data From Strava

Upon selecting the fifth top-level option, a function is fired that fetches new data, recalculates and repopulates the tables so that they are up-to-date with the data from Strava. User is then prompted to restart the app to load the updated data. A "Last Updated" indicator is presented on the same line for user's consideration.

### 6) Logout

Yeah.

## How To Run The App 

You're welcome to explore the app through Github or fork/clone it to test yourself. Below are the steps for running the app on your local machine:

❖ Before you start, make sure you obtain your own [`Strava API Key`](https://developers.strava.com)

❖ Clone/fork the repo.

❖ After you've done so, make sure you are running [`Python 3.11`](https://www.python.org/downloads/release/python-3110/)

❖ Navigate to the Root folder where the `Pipfile` file is located.

❖ Run `pipenv install` then enter the shell with `pipenv shell`

❖ Type `python main.py` to start the application.

***Please reach out if you run into hurdles or have questions regarding the setup***

















