# Django Api

## Deployed Link

- https://sharon-zhao.github.io/Envoy-project-similar-to-reddit-/

## Planning Story

This project has the original express.js api version(we finished it as a group), but after we learned python and django I changed the backend by using django framework(solo work).

As a group we chose to tackle the message board prompt and we decided to try and reproduce a simplistic version of a Reddit-like message board. We began our work on the project by building the backend Express API. As a group we decided to group code the mongoose models for the resources that we would need API routes for. Once we built the models to our satisfaction, we split up the work of creating CRUD routes for each respective resource. Once we had a fully tested and functioning backend we started brainstorming the React.js frontend.

We faced a few challenges when trying to populate a nested mongoose document and we were eventually able to resolve this as a group by reading the mongoose documentation and doing some trial and error. Another interesting challenge arose when the API was sending back a 500 status error when a user tried to change a resource that didn't belong to them. While we were getting the desired behavior on the front-end, we had to go back into our error_handler file and make sure that our custom OwnershipError was included in the errors which would return a status 401 unauthorized.

The biggest challenge and learning point from this project was understanding how to effectively work together in a group and how to manage a common repo to which we were all contributing on a daily basis. While we had to inevitably go on a few LONG tangents as a group in order to solve merge conflicts in our local repos we were able to work well as a unit and this is reflected in the final product for this project.

## User Story

- As an unregistered user, I would like to sign up with email and password.
- As a registered user, I would like to sign in with email and password.
- As a signed in user, I would like to change password.
- As a signed in user, I would like to sign out.
- As a signed in user, I would like to add a post to the message board.
- As a signed in user, I would like to update my post on the message board.
- As a signed in user, I would like to delete my post on the message board.
- As a signed in user, I would like to view all other users' posts on the message board.
- As a signed in user, I would like to comment on other users' posts on the message board.
- As a signed in user, I would like to edit my comment on other users' posts on the - message board.
- As a signed in user, I would like to delete my comment on other users' posts on the message board.

## Technologies Used
- Python
- Django
- sqlite3
- AWS(S3)
- Heroku
