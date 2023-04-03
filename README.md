# MyCookbook
<br>
Project developed for the Full Stack Developer - Code Institute course, using HTML, CSS ,JavaScript, Python and Django to build a website.
<br>

## Introduction
MyCookbook is a website with the purpose of being an online cookbook, where the user can create, edit and save their favorite recipes. In addition, the site administrator has the ability to make any recipe public, for visitors not registered on the site.  


## Showcase
![Preview](docs/Mockup.png)

### Live Website
A deployed link to the website can be found [here](https://my-cookbook.herokuapp.com/)


# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [UX](#ux-user-experience)
- [Agile Development Process](#agile-development-process)
- [Design](#design)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)


## UX User Experience
### User Stories

### As the site creator/admin:
* Is possible to have full access and functionality as a superuser
* Is possible to be able to create, read, edit and delete all recipes
* It is possible to view and publish of recipes by a given user for all website visitors, even without registering on the website. 

### As the site user:
* The user is able to register an account
* The user is able to create, read, edit and delete they on recipes
* The user is able to view all other recipes approved by admin by using the search functionality
* The user is able to make changes into the recipe by editing recipe


## User Stories
I have included links to the [GitHub Issues](https://github.com/PEmbarach/MyCookbook/issues) for this project, as well as the [KANBAN board](https://github.com/users/PEmbarach/projects/4).


## Design

<br>

### Wireframes
 <details>
  <summary>Click here to view all wireframes both Desktop & mobile:</summary>

  ![](docs/frameworks/Home.png)
  ![](docs/frameworks/Login.png)
  ![](docs/frameworks/Recipe.png)

  </details>

<br>

### Navigation

I created a logic flowchart to help organise the site structure.
The ERD entity relationship diagram helped visually to confirm user roles and the permissions.

<details>
  <summary>Click here to view website navigation:</summary>

  ![](docs/Sitemap.jpg)
</details>
<br>

### Database Schema

Below is the template created to produce the required database structure.

<details>

![](docs/database_schema.png)
</details>

<br>
<br>

## Features

<br>

### Existing Features
<br>

### Home Page
Homepage displays the Navbar Brand / logo name, Login, Sign Up and search function on the left.
There is a H1 heading describing what the website is about so that users understand the websites function and target audience.
The main body of the homepage contains 6 recipes and once more than 6 articles are posted pagination shows links to the next page.
Social media network links are displayed in the top page and footer.

![Preview](docs/pages/home_page.png)
<br>

### Navigation Bar
When not logged in the Navbar displays links to Login and Sign Up.
When a user hovers over navigation links the color changes at the bottom of the links to show responsiveness when the user interacts with the link element(s). When a user is logged in the Navbar displays links to Home, My Recipes, Create Recipe and Logout.

![Preview](docs/pages/Navbar.png)
<br>

### Search Page
When a user searches a particular word the result will return recipes which contain the word searched with the recipes down below. Example below user searched "jambon"

![Preview](docs/pages/search_bar.png)
<br>

### Search Article - No Results
![Preview](docs/pages/search-no-result.png)
<br>

### Log in
When a user goes the Login page they are shown a simple form with email and password to sign in.

![Preview](docs/pages/login.png)
<br>

### Sign up
When a user goes to the Sign up page they can enter account details as Name, email and password. If the username and email already exists, an error message will appear. 

![Preview](docs/pages/sign_up.png)
<br>

### Log in messaging 
When a user logs in successfully the same will be directed to the dashboard page, where there is an H1 message from Hello and your recipes already posted.

![Preview](docs/pages/login_message.png)
<br>

### Log out
When a user goes to the Logout they will be redirected to home page.
<br>

### Admin - Superuser Access
![Preview](docs/pages/superuser_access.png)
<br>

### Create Recipe
![Preview](docs/pages/create_recipe.png)
<br>

### User Dashboard
![Preview](docs/pages/User_dashboard.png)
<br>

### C.R.U.D:

#### Create (button):
- The button to invite you to submit a new artwork will be found on the **"Prints"** page.
- It is only visible to users who are signed in.
![CRUD - create button](docs/crud/create.png)

#### Create (form):
- This page may only be accessed from the button on the **"Prints"** page.
![CRUD - create form](docs/crud/create_form.png)

#### Read:
![CRUD - read](docs/crud/read.png)

#### Update & Delete:
- The update & delete feature is only available to the user who who directly submitted the artwork.
![CRUD - update & delete](docs/crud/update_and_delete.png)


## Future Features
* Allows users to like/ unlike a recipe.
* Allows users to filter by recipe creation date
<br>

## Bugs / Errors encountered during development
* The STATICFILES path was wrong and needed to be fixed.
* It was necessary to correct the code responsible for the Search, as it was not showing the searched recipe, even though it existed, and always showed the message "recipe not found".
* Several tests were made until finding the error that was not allowing deploying on Heroku. The error was in the Config Vars on Heroku itself, a typo in the Cloudinary URL.
* An error in the sign up code does not allow the creation of a new user, always appearing as a blank field.
<br>
<br>

### Unfixed Bugs
No known unfixed bugs present at the time of submission
<br>

## Technologies Used
<br>

### Languages Used
  * [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  * [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  * [JavaScript](https://www.javascript.com/)
  * [Python](https://www.python.org/)
<br>

### Frameworks, Libraries & Programs Used
* [amiresponsive](http://ami.responsivedesign.is/) to see how responsive the site is on different devices.
* [Balsamiq](https://balsamiq.com/) was used to create the Wireframes.
* [Cloudinary](https://cloudinary.com/) was used to upload, store, manage, manipulate, and deliver images.
* [Django](https://www.djangoproject.com/) is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern.
* [Font Awesome](https://fontawesome.com/) was used for icons for aesthetic and UX purposes on the buttons.
* [GitHub](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
* [Gitpod](https://www.gitpod.io/) An online IDE linked to the GitHub repository used to write my code.
* [Google Chrome Dev tools](https://developer.chrome.com/docs/devtools/) for debugging.
* [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) used for audits to measure the quality of web pages.
* [Heroku](https://www.heroku.com/) used to deploy this app, a cloud platform as a service supporting several programming languages.
* [Pixabay](https://pixabay.com/) Images for this project were sourced from Pixabay.

<br>

## Testing
<br>

### Validation Testing
|  | Validations |  Pass/Fail |
| ------------- |-------------|  :----: |
| Chrome   | Lighthouse Report | Pass |
| HTML   | W3C Markup Validator | Error |
| CSS   | W3C CSS Validator | Error |
| Python   | PEP8 online | Pass |
| JS   | JSHint | Pass |
<br>

### Lighthouse Report
* Ran Lighthouse reports audits to gauge performance, accessibility, and SEO. Gain actionable and reportable insights in real time.
 <details>
  <summary>Click here to see the Lighthouse Report</summary>

  ![](docs/testing/lighthouse.png)

  </details>
<br>

### The W3C Markup Validator
  <details>
  <summary>Verified using the W3C Markup Validator, which had errors or warnings present. Click here to see the W3C Markup Validator result</summary>

  ![](docs/testing/w3c_html.png)

  </details>
<br>

### W3C CSS Validator
  <details>
  <summary>Verified using the W3C CSS Validator, which had errors or warnings present. Click here to see the W3C CSS Validator result</summary>

  ![](docs/testing/w3c_CSS.png)

  </details>
<br>

### PEP8 Validator
<details>
<summary>Checked Python code is formatted according to the PEP 8 standards </summary>

#### final_user (app.py)
![](docs/testing/pep8/Final_user/Final_user(apps.py).png)
<br>

#### final_user (url.py)
![](docs/testing/pep8/Final_user/Final_user(urls.py).png)
<br>

#### final_user (views.py)
![](docs/testing/pep8/Final_user/Final_user(views.py).png)
<br>

#### MyCookbook (asgi.py)
![](docs/testing/pep8/MyCookbook/MyCookbook(asgi.py).png)
<br>

#### MyCookbook (urls.py)
![](docs/testing/pep8/MyCookbook/MyCookbook(urls.py).png)
<br>

#### MyCookbook (wsgi.py)
![](docs/testing/pep8/MyCookbook/MyCookbook(wsgi.py).png)
<br>

#### recipe (admin.py)
![](docs/testing/pep8/Recipe/recipe(admin.py).png)
<br>

#### recipe (apps.py)
![](docs/testing/pep8/Recipe/recipe(apps.py).png)
<br> 

#### recipe (models.py)
![](docs/testing/pep8/Recipe/recipe(models.py).png)
<br>

#### recipe (urls.py)
![](docs/testing/pep8/Recipe/recipe(urls.py).png)
<br> 
</details>

<br>
<br>

### Manual Testing
* Manual testing was completed for each case and edge case scanerio from user log in, user create a recipe, user delete recipe and user log out and  search articles.
* The site was also manually tested on various browsers (Google Chrome, Safari, Microsoft Edge and Firefox.) and on different screen sizes.
* Dev tools was used often to identify errors within HTML and CSS code, with the console feature to identify errors in Javascript code.
* I also used lighthouse reports to see the performance, quality, and correctness of the website.
<br>

### More manual testing scanerios and results
|   | Pass/Fail |
| ------------- | :----: |
| Selecting heardit logo on homepage directs user back to homepage  |  Pass |
| Selecting Login directs user to /final_user/login/ page  |  Pass |
| Selecting Sign Up directs user to /final_user/signup page |  Pass |
| Selecting My recipes directs user to /final_user/dashboard/ page  |  Pass |
| Selecting Create Recipe directs user to /create/recipe/ page  |  Pass |
| Selecting home directs user to home page  |  Pass |
| Selecting search articles box in navbar and entering a search returns expected result  |  Pass |
| Selecting search articles box in navbar and entering a no results search returns no result page  |  Pass |
| Click on the pagination link at the bottom of the page returns results of the next page (example /?page=2) |  Pass |
| Logging in as superuser / admin |  Pass |
| Logging in as superuser / admin to publish a recipe |  Pass |
| Navigating site as user / admin is permitted |  Pass |
| As admin I can view and publish a recipe |  Pass |
| Updating a post as the author |  Pass |
| Deleting a post as the author |  Pass |
| Logging out as a user / admin directs user to homepage |  Pass |
| Posting a new article requires appropriate fields to be filled in |  Pass |
| Clicking on the social media icons in the footer open the link in a new tab |  Pass |

<br>

### Responsiveness Browser Compatibility

|  | Chrome | Firefox | Edge | Safari | Pass/Fail |
| ------------- |-------------| -----|  ---------- |  -----| :----: |
| Expected Appearance   | yes | yes  | yes  | yes | Pass |
| Expected Layout   | yes | yes  | yes  | yes | Pass |

<br>

## Deployment

### Github Deployment
* Logged into the Github account, navigate to Repositories and click New.
* Select the template (in this case Code-Institute-Org/gitpod-full-tamplate was used).
* Name the repository.
* Select the Public option.
* Click Create Repository.
* In the upper right corner, click on Gitpod, which will open the online VSCode text editor.
* After creating the project, in the terminal, it is deployed as follows.
* In the terminal first type "git add."
* Followed by "git commit -m "comment" ".
* And finally "git push"

<br>

### Heroku Deployment
* Log in to [Heroku](https://id.heroku.com/login) or create an account
* On the main page click New and Create New App
* Note: new app name must be unique
* Next select your region, I chose Europe.
* Click Create App button
* Click in resources and select Heroku Postgres database
* Click Reveal Config Vars and add new config "SECRET_KEY"
* Click Reveal Config Vars and add new config "CLOUDINARY_URL"
* Click Reveal Config Vars and add new config "DISABLE_COLLECTSTATIC = 1"
* The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
* Scroll to the top of the page and choose the Deploy tab
* Select Github as the deployment method
* Confirm you want to connect to GitHub
* Search for the repository name and click the connect button
* Scroll to the bottom of the deploy page and select the preferred deployment type
* Click either Enable Automatic Deploys for automatic deployment when you push updates to Github
<br>

### Final Deployment 

* Create a Procfile `web: gunicorn heardit.wsgi`
* When development is complete change the debug setting to: `DEBUG = False` in settings.py
* In this project the summernote editor was used so for this to work in Heroku add: `X_FRAME_OPTIONS = SAMEORIGIN `to
   settings.py.
* In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`
<br>

## Credits

* Code Institute - [Hello Django](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/121ef050096f4546a1c74327a9113ea6/) - Task Manager Walkthrough
* Code Institute - [I think therefore I blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/
) - Django blog project Walkthrough
* [Django Documentation](https://docs.djangoproject.com/en/4.1/)
* [Codemy's YouTube Channel](https://www.youtube.com/c/Codemycom/playlists)
<br>

## Acknowledgements
* To create this website, I relied on material covered in the Full Stack Development course by Code Institute.
* I also sourced information and help from a variety of sources such as Slack Community Channels, Udemy, W3Schools, MDN and YouTube for Online Web Tutorials and resources.
* Martina Terlevic and Rohit Sharma for reviewing my work and providing valuable feedback and advice.
* Special thanks to Jhonatan Santos, who helped me to give movement to the project, correcting me and indicating ways for JS and CSS.

This project is for educational use only and was created for the Code Institute Module.