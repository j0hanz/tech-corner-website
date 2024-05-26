### Manual Testing

#### Registration
- [ ] **Navigate to Sign-Up page**: `/account/signup/`
- [ ] **Fill registration form with valid details**: 
  - Username, email, password
- [ ] **Submit registration form**
- [ ] **Verify registration success**:
  - User is redirected to login page or logged in automatically
  - Confirmation email is sent (if applicable)

#### Login
- [ ] **Navigate to Sign-In page**: `/account/login/`
- [ ] **Enter valid credentials and log in**
- [ ] **Verify login success**:
  - User is redirected to the home page (index page)
  - User profile information is accessible

### Profile Management
- [ ] **Navigate to Profile page**: `/profile/`
- [ ] **Click on Edit Profile button**
- [ ] **Update profile details**: 
  - First name, last name, email, favorite tech, profile image, bio
- [ ] **Submit profile update form**
- [ ] **Verify profile update success**:
  - Changes are reflected on the Profile page

#### Creating a Post
- [ ] **Navigate to Create Post page**: `/create-post/`
- [ ] **Fill in post details**: Title, body
- [ ] **Submit post creation form**
- [ ] **Verify post creation success**:
  - Post is displayed on the home page (index page)

#### Editing a Post
- [ ] **Navigate to user's posts page**: `/user_posts/`
- [ ] **Edit a post**: Update post body
- [ ] **Submit post edit form**
- [ ] **Verify post update success**:
  - Changes are reflected on the post

#### Deleting a Post
- [ ] **Delete a post**
- [ ] **Verify post deletion success**:
  - Post is removed from the home page and user's posts page

#### Comment Management
- [ ] **Navigate to a specific post's detail page**: `/posts/<slug>/`
- [ ] **Add a comment to the post**
- [ ] **Submit comment form**
- [ ] **Verify comment creation success**:
  - Comment is displayed under the post

#### Editing a Comment
- [ ] **Edit a comment**
- [ ] **Submit comment edit form**
- [ ] **Verify comment update success**:
  - Changes are reflected on the post detail page

#### Deleting a Comment
- [ ] **Delete a comment**
- [ ] **Verify comment deletion success**:
  - Comment is removed from the post detail page

#### Page Navigation and Access Control
- [ ] **Verify redirection for unauthenticated users**:
  - Attempt to access restricted pages (e.g., Create Post, Edit Profile)
  - Ensure unauthenticated users are redirected to the About page

- [ ] **Verify access for authenticated users**:
  - Log in and navigate to restricted pages
  - Ensure authenticated users have access

#### General Functionality
- [ ] **Verify home page displays latest posts**:
  - Ensure pagination is working (5 posts per page)

#### Responsiveness
- [ ] **Check responsiveness**:
  - Ensure the website looks good and works smoothly on phones, tablets, and computers

#### About Page
- [ ] **Verify About page content**: `/about/`
  - Check for correct display of About Tech Corner and Features sections

#### Error Handling
- [ ] **Test invalid login attempt**:
  - Enter incorrect credentials and submit
  - Verify appropriate error message is displayed

- [ ] **Test invalid form submissions**:
  - Leave required fields empty and submit forms
  - Verify appropriate error messages are displayed

#### Security
- [ ] **Ensure password is not visible when typing**
- [ ] **Verify password reset functionality**: `/account/password/reset/`
  - Follow the password reset process and verify success

#### Deployment
- [ ] **Check deployment settings**:
  - Ensure `DEBUG` is set to `False` in production
- [ ] **Verify static file serving**:
  - Ensure static files (CSS, JS, images) are loading correctly in production

#### Miscellaneous
- [ ] **Check favicon is displayed correctly**
- [ ] **Verify all links and buttons work as expected**
- [ ] **Ensure no broken images on the site**