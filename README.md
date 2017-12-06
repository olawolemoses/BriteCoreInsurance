# BriteCoreInsurance
A solution that allows insurers to define their own custom data model for their risks

## Deliverables
1. [A Python file containing the ORM classes for these tables](app/base/models.py)
2. [An entity relationship diagram, which depicts the tables and their relationship to one another](./EERD.png)

## Backend

For the backend, create two API endpoints. One that returns a single risk type and one that returns a list of all risk types. Include all of the risk types' fields, field types, and any other data about the fields. This is your chance to show that you know how to create clean REST APIs.

Deliverables will be...

1. A well-tested REST API written in Python.

### Frontend

The frontend is all about collecting information as it relates to these generic models. Create a single page that hits your risk type API endpoint(s) and displays all of the fields to the user in a form. Be sure to display at least one field of each type on the page. Don't worry about submitting the form.

Fields should use appropriate widgets based on their type. `text` fields should display as text boxes, `date` fields should use date pickers, and so on.

Deliverables will be...

1. A modern JavaScript app. **Bonus points** if you use ES6 and a modern JavaScript framework. **Mega bonus points** if you use Vue.js specifically.

## Questions

For questions, please contact grant@britecore.com.

## Finished?

When you're done with the above project, please submit your GitHub repo to grant@britecore.com. Also submit...

1. A video of you running the code and loading the page in a browser (plus some screenshots).
2. **Bonus points** if you host the application and send us the URL so we can play with it.
3. **Mega bonus points** if you host the backend on [AWS Lambda](https://aws.amazon.com/lambda/) using [Zappa](https://github.com/Miserlou/Zappa).
