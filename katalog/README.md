# Assignment 2: Introduction to Django and Models View Template (MVT) Concept

## Name : Adjie Djaka Permana

## NPM : 2106702485

1. **Create a diagram containing client request to the Django web application and its response. Also explain the flow of the diagram and how the `urls.py`, `views.py`, `models.py` and HTML files connected each other.**  
   
   ![MVT Diagram](https://github.com/DJaegerScript/assignment-2/blob/main/image.png?raw=true)

   Client-side/user will send a `GET` HTTP request to the server. The server, using `urls.py`, will map the request to the controller (views) according to the specified URL. The controller defined in `views.py` will render the HTML file on the server along with the data needed. The data that are rendered into HTML is retrieved from a database that is represented by `models.py`. Lastly, the server will send the response in the form of HTML.
   
2. **Explain why do we use virtual environments? Let's say, if we do not use the virtual environments, can we still create a Django web application?**

   The usage of virtual environments isn't mandatory, we still can develop Django applications without using any virtual environments. But, the virtual environment is very useful to separate the dependencies between different projects. Let's say in project A you need a dependency with a specific version and in project B you need the same dependency but with a different version, to solve the problem, you may use the virtual environment. Also, the virtual environment keeps you from installing unnecessary dependencies on the server.

3. **Explain how did you implement the steps on point 1 to point 4 above.**

   Firstly, I clone the template from PBP's repository on GitHub. Then, create a venv, install the dependencies, do the migrations, and load the fixture. After that, I start working on `views.py`, creating a method that will query the model that is defined in `models.py` using `all()` method. Then, creates a dictionary that contains my name and student id along with the data that is retrieved from the model. The dictionary, later, will be mapped properly into each field on the HTML file. Then, make the views return rendered HTML file with the dictionary.

   After that, I defined the routing in the `katalog.urls`. Then, I register it on the `project_django.urls`.

   Lastly, I do a little setup on my GitHub repo, such as registering the Heroku app name and API key as the secrets. Then, push the project to GitHub and let the GitHub Actions do the rest.