# Tech Corner

![tech-corner-high-resolution-logo-white-transparent](https://github.com/j0hanz/tech-corner-website/assets/159924955/7a15d4d7-c904-43f9-9769-4e9ba7d57fc7)

Tech Corner is a Reddit-style news site where users can share tech news. Users can interact with posts by creating their own posts and commenting on existing posts.

## User Stories

### User

- **Account Management**
  - As a user, I want to create an account so that I can participate in discussions and post content.
  - As a user, I want to edit my profile so that I can update my personal information.
  - As a user, I want to view my profile so that I can see my personal information and posts.
  - As a user, I want to delete my account if I no longer wish to use the platform.
  - As a user, I want to reset my password if I forget it.

- **Post Management**
  - As a user, I can create, read, update, and delete my posts so that I can manage my content.
  - As a user / owner, I can view comments on an individual post so that I can read the conversation.
  - As a user, I want to click on a post title, so that I can read the full text and see detailed information including comments and upvotes.

## Database Structure

![graphviz](https://github.com/j0hanz/tech-corner-website/assets/159924955/ed537dfd-943c-4ee2-bac9-877cb1c8e52d)

## Wireframes

#### Home Page
![Home_Page](https://github.com/j0hanz/tech-corner-website/assets/159924955/dd145c8d-b149-4d14-9ed3-0ade18e690f7)

__________________________________________________________________________________________________________
#### Enter Post Page
![Enter_Post_Page](https://github.com/j0hanz/tech-corner-website/assets/159924955/3948334f-6c02-4a7e-abf7-6152a26fe30a)

__________________________________________________________________________________________________________
#### Post Page
![Post_Page](https://github.com/j0hanz/tech-corner-website/assets/159924955/345af101-1edd-46e2-98ce-c2a48dd19d1f)

__________________________________________________________________________________________________________
#### Sign Up Page
![Sign_Up_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/a8995187-9038-451a-97ef-d930b094a9d8)

__________________________________________________________________________________________________________
#### Sign In Page
![Sign_In_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/1a032e68-b27d-4049-941d-8bcdab49dfb8)

__________________________________________________________________________________________________________
#### Password Reset Page
![Password_Reset_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/5bbf0e31-7a7c-4f33-8a84-9295d5046300)

__________________________________________________________________________________________________________
#### Profile Page
![Profile_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/5f12a900-bf1b-473f-9c8e-10bba8c07e1b)

__________________________________________________________________________________________________________
#### Edit Profile Page
![Edit_Profile_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/93cf9d0f-d039-4b3b-8448-50182f9002fb)

__________________________________________________________________________________________________________
#### Your Post Page
![Your_Post_Page-removebg-preview](https://github.com/j0hanz/tech-corner-website/assets/159924955/8a186954-25b3-4a96-9fcb-90b2c6d4b1b9)

## Technologies Used

The following technologies were used on this project:

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

The packages installed for this file can be found in requirements.txt, and can be seen below.

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

# Credits

- [Namify](https://namify.tech/): A tool for generating brandable names for your business, project, or website.
- [Logo.com](https://logo.com/): A service for creating professional logos for your brand or project.
- [CSS Gradient](https://cssgradient.io/): An online tool for creating beautiful gradient backgrounds for your website.
- [Google Fonts](https://fonts.google.com/selection/embed): A library of free, open-source fonts optimized for the web, easily embeddable in your site.
- [Favicon.io](https://favicon.io/favicon-converter/): A tool to convert any image to a favicon for your website.
- [Django User Profile Guide](https://dev.to/earthcomfy/django-user-profile-3hik): A comprehensive guide to creating user profiles in Django.
- [Bootstrap](https://getbootstrap.com/): A framework for building responsive, mobile-first sites.
