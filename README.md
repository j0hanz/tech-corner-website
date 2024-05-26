<p align="center">
  <img src="https://github.com/j0hanz/tech-corner-website/assets/159924955/7a15d4d7-c904-43f9-9769-4e9ba7d57fc7" alt="tech-corner-high-resolution-logo-white-transparent"/>
</p>

<p align="center">
<strong>Tech Corner</strong> is a community blog and news site for technology enthusiasts to share and engage with the latest tech news. <br>Join us to post your insights, comment on discussions, and connect with a network of tech enthusiasts.<br>
   Discover and share the latest in technology with us!
</p>
<p align="center">Visit :arrow_right:<a href="https://tech-corner-web-70b84e69e118.herokuapp.com/">Tech Corner</a></p>

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
13. [Future Implementation](#future-implementation)
14. [Deployment](#deployment)
    - [Deploy to Heroku](#deploy-to-heroku)
15. [FAQs](#faqs)
16. [Credits](#credits)
    - [Acknowledgments](#acknowledgments)

## Introduction

![responsive-removebg](https://github.com/j0hanz/tech-corner-website/assets/159924955/f554fd8a-0d91-4aa6-9ac8-d2ca90aad1c2)

Welcome to Tech Corner, a platform designed for technology enthusiasts to connect, share knowledge, and stay updated with the latest trends in technology. Whether you're a developer, a tech blogger, or simply passionate about tech, Tech Corner offers a space for you to engage and grow within a vibrant community.

## Features

- **Share Knowledge:** Start discussions, answer questions, and offer help.
- **Connect with Users:** Interact with fellow tech enthusiasts.
- **Join the Conversation:** Comment and share your thoughts on the latest tech trends.
- **Personalize Your Space:** Customize your profile with a photo, favorite tech, and optional contact details.
- **Fully Responsive:** Designed to work smoothly on phones, tablets, and computers.
- **Security:** Includes features like Django Axes to protect against brute-force attacks.

## User Stories

### Account Management
- **Create Account:** Register to join and contribute to the community.
- **Edit Profile:** Update personal details and preferences.
- **View Profile:** Access personal profile and contributions.
- **Delete Account:** Remove personal data and exit the community.

### Post Interaction
- **CRUD Operations:** Create, read, update, and delete posts.
- **Comment System:** Engage with posts through comments.
- **Detailed View:** Access detailed post views including comments and interactions.

## Design

### Color Scheme
The background image uses a gradient created with [CSS Gradient](https://cssgradient.io/).

### Typography
The Open Sans font family is used for its clear and readable design across all devices.

### Imagery
- **Logo:** Designed using the [LOGO](https://logo.com/) tool.
- **Favicon:** Created with [Favicon Generator](https://favicon.io/favicon-converter/) for a custom browsing icon.

Your section on the database structure looks good and is clear. Here are a few minor improvements for clarity and formatting:

Sure, here's a simpler version:

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

## Wireframes

#### Below are the wireframes used in the development of this site.

- **Home Page**

![Home_Page](https://github.com/j0hanz/tech-corner-website/assets/159924955/dd145c8d-b149-4d14-9ed3-0ade18e690f7)

- **Enter Post Page**

![Enter_Post_Page](https://github.com/j0hanz/tech-corner-website/assets/159924955/3948334f-6c02-4a7e-abf7-6152a26fe30a)

- **Post Page**

![Post_Page](https://github.com/j0hanz/tech-corner-website/assets/159924955/345af101-1edd-46e2-98ce-c2a48dd19d1f)

- **Sign Up Page**

![Sign_Up_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/a8995187-9038-451a-97ef-d930b094a9d8)

- **Sign In Page**

![Sign_In_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/1a032e68-b27d-4049-941d-8bcdab49dfb8)

- **Password Reset Page**

![Password_Reset_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/5bbf0e31-7a7c-4f33-8a84-9295d5046300)

- **Profile Page**

![Profile_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/5f12a900-bf1b-473f-9c8e-10bba8c07e1b)

- **Edit Profile Page**

![Edit_Profile_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/93cf9d0f-d039-4b3b-8448-50182f9002fb)

- **Your Post Page**

![Your_Post_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/8a186954-25b3-4a96-9fcb-90b2c6d4b1b9)

## User Experience

### Pages

- **About:**
 
![About](https://github.com/j0hanz/tech-corner-website/assets/159924955/a01112fe-2e04-4b9c-999a-2d1802b983f7)

*The About page provides information about the Tech Corner website and its features. If you are not logged in, you will be redirected to this page. If you are logged in, you will be redirected to the home page.*

- **Sign Up:**

![Sign Up](https://github.com/j0hanz/tech-corner-website/assets/159924955/b9116200-8ff9-4fc0-a938-70d45b63d222)

*The Sign Up page allows users to create their own accounts.*

- **Sign In:**

![Sign In](https://github.com/j0hanz/tech-corner-website/assets/159924955/69ce63bf-8755-4eb3-a8f8-7a0ded3bc97b)

*The Sign In page allows users to log into their accounts.*

- **Profile:**

![Profile](https://github.com/j0hanz/tech-corner-website/assets/159924955/ed674dac-c53b-4ae8-aebe-936e5e6dbc40)

*The Profile page allows users to navigate to the Edit Profile section, view their own posts, and provide a description of themselves.*

- **Edit Profile:**

![Edit Profile](https://github.com/j0hanz/tech-corner-website/assets/159924955/5d4e9faf-1337-4261-be1c-fe5d75fb24bc)

*The Edit Profile page allows users to customize their profiles, change their passwords, delete their accounts, and upload profile images.*

- **Create Post:**

![Create Post](https://github.com/j0hanz/tech-corner-website/assets/159924955/9f6b91e0-c7ba-4afd-aefa-67c6d54d2a19)

*The Create Post page allows users to create their own posts.*

- **User Posts:**

![User Posts](https://github.com/j0hanz/tech-corner-website/assets/159924955/9c5382ca-a569-497b-874b-8534d13c5aab)

*The User Posts page allows users to view their own posts.*

- **Sign Out:**

![Sign Out](https://github.com/j0hanz/tech-corner-website/assets/159924955/c8bfb96f-ecdf-4762-b0df-5920c77671d3)

*The Sign Out page allows users to log out of their accounts.*

- **Change Password:**

![Change Password](https://github.com/j0hanz/tech-corner-website/assets/159924955/01793358-72e1-4b71-8344-11e3d2198aaa)

*The Change Password page allows users to update their passwords.*

- **Delete Account:**

![Delete Account](https://github.com/j0hanz/tech-corner-website/assets/159924955/d006e70f-50d7-47c6-926d-e017f1264919)

*The Delete Account page allows users to delete their accounts.*

- **Edit Post:**

![Edit Post](https://github.com/j0hanz/tech-corner-website/assets/159924955/88834cba-7a08-4bf5-a92e-6d92f7c26489)

*The Edit Post page allows users to modify their posts.*

- **Delete Post:**

![Delete Post](https://github.com/j0hanz/tech-corner-website/assets/159924955/6a4f400e-e504-49ae-8f62-12207bedc9e2)

*The Delete Post page allows users to delete their posts.*

- **User Profile:**

![User Page](https://github.com/j0hanz/tech-corner-website/assets/159924955/067d6793-c913-4fe1-82e9-901e5f84d40b)

*Users can view other users' profiles by clicking on their icons.*

- **Home Page:**

![Home](https://github.com/j0hanz/tech-corner-website/assets/159924955/40934211-8091-4f4f-9f2e-03a3e719099f)

*The Home page displays all published posts, sorted from newest to oldest. Logged-in users are redirected to this page by default.*

### Security

#### Django Axes

Django Axes is an essential security feature for our users, designed to protect against brute-force attacks by limiting the number of login attempts. Here’s why we chose to include Django Axes:

- **Security Enhancement**: By restricting the number of login attempts, we greatly reduce the risk of unauthorized access via brute-force methods.
- **User Protection**: This ensures that legitimate users are protected from malicious login attempts.

If your account is locked due to multiple failed login attempts, it will automatically be reset after 30 minutes, allowing you to try logging in again.

## Technologies Used

The following technologies were used in this project:

### Backend
- **Python**: The main programming language for backend development.
- **Django**: A high-level Python web framework for fast development and clean design. [Django Documentation](https://docs.djangoproject.com/)
- **Django Allauth**: Handles authentication, registration, and account management. [Django Allauth Documentation](https://django-allauth.readthedocs.io/)

### Frontend
- **HTML**: Standard markup language for creating web pages.
- **CSS**: Styles the appearance of web pages, including layout and design.
- **JavaScript**: Programming language for creating interactive web elements.
- **Bootstrap**: A front-end framework for responsive, mobile-first web development. This project uses [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/).
- **Font Awesome**: A toolkit for icons and fonts based on CSS. [Font Awesome](https://fontawesome.com/)
- **Google Fonts**: A library of web fonts. [Google Fonts](https://fonts.google.com/)

### Database
- **PostgreSQL**: An open-source relational database system. [PostgreSQL](https://www.postgresql.org/)

### Storage
- **Cloudinary**: Manages images and videos in the cloud. [Cloudinary](https://cloudinary.com/)

### Deployment
- **Heroku**: A platform for deploying and scaling web applications. [Heroku](https://www.heroku.com/)
- **ElephantSQL**: A hosting service for PostgreSQL databases. [ElephantSQL](https://www.elephantsql.com/)

### Other Tools and Libraries
- **Git**: Tracks changes in source code. [Git Documentation](https://git-scm.com/doc)
- **GitHub**: Platform for version control and collaborative development. [GitHub](https://github.com/)
- **Whitenoise**: Serves static files for Python web apps. [Whitenoise Documentation](http://whitenoise.evans.io/en/stable/)
- **Axes**: Tracks failed login attempts in Django sites. [Axes Documentation](https://django-axes.readthedocs.io/en/latest/)

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

## Future Implementation

- **Mobile App**: Develop a mobile app version of Tech Corner for iOS and Android.
- **Advanced Search**: Implement an advanced search feature to help users find posts more efficiently.
- **Notifications**: Add real-time notifications for post interactions and comments.

## Deployment

### Deploy to Heroku

#### Create and Set Up Your App

1. **Log in** to your Heroku Dashboard: [Heroku Dashboard](https://devcenter.heroku.com/articles/heroku-dashboard).
2. Click "**New**" and select "**Create new app**".
3. **Name your app** and choose a region. Click "**Create app**".
4. Go to the "**Deploy**" tab and choose "**GitHub**" as the deployment method.
5. **Connect Heroku to GitHub** and authorize access to your project repository.
6. Select your project repository.

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
     os.environ['SECRET_KEY'] = 'your secret key'
     ```
   - Add the database URL:
     ```python
     os.environ['DATABASE_URL'] = 'Paste the database link in here'
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

#### Configure Heroku Environment Variables

1. **Navigate to the "Settings" tab in Heroku.**
2. **Open the "Config Vars" section and add environment variables:**
   - Add `DATABASE_URL` with the database link from your `env.py`.
   - Add `SECRET_KEY` with the secret key value from your `env.py`.

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
   STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
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
   - The format will be `your-app-name.herokuapp.com`, which

 you can copy from the Domains section in the Settings tab of your Heroku app.

#### Create Necessary Folders and Files

1. **Create `static` and `templates` folders:**
   - In your Django app's code editor, create new top-level folders named `static` and `templates`.

2. **Create a `Procfile`:**
   - At the top level of your project directory, create a new file named `Procfile` with a capital "P".
   - Add the following line to the `Procfile`:
     ```bash
     web: gunicorn PROJECT_NAME.wsgi
     ```

#### Deploy Your Changes

**Deploy Your App from Heroku:**
- Go to the "**Deploy**" tab in Heroku.
- Choose the branch you want to deploy and click "**Deploy Branch**".

Your app should now be live! You can find the access link at the top of the Heroku dashboard.

## FAQs

**Q: How can I reset my password?**
A: The current version does not offer a password reset feature. However, this functionality is planned for future implementation.

**Q: How can I delete my account?**
A: To delete your account, first go to your profile, then click "Edit Profile" and scroll down to the red button marked "Delete Account." Confirm your choice, and your data will be permanently removed.

## Credits

### Acknowledgments

- Thanks to all the contributors who spend time improving Tech Corner.
- Special thanks to [Namify](https://namify.tech/) and [Logo.com](https://logo.com/) for branding resources.
