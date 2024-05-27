## Manual Testing

#### Registration
- [X] **Navigate to Sign-Up page**: `/account/signup/`
- [X] **Fill registration form with valid details**: 
  - Username, email, password
- [X] **Submit registration form**
- [X] **Verify registration success**:
  - User is redirected to Home page automatically

#### Login
- [X] **Navigate to Sign-In page**: `/account/login/`
- [X] **Enter valid credentials and log in**
- [X] **Verify login success**:
  - User is redirected to the home page (index page)

### Profile Management
- [X] **Navigate to Profile page**: `/profile/`
- [X] **Click on Edit Profile button**
- [X] **Update profile details**: 
  - First name, last name, email, favorite tech, profile image
- [X] **Submit profile update form**
- [X] **Verify profile update success**:
  - Changes are reflected on the Profile page

#### Creating a Post
- [X] **Navigate to New Post page**: `/create-post/`
- [X] **Fill in post details**: Title, body
- [X] **Submit post creation form**
- [X] **Verify post creation success**:
  - Post is displayed on the home page (index page)

#### Editing a Post
- [X] **Navigate to user's posts page called "Your Posts"**: `/user_posts/`
- [X] **Edit a post**: Update post body
- [X] **Submit post edit form**
- [X] **Verify post update success**:
  - Changes are reflected on the post

#### Deleting a Post
- [X] **Delete a post**
- [X] **Verify post deletion success**:
  - Post is removed from the home page and user's posts page

#### Comment Management
- [X] **Navigate to a specific post's detail page**: `/posts/<slug>/`
- [X] **Add a comment to the post**
- [X] **Submit comment form**
- [X] **Verify comment creation success**:
  - Comment is displayed under the post

#### Deleting a Comment
- [X] **Delete a comment**
- [X] **Verify comment deletion success**:
  - Comment is removed from the post detail page

#### Page Navigation and Access Control
- [X] **Verify redirection for unauthenticated users**:
  - Attempt to access restricted pages (Create/Edit/Delete) that belongs to other users.
  - Ensure unauthenticated users are redirected to the About page

#### General Functionality
- [X] **Verify home page displays latest posts**:
  - Ensure pagination is working (5 posts per page)

#### Responsiveness
- [X] **Check responsiveness**:
  - Ensure the website looks good and works smoothly on phones, tablets, and computers

#### About Page
- [X] **Verify About page content**: `/about/`
  - Check for correct display of About Tech Corner and Features sections

#### Error Handling
- [X] **Test invalid login attempt**:
  - Enter incorrect credentials and submit
  - Verify appropriate error message is displayed

- [X] **Test invalid form submissions**:
  - Leave required fields empty and submit forms
  - Verify appropriate error messages are displayed

#### Security
- [X] **Ensure password is not visible when typing**
- [X] **Verify password change functionality**: `/account/password/change/`
  - Check if password has changed and log-in with the new password.

#### Django Axes
- [X] **Ensure user lockout after reaching maximum login attempts**:
  - Confirm that the user account is locked after the specified number of failed login attempts.
  
- [X] **Verify reset of locked users after 30 minutes**:
  - Access the `/lockout/` endpoint to check if the lockout template is displayed correctly.
  - Ensure that only the specific username is locked out, not the entire IP address.

#### Deployment
- [X] **Check deployment settings**:
  - Ensure `DEBUG` is set to `False` in production
- [X] **Verify static file serving**:
  - Ensure static files (CSS, JS, images) are loading correctly in production

#### Miscellaneous
- [X] **Check favicon is displayed correctly**
- [X] **Verify all links and buttons work as expected**
- [X] **Ensure no broken images on the site**


## Responsiveness

The website must be fully responsive across all screen sizes.
This includes ensuring that images maintain their quality without any pixelation or distortion.
Additionally, page elements should be arranged to prevent overlapping, and horizontal scrolling should be completely avoided.

https://github.com/j0hanz/tech-corner-website/assets/159924955/04591c56-63dd-44e1-b286-fb5fafc8a369

### Index
![Home_page](https://github.com/j0hanz/tech-corner-website/assets/159924955/ab31d339-157c-492a-9b83-913337f5d771)

### About
![about_page](https://github.com/j0hanz/tech-corner-website/assets/159924955/df62820e-1070-45cd-93b0-3c362cc82af7)

### Sign Up & Sign In
![signup_signin_pages](https://github.com/j0hanz/tech-corner-website/assets/159924955/d0e7fb13-5318-4424-ab61-aad8c62227e4)

### Post Detail
![Post_Detail_page](https://github.com/j0hanz/tech-corner-website/assets/159924955/7647ee2a-13c9-45cb-beb6-da4cff927c2a)


## Python Linter

### Views in Website App
![views_website](https://github.com/j0hanz/tech-corner-website/assets/159924955/7ababed0-167e-4eed-b89f-bc4e247803f9)

### Models in Website App
![models_website](https://github.com/j0hanz/tech-corner-website/assets/159924955/e9e7af68-7d76-484b-af9a-59957d1552ad)

### Views in User Profile App
![views_userprofile](https://github.com/j0hanz/tech-corner-website/assets/159924955/11fd69e0-6d5e-4f23-bf5a-687c94fa4484)

### Models in User Profile App
![models_userprofile](https://github.com/j0hanz/tech-corner-website/assets/159924955/622dcae4-1aaa-4123-a221-da2d16e086b2)

## JavaScript

### JavaScript file for this project were checked using [JSHint](https://jshint.com/).

![JSHint](https://github.com/j0hanz/tech-corner-website/assets/159924955/ed1504be-03f5-429d-9dfa-a77e207cfa20)



