# Photos of Ireland
This is a fictional e-commerce site built using Django. It was built as one of three projects for my Code Institute bootcamp course. 

The main features are: 
1.	Account registration, login, logout and users blog history.
2.  Allows users to purchase and rate/review photographs.
3.	Users can additionally add their own photos as part of a blog post.
4.	Highly liked blog posts will be reviewed and potentially added to photographs for sale. Blog posts may only be liked once per user.
5.	Users can view their shopping cart before purchase.


## Demo
The deployed version of the web app is available on heroku: https://photos-project3.herokuapp.com/


## View locally
The repository is available on github: https://github.com/ColmHughes/photos. In order to run this app locally, all dependancies 
listed in requirements.txt must be installed. 
When running locally, SQLite database was used & static and media files were stored locally. 
When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. 
Our settings.py file was changed to base.py with local.py and production.py showing specifics on where to look for our media files.


## Built using
* SQLite database
* Django framework
* Python
* JavaScript
* jQuery
* HTML5
* CSS3
* Bootstrap


## Apps
All templates inherit the base.html template which provides the website with a consistant navbar and footer.

### Accounts
The Account App allows the user to register an account, login and logout of the website and also view a list of their historic blog posts.

### Home
The Home App renders the index.html template, it includes a carousel of some of the photos for sale and also
shows the most liked blog post and the highest rated photograph for sale.

### Photos/Ratings
The Photo App allows users browse through a gallery of photographs and add them to their shopping cart.
The Ratings App allows users to give their opinion on the photographs for sale and give it a rating out of five stars. User may only
rate each photo once.

### Blog
The Blog App displays all blog posts and allows the user to contribute their own blog post. Users can also edit and delete their own posts and like
posts made by other users. Users may only like a photo once.

### Cart/Checkout
The Cart App stores the photographs, quantity and prices and displays a basket total.
The Checkout App renders a form for the user to provide their payment details and processes the payment via Stripe.

### Contact
The Contact App allows the user to get in contact and ask any questions he/she feels fit.


## Wireframes
The wireframes for this project can be viewed on github in the 'Wireframes' folder. The project is
fully mobile-responsive with the only major difference being the home page and navbar which have separate sketches
for mobile and desktop. All sketches were made on 'wireframepro'.

## Testing
This application was tested across a range of browsers and devices, it is fully mobile responsive. Manual tests were carried out on all 
functionality including:
* Only registered users can purchase photographs.
* Only registered users can add a blog post.
* Only registered users can leave a rating or like a blog post.
* Registered users may only leave one review per photo and one like per blog post.
* Only the admin or author of a blog post may delete or edit the post.
* Highest rated and most like blog post show up on home page.
* Incorrect URL's will direct to custom 404 page.

Automated testing is also available in the tests.py located within each app.


## Media
All photographs in the photo gallery and the 404 page were taken by my friend Paul Gannon.

## Features to be implemented
More automated testing to increase total coverage, include login users username in navbar.
