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
- [X] **Verify password change functionality**: `/account/password/reset/`
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