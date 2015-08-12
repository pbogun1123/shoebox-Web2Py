Piotr Bogun | Chris Vick
ShoeBox Application
CSC308
________________________________________________________________________
The application is very simple and easy to use. There are more features that I would like to add to it when I have more time. Each view contains an explanation of the application similar to what this readme does.
________________________________________________________________________

 
Run the Web2Py application after you put the shoebox directory into your web2py/applications folder. Run localhost/shoebox as shown
________________________________________________________________________


 
The front page posts are handled automatically through the dashboard view.

 
 
The dashboard view is only available to administrators
Login with: peter.bogun@example.com | password = "test"

 
The dashboard view  grid shows you all the front page articles. The two newest articles are automatically shown on the Home/Index page.
________________________________________________________________________

The article view allows anyone to search and read all submitted articles.
 
After searching for articles you are able to click on them to take you to a dynamically generated page for the selected article to read it.

 
________________________________________________________________________

The author page is very similar to the article page. Search for authors in the search bar:
 
The search bar only searches for shoebox "Authors". There are many shoebox users in the db but only 3 authors at the moment (Peter Bogun, Ryan Hewitt, Dan Thom).
You are able to click on an author to get more information about them and see all of their submitted articles.
 
You are able to click on their articles in this view to again read their articles.
 
________________________________________________________________________

All controller actions take place in controllers\default

 

All of the tables are in models\db_content.py

 

All of the views for each page are in views\default\<view>.html

 












