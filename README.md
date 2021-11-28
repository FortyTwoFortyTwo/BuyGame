# BuyGame

## About
I developed a [website](https://fortytwo-buygame.herokuapp.com/) for Code Institute's Full Stack Frameworks with Django Milestone Project. The website's goal is to allow user to view and buy games. The website is designed to be simple and easy to use on any platform or scale.

## Index – Table of Contents
* [Project purpose](#project-purpose)
* [User Experience (UX)](#user-experience)
* [Features](#features)
* [Designs](#designs)
* [Technologies Used](#technologies-used)
* [Database](#database)
* [Testing](#testing)
* [Known Bugs](#known-bugs)
* [Deployment](#deployment)

## User Experience

#### Ideal user

##### The ideal user for this website is:
* Anyone wanting to find a game
* Anyone wanting to buy a game

##### Visitors to this website are searching for:
* A game to buy for a particular platform
* A game to buy on special offer
* New games to find
* Best rating games
* Free games to play
* Find games by category

##### This project is the best way to help them achieve these things because:
* Easy to understand
* Very clear
* Quick filter for different types of games by categories and platforms
* Many different ways to sort list of games
* Free games attracts people
* Very fast site

##### User stories
1. As a new user, I want to find and buy a game
3. As a new user, I want to see a specific category of game
3. As a new user, I want to find a game that supports specific platform
4. As a new user, I want to find new releases
5. As a new user, I want to find most popular games
6. As a new user, I want to find free games
7. As a new user, I want to find good deals

## Features

##### Store page
Product page shows list of game titles that can be clicked for more information.
Product page shows essential infomation.
Shows sorting options, categories and platform filters.

##### Infromation on games
Info page for each game shows more infomation, user can select quantity and platform to add to cart.

##### Cart
List of games in cart to buy, update quantities and remove items in cart.

##### Checkout
Input user name, email, address and card number

## Designs

TODO screenshots

## Technologies used
* HTML5
* CSS3
* Javascript
* Python
* [HTML Validator](https://validator.w3.org) for validity of HTML
* [CSS Validator](https://jigsaw.w3.org/css-validator) for validity of CSS
* [PEP8](http://pep8online.com) for validity of python
* [Django](https://www.djangoproject.com/) for python web framework used for rapid development, maintainable, clean design
* [Stripe](https://stripe.com/) for receiving payments on buying games
* [Psycopg2](https://pypi.org/project/psycopg2/) for Python database adapter
* [Gunicorn](https://gunicorn.org/) for WSGI server implementation used to run Python web application
* [Bootstrap4](https://getbootstrap.com) for the grid layout, components and styling
* [FontAwsome](https://fontawesome.com/) as icon provider
* [Google Fonts](https://fonts.google.com/specimen/Lato) for Lato fonts
* [JQuery](https://jquery.com/) for JavaScript library to simplify HTML DOM manipulation
* [Git](https://git-scm.com) for version control
* [GitHub](https://github.com) for the repository to store the files
* [GitPod](https://gitpod.io) to test and edit the website
* [Heroku](https://dashboard.heroku.com) to deploy the site
* [AWS S3 Bucket](https://store.steampowered.com/) for cloud storage
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) to make use of Amazon S3
* [Pillow](https://python-pillow.org/) for saving image file formats
* [Steam](https://store.steampowered.com/) for games and images used as an example

## Database
The DJango's model relational database is used.

The application uses 3 databases to store list of games, 'Product', 'Category' and 'Platform'.

#### Product
- category (Foreign key for 'Category' assigned to it)
- platforms (Many to many foreign key for 'Platform', lists which platforms is aviable)
- name (Char field for friendly name)
- description (Text field for description)
- price (Decimal field for cost  in GBP, 0.00 for free)
- rating (Integer field for rating between 0 to 100)
- new (Boolean field on whenever if should have "New" label)
- discount (Decimal field on whenever it should have a discount in 0.0 to 1.0 percentage)
- image_url (URL field for link to image)

#### Category
- name (Char field for improper name)
- friendly_name (Char field for name to display)

#### Platform
- name (Char field for improper name)
- friendly_name (Char field for name to display)

## Testing
| Test Label | Test Action | Expected Outcome | Test Outcome |
| --- | --- | --- | --- |
| HTML Validator | Check for any warnings or errors at [HTML Validator](https://validator.w3.org/) | No warnings or errors reported | TODO |
| CSS Validator | Check for any warnings or errors at [CSS Validator](https://jigsaw.w3.org/css-validator/) | No warnings or errors reported | TODO |
| Opening home browser | Opening the home website browser by google chrone, microsoft edge and phones | Home website can be opened | PASS |
| Screen Size | Resizing all website screens for any sizes above 300 pixels | All websites is responsive when screen changes size to fit | PASS |
| Opening all products | Select "All Products" in nav bar | All products shown | PASS |
| Filter product categories | Select any cateogries in nav bar | Only products using selected category shown | PASS |
| Filter product platforms | Select any platforms in nav bar | Only products using selected platform shown | PASS |
| Filter special offers | Select any special offers in nav bar | Only products using selected special offers show | PASS |
| Sorting products | Select "Sort Buy..." in products page | Products sorted by selected sort | PASS |
| Opening game detail page | Select any games in products page | Page about selected game shown | PASS |
| Buying for platform | Select platform that can only be bought for specific game | Can only select platform for specific game | PASS |
| Quantity range | Set quantity count by 1-99 range | Can only set quantity count by 1-99 range | PASS |
| Add to cart | Add game with selected platform and quantity to cart | Game added to cart | PASS |
| Opening cart page | Open cart page from cart icon at top right | Cart page opened with correct amount of games and cost listed | PASS |
| Checkout | Preform checkout | Game is bought | PASS |

## Known Bugs
There are currently no known bugs

## Deployment

#### Running Code Locally
1. Follow this link to my [Repository on Github](https://github.com/FortyTwoFortyTwo/BuyGame) and open it.

2. Click `Clone or Download`.

3. In the Clone with HTTPs section, click the `copy` icon.

4. In your local IDE open Git Bash.

5. Change the current working directory to where you want the cloned directory to be made.

6. Type `git clone`, and then paste the URL you copied earlier.

7. Press enter and your local clone will be ready.

8. Create and start a new environment:  
python -m .venv venv  
source env/bin/activate

9. Install the project dependencies:  
pip install -r requirements.txt

10. Create a new file, called `env.py` and add your environment variables:

import os  
os.environ.setdefault("STRIPE_PUBLISHABLE", "secret key here")
os.environ.setdefault("STRIPE_SECRET", "secret key here")
os.environ.setdefault("DATABASE_URL", "secret key here")
os.environ.setdefault("SECRET_KEY", "secret key here")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "secret key here")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "secret key here")

11. Go to `settings.py` file and add your environment variables.

12. Add `env.py` to .gitignore file

13. Go to terminal and run the following: `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

14. Create a superuser: `python3 manage.py createsuperuser`

15. Run it with the following command:  
`python manage.py runserver`

16. Open `localhost:8000` on your browser

17.  Add `/admin` to the end of the url address and login with your superuser account and create new products.

#### Deployment to Heroku

The following steps were taken in order to deploy this site to Heroku:

1. Created a new app in `Heroku` with a unique name, chose my region

2. Went to `Resources`, within Add-ons searched `Heroku Postgres`, chose Hobby Dev - Free version, then clicked `Provision` button.

3. In `Settings` clicked on `Reveal Config Vars` button, and copied the value of `DATABASE_URL`

4. Returned to terminal window and run `sudo pip3 install dj_database_url`

5. Also run `sudo pip3 install psycopg2`. Created a requirements.txt file using the terminal command `pip3 freeze > requirements.txt`

6. Went to `settings.py` and added `import dj_database_url` and updated `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}` also updated `env.py` with `os.environ.setdefault("DATABASE_URL", "postgres://postgres key - copied earlier from Heroku")`

7. I run `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

8. I created a superuser: `python3 manage.py createsuperuser`

9. Logged in to `Amazon AWS`, went to `S3` and created a new `S3` bucket.

10. Returned to terminal window and run `sudo pip3 install django-storages` and `sudo pip3 install boto3`. Went to `settings.py` and added `storages` to `INSTALLED_APPS`.

11. Also in `settings.py` the following lines are added:

AWS_S3_OBJECT_PARAMETERS = {  
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',  
    'CacheControl': 'max-age=94608000'  
}

AWS_STORAGE_BUCKET_NAME = 'egg-sell-nt'  
AWS_S3_REGION_NAME = 'eu-west-1'  
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")  
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")  

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

12. Updated `env.py` with `AWS` keys (these keys are from `S3`).

13. Created `custom_storages.py` at the top level:

from django.conf import settings  
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
   location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
   location = settings.MEDIAFILES_LOCATION

14. Went to `settings.py` and added:

STATICFILES_LOCATION = 'static'  
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'  
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

15. Returned to terminal window and run `python3 manage.py collectstatic`

16. Returned to `Heroku`. In `Settings` clicked on `Reveal Config Vars` button, and added all the following config vars from `env.py`:

| Key         | Value | 
|:-------------:| :----: | 
|  AWS_ACCESS_KEY_ID | secret key here  |
|  AWS_SECRET_ACCESS_KEY | secret key here |
|  DATABASE_URL | secret key here |
|  DISABLE_COLLECTSTATIC| 1 |
|  SECRET_KEY | secret key here |
|  STRIPE_PUBLISHABLE | secret key here |
|  STRIPE_SECRET| secret key here |

17. Clicked to `Deploy`, then `GitHub`, searched for my repository and clicked to `Connect` button.

18. Returned to terminal window and run `sudo pip3 install gunicorn` and added to `requirements.txt`

19. Created a `Procfile` using the following command: `echo web: gunicorn ms4.wsgi:application`

20. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

20. Returned to `Heroku` and hit `Deploy Branch`

21. Once the build is complete, click on `Open app`

22. Went to `settings.py` and added `egg-sell-nt.herokuapp.com` to `ALLOWED_HOSTS`

23. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

24. Returned to `Heroku` and hit `Deploy Branch` again.