<p align="center">
  <img src="https://github.com/j0hanz/tech-corner-website/assets/159924955/7a15d4d7-c904-43f9-9769-4e9ba7d57fc7" alt="tech-corner-high-resolution-logo-white-transparent"/>
</p>

<p align="center">
<strong>Tech Corner</strong> is a community blog and news site for technology enthusiasts to share and engage with the latest tech news. <br>Join us to post your insights, comment on discussions, and connect with a network of tech enthusiasts.<br>
   Discover and share the latest in technology with us!
</p>
<p align="center">Visit :arrow_right:<a href="https://tech-corner-web-70b84e69e118.herokuapp.com/">Tech Corner</a></p>

---

# Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [User Stories](#user-stories)
   - [Account Management](#account-management)
   - [Post Interaction](#post-interaction)
4. [Design](#design)
   - [Color Scheme](#color-scheme)
   - [Typography](#typography)
   - [Imagery](#imagery)
5. [Database Structure](#database-structure)
6. [Wireframes](#wireframes)
7. [User Experience](#user-experience)
   - [Pages](#pages)
8. [Security](#security)
   - [Django Axes](#django-axes)
9. [Technologies Used](#technologies-used)
   - [Backend](#backend)
   - [Frontend](#frontend)
   - [Database](#database)
   - [Storage](#storage)
   - [Deployment](#deployment)
   - [Other Tools and Libraries](#other-tools-and-libraries)
10. [Packages](#packages)
11. [Dependencies](#dependencies)
12. [Testing](#testing)
13. [Known Issues](#known-issues)
14. [Future Implementation](#future-implementation)
15. [Deployment](#deployment)
    - [Deploy to Heroku](#deploy-to-heroku)
    - [Forking the Repository](#forking-the-repository)
    - [Cloning the Repository](#cloning-the-repository)
16. [FAQs](#faqs)
17. [Credits](#credits)
    - [YouTube Channels](#youtube-channels)
    - [Acknowledgments](#acknowledgments)

---

## Introduction

![responsive-removebg](https://github.com/j0hanz/tech-corner-website/assets/159924955/f554fd8a-0d91-4aa6-9ac8-d2ca90aad1c2)

Welcome to Tech Corner, a platform designed for technology enthusiasts to connect, share knowledge, and stay updated with the latest trends in technology. Whether you're a developer, a tech blogger, or simply passionate about tech, Tech Corner offers a space for you to engage and grow within a vibrant community.

---

## Features

- **Share Knowledge:** Start discussions, answer questions, and offer help.
- **Connect with Users:** Interact with fellow tech enthusiasts.
- **Join the Conversation:** Comment and share your thoughts on the latest tech trends.
- **Personalize Your Space:** Customize your profile with a photo, favorite tech, and optional contact details.
- **Fully Responsive:** Designed to work smoothly on phones, tablets, and computers.
- **Security:** Includes features like Django Axes to protect against brute-force attacks.

## User Stories

### Agile Development

This project followed an agile methodology. The initial focus was on developing a functional site covering all key user stories. Additional features and functionalities were added incrementally.

- **Examples of User Stories:**
  - [User Account Creation](https://github.com/j0hanz/tech-corner-website/issues/1)
  - [Profile Management](https://github.com/j0hanz/tech-corner-website/issues/12)
  - [View My Profile](https://github.com/j0hanz/tech-corner-website/issues/13)
  - [Open a Post](https://github.com/j0hanz/tech-corner-website/issues/5)
  - [Manage Posts](https://github.com/j0hanz/tech-corner-website/issues/4)
  - [About Page](https://github.com/j0hanz/tech-corner-website/issues/17)
  - [Enhance Authentication Pages](https://github.com/j0hanz/tech-corner-website/issues/9)

GitHub Projects was used to manage the project board. You can view it [here](https://github.com/users/j0hanz/projects/4/views/1).

#### Account Management
- **Create Account:** Register to join and contribute to the community.
- **Edit Profile:** Update personal details and preferences.
- **View Profile:** Access personal profile and contributions.
- **Delete Account:** Remove personal data and exit the community.

#### Post Interaction
- **CRUD Operations:** Create, read, update, and delete posts.
- **Comment System:** Engage with posts through comments.
- **Detailed View:** Access detailed post views, including comments and interactions.

###### [ Back to Start ](#table-of-contents)

## Design

### Color Scheme
The background image uses a gradient created with [CSS Gradient](https://cssgradient.io/).

### Typography
The Open Sans font family is used for its clear and readable design across all devices.

### Imagery
- **Logo:** Designed using the [LOGO](https://logo.com/) tool.
- **Favicon:** Created with [Favicon Generator](https://favicon.io/favicon-converter/) for a custom browsing icon.

## Database Structure

#### The entity relationship diagram for this project can be seen below.
![schema_database](https://github.com/j0hanz/tech-corner-website/assets/159924955/3358bd6e-1b74-4b9d-ae49-9bed0c9fc2f3)

### Entities and Relationships

This project has several models that make up the main parts of the application. Here’s a brief description of each model and their connections:

1. **User Model**:
   - This is the built-in Django model for users.
   - Linked with `UserProfile`, `Post`, and `Comment`.

2. **UserProfile Model**:
   - Extends the `User` model with more details.
   - Fields: `first_name`, `last_name`, `favorite_tech`, `profile_image`, `bio`.
   - One user has one profile.
   - Linked to `FavoriteTech`.

3. **FavoriteTech Model**:
   - Stores different types of favorite technologies.
   - Field: `type`.
   - Linked with `UserProfile`.

4. **Post Model**:
   - Represents blog posts.
   - Fields: `title`, `slug`, `author`, `body`, `date`, `status`, `excerpt`, `updated_on`.
   - Each post is written by one user.
   - Linked with `Comment`.

5. **Comment Model**:
   - Represents comments on posts.
   - Fields: `post`, `author`, `body`, `created_on`.
   - Each comment is linked to one post and one user.

**Relationships:**

* One user has one profile (One-to-One).
* One profile can have one favorite tech (One-to-One, Optional).
* One user can write many posts (One-to-Many).
* One post can have many comments (One-to-Many).
* One user can write many comments (One-to-Many).

###### [ Back to Start ](#table-of-contents)

## Wireframes

#### Below are the wireframes used in the development of this site.

- **Home Page**

![Home_Page](https://github.com/j0hanz/tech-corner-website/assets/159924955/dd145c8d-b149-4d14-9ed3-0ade18e690f7)

---

- **Enter Post Page**

![Enter_Post_Page](https://github.com/j0hanz/tech-corner-website/assets/159924955/3948334f-6c02-4a7e-abf7-6152a26fe30a)

---

- **Post Page**

![Post_Page](https://github.com/j0hanz/tech-corner-website/assets/159924955/345af101-1edd-46e2-98ce-c2a48dd19d1f)

---

- **Sign Up Page**

![Sign_Up_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/a8995187-9038-451a-97ef-d930b094a9d8)

---

- **Sign In Page**

![Sign_In_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/1a032e68-b27d-4049-941d-8bcdab49dfb8)

---

- **Password Reset Page**

![Password_Reset_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/5bbf0e31-7a7c-4f33-8a84-9295d5046300)

---

- **Profile Page**

![Profile_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/5f12a900-bf1b-473f-9c8e-10bba8c07e1b)

---

- **Edit Profile Page**

![Edit_Profile_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/93cf9d0f-d039-4b3b-8448-50182f9002fb)

---

- **Your Post Page**

![Your_Post_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/8a186954-25b3-4a96-9fcb-90b2c6d4b1b9)

###### [ Back to Start ](#table-of-contents)

---

## User Experience

### Pages

- **About:**
 
![About](https://github.com/j0hanz/tech-corner-website/assets/159924955/a01112fe-2e04-4b9c-999a-2d1802b983f7)

*The About page provides information about the Tech Corner website and its features. If you are not logged in, you will be redirected to this page. If you are logged in, you will be redirected to the home page.*

---

- **Sign Up:**

![Sign Up](https://github.com/j0hanz/tech-corner-website/assets/159924955/b9116200-8ff9-4fc0-a938-70d45b63d222)

*The Sign Up page allows users to create their own accounts.*

---

- **Sign In:**

![Sign In](https://github.com/j0hanz/tech-corner-website/assets/159924955/69ce63bf-8755-4eb3-a8f8-7a0ded3bc97b)

*The Sign In page allows users to log into their accounts.*

---

- **Profile:**

![Profile](https://github.com/j0hanz/tech-corner-website/assets/159924955/ed674dac-c53b-4ae8-aebe-936e5e6dbc40)

*The Profile page allows users to navigate to the Edit Profile section, view their own posts, and provide a description of themselves.*

---

- **Edit Profile:**

![Edit Profile](https://github.com/j0hanz/tech-corner-website/assets/159924955/5d4e9faf-1337-4261-be1c-fe5d75fb24bc)

*The Edit Profile page allows users to customize their profiles, change their passwords, delete their accounts, and upload profile images.*

---

- **Create Post:**

![Create Post](https://github.com/j0hanz/tech-corner-website/assets/159924955/9f6b91e0-c7ba-4afd-aefa-67c6d54d2a19)

*The Create Post page allows users to create their own posts.*

---

- **User Posts:**

![User Posts](https://github.com/j0hanz/tech-corner-website/assets/159924955/9c5382ca-a569-497b-874b-8534d13c5aab)

*The User Posts page allows users to view their own posts.*

---

- **Sign Out:**

![Sign Out](https://github.com/j0hanz/tech-corner-website/assets/159924955/c8bfb96f-ecdf-4762-b0df-5920c77671d3)

*The Sign Out page allows users to log out of their accounts.*

---

- **Change Password:**

![Change Password](https://github.com/j0hanz/tech-corner-website/assets/159924955/01793358-72e1-4b71-8344-11e3d2198aaa)

*The Change Password page allows users to update their passwords.*

---

- **Delete Account:**

![Delete Account](https://github.com/j0hanz/tech-corner-website/assets/159924955/d006e70f-50d7-47c6-926d-e017f1264919)

*The Delete Account page allows users to delete their accounts.*

---

- **Edit Post:**

![Edit Post](https://github.com/j0hanz/tech-corner-website/assets/159924955/88834cba-7a08-4bf5-a92e-6d92f7c26489)

*The Edit Post page allows users to modify their posts.*

---

- **Delete Post:**

![Delete Post](https://github.com/j0hanz/tech-corner-website/assets/159924955/6a4f400e-e504-49ae-8f62-12207bedc9e2)

*The Delete Post page allows users to delete their posts.*

---

- **User Profile:**

![User Page](https://github.com/j0hanz/tech-corner-website/assets/159924955/067d6793-c913-4fe1-82e9-901e5f84d40b)

*Users can view other users' profiles by clicking on their icons.*

---

- **Home Page:**

![Home](https://github.com/j0hanz/tech-corner-website/assets/159924955/40934211-8091-4f4f-9f2e-03a3e719099f)

*The Home page displays all published posts, sorted from newest to oldest. Logged-in users are redirected to this page by default.*

###### [ Back to Start ](#table-of-contents)

---

## Security

### Django Axes

Django Axes is an essential security feature for our users, designed to protect against brute-force attacks by limiting the number of login attempts. Here’s why we chose to include Django Axes:

- **Security Enhancement**: By restricting the number of login attempts, we greatly reduce the risk of unauthorized access via brute-force methods.
- **User Protection**: This ensures that legitimate users are protected from malicious login attempts.

If your account is locked due to multiple failed login attempts, it will automatically be reset after 30 minutes, allowing you to try logging in again.

###### [ Back to Start ](#table-of-contents)

## Technologies Used

The following technologies were utilized in this project:

### Backend
- **Python**: The primary language for backend development.
- **Django**: A Python web framework for rapid development and clean design. [Django Documentation](https://docs.djangoproject.com/)
- **Django Allauth**: Manages authentication, registration, and account management. [Django Allauth Documentation](https://django-allauth.readthedocs.io/)

### Frontend
- **HTML**: The standard markup language for creating web pages.
- **CSS**: Styles web page layout and design.
- **JavaScript**: Adds interactivity to web pages.
- **Bootstrap**: A front-end framework for responsive, mobile-first web development. Using [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/).
- **Font Awesome**: A toolkit for icons and fonts. [Font Awesome](https://fontawesome.com/)
- **Google Fonts**: A library of web fonts. [Google Fonts](https://fonts.google.com/)

### Database
- **PostgreSQL**: An open-source relational database system. [PostgreSQL](https://www.postgresql.org/)

### Storage
- **Cloudinary**: Manages images and videos in the cloud. [Cloudinary](https://cloudinary.com/)

### Deployment
- **Heroku**: A platform for deploying and scaling web applications. [Heroku](https://www.heroku.com/)
- **ElephantSQL**: A hosting service for PostgreSQL databases. [ElephantSQL](https://www.elephantsql.com/)

### Other Tools and Libraries
- **Git**: Version control system to track changes in source code. [Git Documentation](https://git-scm.com/doc)
- **GitHub**: Platform for version control and collaborative development. [GitHub](https://github.com/)
- **Whitenoise**: Serves static files for Python web apps. [Whitenoise Documentation](http://whitenoise.evans.io/en/stable/)
- **Axes**: Tracks failed login attempts in Django sites. [Axes Documentation](https://django-axes.readthedocs.io/en/latest/)

###### [ Back to Start ](#table-of-contents)

## Packages

The packages installed for this project can be found in requirements.txt and can be seen below.

- [asgiref==3.8.1](https://pypi.org/project/asgiref/)
- [Django==4.2.9](https://pypi.org/project/Django/)
- [django-allauth==0.62.1](https://pypi.org/project/django-allauth/)
- [django-axes==6.4.0](https://pypi.org/project/django-axes/)
- [django-crispy-forms==2.1](https://pypi.org/project/django-crispy-forms/)
- [django-summernote==0.8.20.0](https://pypi.org/project/django-summernote/)
- [dj-database-url==0.5.0](https://pypi.org/project/dj-database-url/)
- [dj3-cloudinary-storage==0.0.6](https://pypi.org/project/dj3-cloudinary-storage/)
- [psycopg2==2.9.9](https://pypi.org/project/psycopg2/)
- [sqlparse==0.5.0](https://pypi.org/project/sqlparse/)
- [cloudinary==1.36.0](https://pypi.org/project/cloudinary/)
- [Pillow==10.3.0](https://pypi.org/project/Pillow/)
- [crispy-bootstrap5==2024.2](https://pypi.org/project/crispy-bootstrap5/)
- [oauthlib==3.2.2](https://pypi.org/project/oauthlib/)
- [requests-oauthlib==2.0.0](https://pypi.org/project/requests-oauthlib/)
- [PyJWT==2.8.0](https://pypi.org/project/PyJWT/)
- [gunicorn==22.0.0](https://pypi.org/project/gunicorn/)
- [whitenoise==6.6.0](https://pypi.org/project/whitenoise/)
- [urllib3==1.26.18](https://pypi.org/project/urllib3/)

## Dependencies

For full details on project dependencies, please refer to the `requirements.txt` file in the project repository.

## Testing

[View detailed testing information here](TESTING.md).

## Known Issues

1. On the "Your Posts" page, the "New Post +" button does not align correctly in height when no posts have been created.
2. When scrolling on smaller screen sizes, a small white bar briefly appears at the bottom of the screen and disappears after scrolling stops.
3. On touchscreens, button effects remain in a hovered state if the user navigates back to the same page.
4. Some user-uploaded profile images are cropped or not displayed in their original state.

## Future Implementation

- **Search Posts**: Implement search functionality to find specific posts.
- **Notifications**: Add notifications for interactions and comments.
- **Messages**: Enable users to send private messages for private communication.
- **Like Button Functionality**: Implement a like button for posts.
- **Hyperlink Support**: Enable users to add URLs using a hyperlink function.
- **Reset Password**: Allow users to reset their password via email if forgotten.
- **Edit Comment**: Allow users to edit their comments.
- **Follow Other Users**: Allow users to follow other users.
- **MFA**: Implement multi-factor authentication (MFA) for enhanced security.
- **Feedback Page**: Provide a page for users to contact us directly.
- **Report Inappropriate Content**: Enable users to report inappropriate content to help maintain community standards.

###### [ Back to Start ](#table-of-contents)

---

## Deployment

### Deploy to Heroku

#### Create and Set Up Your App

1. **Log in** to your Heroku Dashboard: [Heroku Dashboard](https://devcenter.heroku.com/articles/heroku-dashboard).
2. Click "**New**" and select "**Create new app**".
3. **Name your app** and choose a region. Click "**Create app**".
4. Go to the "**Deploy**" tab and choose "**GitHub**" as the deployment method.
5. **Connect Heroku to GitHub** and authorize access to your project repository.
6. Select your project repository.

---

#### Set Up Environment Variables in Django

1. **Create an `env.py` file:**
   - In the top-level directory of your Django app, create a new file named `env.py`.

2. **Import `os` in `env.py`:**
   ```python
   import os
   ```

3. **Set up necessary environment variables in `env.py`:**
   - Add a secret key:
     ```python
     os.environ['SECRET_KEY'] = 'your_secret_key'
     ```
   - Add the database URL:
     ```python
     os.environ['DATABASE_URL'] = 'your_database_url'
     ```

4. **Update `settings.py` to use environment variables:**
   - Replace the value of the `SECRET_KEY` variable with:
     ```python
     SECRET_KEY = os.environ.get('SECRET_KEY')
     ```
   - Change the value of the `DATABASES` variable to:
     ```python
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
     ```

5. **Modify the top of `settings.py`:**
   ```python
   from pathlib import Path
   import os
   import dj_database_url

   if os.path.isfile('env.py'):
       import env
   ```

---

#### Configure Heroku Environment Variables

1. **Navigate to the "Settings" tab in Heroku.**
2. **Open the "Config Vars" section and add environment variables:**
   - Add `DATABASE_URL` with the database link from your `env.py`.
   - Add `SECRET_KEY` with the secret key value from your `env.py`.

---

#### Finalize Settings in Django

1. **Migrate the models to the new database connection:**
   - In your terminal, run:
     ```bash
     python manage.py migrate
     ```

2. **Add static files settings in `settings.py`:**
   ```python
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   ```

3. **Update the templates directory in `settings.py`:**
   ```python
   TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
   ```

4. **Modify the `DIRS` key in the `TEMPLATES` variable in `settings.py`:**
   ```python
   'DIRS': [TEMPLATES_DIR],
   ```

5. **Add Heroku to the `ALLOWED_HOSTS` list:**
   - The format will be `your-app-name.herokuapp.com`, which you can copy from the Domains section in the Settings tab of your Heroku app.

---

#### Create Necessary Folders and Files

1. **Create `static` and `templates` folders:**
   - In your Django app's code editor, create new top-level folders named `static` and `templates`.

2. **Create a `Procfile`:**
   - At the top level of your project directory, create a new file named `Procfile` with a capital "P".
   - Add the following line to the `Procfile`:
     ```bash
     web: gunicorn PROJECT_NAME.wsgi
     ```

---

#### Deploy Your Changes

**Deploy Your App from Heroku:**
- Go to the "**Deploy**" tab in Heroku.
- Choose the branch you want to deploy and click "**Deploy Branch**".

Your app should now be live! You can find the access link at the top of the Heroku dashboard.

---

### Forking the Repository

By forking the GitHub repository, you can create a copy of the original repository to view or modify without affecting the original. Follow these steps to fork the repository:

1. **Log in to GitHub** or create an account if you don't have one.
2. Navigate to this [Repository](https://github.com/j0hanz/tech-corner-website).
3. Click on the "**Fork**" button at the top right of the repository page.
4. GitHub will create a copy of the repository in your account.

---

### Cloning the Repository

Creating a clone allows you to make a local copy of the repository to run the project on your machine. Follow these steps to clone the repository:

1. Navigate to [Tech Corner Repository](https://github.com/j0hanz/tech-corner-website).
2. Click on the "**Code**" button at the top of the list of files.
3. Select the "**HTTPS**" option and copy the provided URL to your clipboard.
4. Open your code editor and, in the terminal, navigate to your desired directory.
5. Type `git clone` followed by the URL you copied.
6. Press Enter, and Git will clone the repository to your local machine.

By following these steps, you'll have a local copy of the Tech Corner project that you can modify and run as needed.

###### [ Back to Start ](#table-of-contents)

---

## FAQs

#### Q: How can I reset my password?
**A:** Currently, there is no password reset feature, but it will be available in the future.

#### Q: How can I delete my account?
**A:** Go to your profile, click "Edit Profile," scroll down, and click the red "Delete Account" button.

#### Q: How can I search for specific posts?
**A:** Search functionality is not available now but will be added in the future.

#### Q: How do I send private messages?
**A:** Private messaging is not supported yet but will be added in future updates.

#### Q: Can I edit my comments?
**A:** Comment editing is not available now but is planned for future updates.

#### Q: How do I follow other users?
**A:** Following users is a feature planned for future versions.

#### Q: Can I add hyperlinks in my posts?
**A:** Adding hyperlinks will be available in future updates.

#### Q: How do I personalize my profile?
**A:** Go to your profile, click "Edit Profile," and customize your details.

#### Q: Is Tech Corner accessible on different devices?
**A:** Yes, it's fully responsive and works on phones, tablets, and computers.

#### Q: What security measures are in place to protect my account?
**A:** Tech Corner uses features like Django Axes to protect against brute-force attacks.

---

## Credits

### YouTube Channels

[Dave Gray](https://www.youtube.com/@DaveGrayTeachesCode)
- **This** [Python Django Tutorial](https://www.youtube.com/watch?v=qcJZN1pvG6A&list=PL0Zuz27SZ-6NamGNr7dEqzNFEcZ_FAUVX) was very helpful.

[Python Simplified](https://www.youtube.com/@PythonSimplified)
- For great Python tutorials.

[Programming with Mosh](https://www.youtube.com/watch?v=rHux0gMZ3Eg)
- For excellent programming tutorials.

### Acknowledgments

- **Contributors:** Thanks to everyone improving Tech Corner.
- **Special Thanks:** 
  - [Namify](https://namify.tech/) and [Logo.com](https://logo.com/) for branding resources.

I would also like to thank:

- **Graeme Taylor** - My mentor.
- **Kristyna** - My cohort facilitator.
