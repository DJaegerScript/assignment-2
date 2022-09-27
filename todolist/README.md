# [Assignment 4: Implementing Forms and Authentication Using Django](https://pbp-assigments-adjie.herokuapp.com/todolist)

## Name : Adjie Djaka Permana

## NPM : 2106702485

1. **What does `{% csrf_token %}` do in the `<form>` element? What happens if there is no such "code snippet" in the `<form>` element?**

   CSRF token is required to prevent CSRF attacks. CSRF (Cross-Site Request Forgery Protection) is a type of attack that will exploit the user's authenticated state. The attacker will modify the user's request and it will make the User do something that they do not intend to perform.

   CSRF token will generates a token when rendering the page on the server. Server will cross-check this token every time the page sent a request. In Django, CSRF token will generates the token in the form of hidden `<input>`.

2. **Can we create the `<form>` element manually (without using a generator like `{{ form.as_table }})`? Explain generally how to create `<form>` manually.**

   Of course, we can create the `<form>` element manually because HTML form is originally a set of `<input>` field variations that is wrapped with `<form>`. Generally, to structure an HTML form, we must provide the `<form>` element as the wrapper. Then, set `method` and `action` attributes with a needed value. `method` attribute is used to specify the HTTP method that will be used to send a request to the server, while the `action` attribute is used to specify the endpoint of the request that will be sent. In Django, if the endpoint has the same URL as the current URL, you may only specify just the `method` and ignore the `action` attributes.

   After we provide the `<form>` elements, we may give the variation of `<input>` elements as the child element of the `<form>`. We can change the `type` attribute to specify what kind of input we want the user to give and we must give the `name` attribute a value to specify a key of the data that will be sent. Lastly, we can provide either `<input>` or `<button>` element with the `submit` type to trigger the HTTP request to the server. Besides that, don't forget to provide the `{% csrf_token %}` to protect the request.

3. **Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.**

   When the user clicks on submit button inside the `<form>`, it will trigger the HTTP request to the server with the specified `method` and `action`. Then, the specified `action` will map the request to the corresponding URL registered in `urls.py` to forward the request to the specified handler defined in `views.py`. If the specified `action` is the same as the current URL but with a different HTTP method, we may control the flow based on that request method.

   In the corresponding handler defined in `views.py`, the request data will be validated using Django form. If the data is not valid, the server will send a response containing the error message. Otherwise, the request data will be stored in the database. After that, the server will respond with the HTTP redirect to the specified URL to display the stored data.

4. **Explain how you implement the checklist above.**

   First, I create a new Django app named `todolist`, register the app and the url, create the migration model, and the index view that will show the data in the form of the table. After that, I implements the Django auth like register, login, and logout. Then, the main effort is when I create the logic to insert the data into database.

   When I create the logic to insert the data, first, I create a new template to display the form based on the data from the model along with its corresponding handler that is defined in `views.py`. Handler that I create is consist of two conditions, the first is to handle the `GET` method that will respond the request with the HTML form and the second is to handle the `POST` method that will process the request to insert it into the database and redirect the request to the index of `todolist`. Last, I configure the handler of the index to display the data that based on the current authenticated user id.
