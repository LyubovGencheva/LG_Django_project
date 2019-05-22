# LG_Django_project - Destiliarahi Blog
# A simple blog platform, intended for sharing adventure stories and future plans by family and friends 

## URL-s

## Superuser (admin) credentials:
### /admin/                             		Django Admin panel 


## All (non-registered, unauthenticated and authenticated) users:
### /                                   		Destiliarahi Homepage - list of all blog posts (NavigationBar-top left>>Destiliarahi)
### /about/                             		Destiliarahi About (Welcome) Page (NavigationBar-top-left>>About)
### /profiles/all/                       		List of all registered users (Sidebar>"Who's already here?")
### /user/<str:username>/               		List of all posts by the user with that username 
								(@click on the username above a post or 
								SideBar>>Who's Already Here?>>@click on user from the list)
## Non-registered/Registered, but not logged-in users:
### /login/                             		Login (being redirect after register or NavigationBar-top-right when registered, but not logged in)
### /register/                          		Register New User (NavigationBar-top-right, for new users only; redirect to login page)


## Registered, but not logged-in users - 
## Forgotten password at Login attempt:
### /password-reset/                    		Request password reset via e-mail (from Login page >> Forgot password?)
### /password-reset/done                		E-mail with pass reset instructions sent to user's mail (redirected after 'Request pass reset')
### /password-reset/<uidb64>/<token>/   		Confirms that pass-reset requestor is a registered user (after click on the sent e-mail link)
### /password-reset/complete/           		Password reset finalization


## Authenticated users only:
### /profile/                            		User's own profile page with options for profile info (username, e-mail, about, profile pic) updates
### /post/new/                           		Create new post
### /post/<int:pk>/                     		Post details (redirect after post creation by author or @clicking on post's title from homepage)
                                    				PostDetail view: update/delete options for the author/ read-only for the rest of the users
### /post/<int:pk>/update/               		Post update option - for the post's author only (from Post Detail view-> redirect to Post details)
### /post/<int:pk>/delete/              		Post delete option - for the post's author only (from Post Detail view)
                                          			At 'Delete' -> 'Confirm?' -> Cancel: redirect to Post Details
                                          			At 'Delete' -> 'Confirm?' -> Yes, delete!: redirect to Homepage
### /logout/                            		Logout (NavBar-top-right when authenticated-> redirect to logout page with LoginAgain option)
