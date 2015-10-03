# travel_wishes_website

This is an in-progress practice/experimental website project for the purposes of learning more about html, css, sqlalchemy, flask and other database and web development tools. The eventual idea of the website is to present a catalogue of "travel locations" and to allow users to add locations to their "wishlist" and then to also allow users to view each other's lists.

## access
currently hosted by Heroku here: http://travel-wishes-website.herokuapp.com/


## usage
In it's current state, the website has the following pages and abilities:

1.) a home page ('/'):
where a user can choose either to view a list of all the travel locations in the database or to view a particular user's travel wish list

2.) a list of travel locations page ('/locations'):
where the locations are listed alphabetically by default and the user can choose to sort them by location (state) instead, or choose to view a user's list

3.) a view user wishlist page ('/wishlists'):
where the user can enter a username and view that user's travel wish list

## next steps
For now I've populated the database with users, locations, and user wishlists to enable the above functions to work. The next steps that I'll work on will be enabling users to sign up and log in to the website with a username and pass and to add and delete locations from their wishlists.

