# BriteCoreInsurance
A solution that allows insurers to define their own custom data model for their risks

## Deliverables

### Data
1. [A Python file containing the ORM classes for these tables](app/base/models.py)
2. [An entity relationship diagram, which depicts the tables and their relationship to one another](./EERD.png)

### Backend

Deliverables are:

[Controller Endpoints](app/base/controllers.py)

1. returns a single risk type
@base.route('/risktype/<int:pk>', methods=['GET'])

2. returns all risk types
@base.route('/risktype/all/', methods=['GET'])


### Frontend

1. [a single front end page](app/templates/base/index.html)

2. [A morden Javascript Vue app](app/base/static/app.vue.js)


## Finished

1. A video of you running the code and loading the page in a browser (plus some screenshots).

2. **Hosted at** 
- http://todev.com.ng:8800/
- http://todev.com.ng:8800/base/risktype/1
- http://todev.com.ng:8800/base/risktype/all/
