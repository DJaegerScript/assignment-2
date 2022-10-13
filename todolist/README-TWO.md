# [Assignment 6: Javascript and AJAX](https://pbp-assigments-adjie.herokuapp.com/todolist/ajax-index)


## Name : Adjie Djaka Permana

## NPM : 2106702485

1. **Describe the difference between asynchronous programming with synchronous programming!**

    **Synchronous** means that client requests must be processed in sequence order. Simply, every time client sends a request to the server, the client must wait for the process to be completed and the client should get the response from the server before the client sends another request.

    **Asynchronous** is when every time a client sends a request to the server, the client can send another request to the server even though the server has not sent the response back.

2. **When Implementing Javascript and AJAX, there is an application in the paradigms of Event-Driven Programming. Describe the reasoning for those paradigms and state some examples of its application!**
   
    Event-Driven Programming is a paradigm where the control flow is determined by the occurrence of events. One of the examples is DOM events in Javascript DOM manipulation. DOM events allow JavaScript to set a handler for a specific event that is triggered by DOM interaction such as click, submit, etc. We can set the handler inline in the HTML tag or use `addEventListener`.

3. **Describe the implementation of asynchronous programming in AJAX!**

    Asynchronous programming in AJAX makes the delay of data retrieval avoidable. It makes the user can continue to interact with the page while AJAX processing the request in the background. Then, when the server sends the response back, AJAX will update the data in the page seamlessly.

4. **Explain how you would implement the checklist above!**
   
   First, I create separate index views to serve data from the server using `fetch`. Then, I fetch the data from the `/todolist/json` and inject it into the template. After finishing the fetching process of the data, I create the modal with `tailwind` that fetch the django form from the server when it's opened. Then, I make the logic to send the `POST` request using fetch to `/todolist/add`. Finally, I add the bonuses requirement with allowing my app to asynchronously update and delete the data.