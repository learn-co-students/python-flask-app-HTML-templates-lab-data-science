
# Python - Getting Started with Flask

## Introduction
In this lab we are going to continue building out a flask app. This time we are going to explore returning HTML instead of just simple text. We'll use HTML to help us make our web page look a bit more organized and stylized. Then we'll go a step further and create templates for our HTML pages. This will help make our program more reusable and flow a bit cleaner by separating our concerns. This will become clearer as we start building, so, let's get started! 

## Objectives
* Define routes that return HTML
* Create routes that use params from the route to make more dynamic HTML
* Separate HTML from the routing logic using `render_template`
* Create HTML templates that use information from params

## Getting Started
Okay, our first step is to set up our flask app and define some routes in our `app.py` file. 

The first route we want to define is the root route, or index, or home. It's the first route you are taken to for any website -- `"/"`. If we don't define this route then we will get the dreaded `404 error`. So, let's define this route and have it return an `h1` tag that reads `"Welcome to my flask app"` and a `p` tag that reads `"be careful, it's still under construction..."`.

**Note:** The convention in Flask is to name the function that follows a route the same as the route. We cannot define functions with the same name as another function in the same file, so, it is a good practice to name the functions similarly to the routes they belong to. 

```python

@app.route('/')
def index():
    return "SOME HTML"

# index is the conventional name for our root route ("/")

@app.route('/login')
def login():
    return "SOME HTML"

```

## Making Dynamic HTML
Alright, great! We have our index page showing our welcome message. Now, what if we wanted everyone who visited our web app to have their own profile? For example, if we wanted to see a page with our friend Mary's name on it, how could we do this?

Well we could start by defining a route for Mary specifically. Let's do that. Define a route, `"/profile/mary"` and have it return an `h1` tag that reads `"Welcome to Mary's profile"`. 

Once we have a route that takes us to Mary's profile, we need to create 4 more for our other friends Jeff, Becca, John, and Kathleen. Seems like this would be a lot more work than it should be, right? Could we maybe make this process a bit more dynamic? Yes! If we change our route from `"/profile/mary"` to `"/profile/<name>"` and we have our method underneath this route take an argument of `name`, which is being passed by our route, we can make it this route a lot more dynamic. Now if we go to `"/profile/john"` our app will assing the <name> variable to `"john"` and when we interpolate our `name` argument it will show John's name on the page. Try it out!

> **note:** the `< >` in a route definition tells our app that this part of the route is a variable and what we put between these symbols (i.e. `"john"`) is what gets assigned to our variable (i.e. `name`)

## Building Out a Profile Page

Neat! We have our routes becoming a bit more interesting, but our profile page looks a bit blank. Let's add a bit more HTML. Since we know we can pass in information in our routes, let's make a short __about me__ section for the profile page. Let's have a person's `age`, `favorite hobby`, and `hometown` be listing in an unordered list below their name.

First let's define a route to be `"/profile/<name>/<age>/<favorite_hobby>/<hometown>"`
Then the HTML returned should look like the below with an `<h1>` as the welcome message, and `<h3>` as the `About <name>:` title, followed by an unordered list with `age`, `favorite hobby`, and `hometown` all being bolded followed by the corresponding information.

The following route should take you to a page that looks like the below HTML:

**route:** `"/profile/john/27/sailing/asbury_park,nj"`

<h1>Welcome to John's profile!</h1>
<h3>About John:</h3>
<ul>
    <strong>Age:</strong><li>27</li>
    <strong>Favorite Hobby:</strong><li>Sailing</li>
    <strong>Hometown:</strong><li>Asbury Park, NJ</li>
</ul>

> **hint:** you will need to do some string operations to make sure that names are capitlaized and the hometown is formatted properly. Once your strings are formatted propery, you will need to interpolate them into the string of HTML your function is returning.

## Separating Our Concerns with Templates

Awesome, we got our very long route to display our information in a more legible and organized fashion. But the function below this route is really starting to get pretty illegible and ugly. How do we fix this? That's right -- we fix this with Templates! Let's start out with a simple one. Let's create a route called `"/hello-world-template"`. The function beneath this route will return a render template expression with the argument of the template filename like this:

**First** we need to update our flask import to include the render_template function:


```python
from flask import Flask, render_template
```
Then we can use render template like we do below:

```python
def hello_world_template()
    return render_template('hello_world.html')
```

So, in our templates folder, open the `hello_world.html` file and inside this file, include an `h1` tag with the text `Hello again, World! This is a template!`.

Keep in mind, since we are no longer returning a string from our function (i.e. `hello_world_template()`), we will be writing HTML directly in the `hello_world.html` file. So, the file will look like the below:

`<h1>Hello again, World! This is a template!</h1>`

Awesome! Now when we go to the hello-world-template route we see our new `h1` tag with our updated text.

This is great. We can now separate our HTML and our routes, which feels like a step in the right direction if we think about having to scale our application into something larger. 

## More Dynamic Templates

What about our dynamic routes though? We really need to separate our profile HTML but we also need to make sure we can get our params (or data from our route) so we can personalize the profiles. 

Luckily, this is not as difficult as it might seem. We can pass our params to the render_template function like we do with the name of the template.

```python
def show_profile(name, age, favorite_hobby, hometown)
    return render_template('profile.html', name=name, age=age, favorite_hobby=favorite_hobby, hometown=hometown)
```

> **hint:** we will want to keep our string operations in this fuction before the render_template function. We can also pass as many or few arguments into the render template function as we would like.

This makes our name, age, favorite_hobby, and hometown variables available to our HTML in the `profile.html` template, and whatever name we assign these variables (i.e. `name`=name) will define how refer to them in the HTML templates. For example if we were passing in a variable for a name our render_template function would look like the following:

```python
render_template('profile.html', name=name)
``` 

and my template would then look something like this:

`<h1>Hi! My name is {{name}}</h1>`

And when our Flask app reads the HTML it will know to use the `name` variable we passed in and interpolate it where we have the double curly braces, `{{}}`. These double curly braces simply tell our flask app that what is between the braces is python code and then it is interpreted as such.

So, where we were interpolating our params in our string of HTML will need to be updated to use the double brace method of interpolation instead of our string interpolation. Once we have updated our HTML to use the double curly braces, we can again visit our profile route and see our template in action!

## Summary

Great work! In this lab we used Flask to create different routes and return some more dynamic HTML. Once our application started to get a bit more complex we decided to use the render_template function from Flask so that we separate our routing logic from our HTML. We then updated our template to recieve variables and interpolate them in our HTML using the double curly braces. Our Flask apps are looking better and better! 
