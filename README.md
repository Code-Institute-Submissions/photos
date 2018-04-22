# Photos of Ireland

This is a fictional e-commerce site built using Django. It was built as one of three projects for my Code Institute bootcamp course. The main features are: 
1.	Account registration, login, logout and users blog history.
2.  Allows users to purchase and rate/review photographs.
3.	Users can additionally add their own photos as part of a blog post.
4.	Highly liked blog posts will be reviewed and potentially added to photographs for sale.
5.	Users can view their shopping cart before purchase.


## Demo

A live demo of this project is available here 


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
The Ratings App allows users to give their opinion on the photographs for sale and give it a rating out of five stars.

### Blog
The Blog App displays all blog posts and allows the user to contribute their own blog post. Users can also edit and delete their own posts and like
posts made by other users.

### Cart/Checkout
The Cart App stores the photographs, quantity and prices and displays a basket total.
The Checkout App renders a form for the user to provide their payment details and processes the payment via Stripe.

### Contact
The Contact App allows the user to get in contact and ask any questions he/she feels fit.










