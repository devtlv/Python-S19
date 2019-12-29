# Models-Views-Controller

### MVC model is the base of every flask operations

***
### Everything start with a request, the user can make requests by calling URLs
This URL will be *routed* to a function


***
## Views
As a user, you only see views, views are the rendered page, it's what the user sees.
***
## Models
Models are the data, the objects that compose your page (the users, the posts, the comments, the pics...)
***
## Controller 
Controller is the constructor, he knows how to take _models_ and assemble them to make *views*


***
# How it work

1) A user send a request (by entering a URL)<br>
2) The request is routed to a function of the controller<br>
3) The controller uses the models to retrieve necessary data<br>
4) The controller build the view with the data from the models<br>
5) The controller render the view and send it back to the user<br>
