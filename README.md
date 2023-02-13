This microservice allows users to retrieve climate data for a given city and state. The user enters the city and state information, which is then sent to a Flask app using a POST request. The Flask app processes the data and returns the climate data for the given city and state in JSON format.

Communication Contract:

Requesting Data from the Microservice:

To request climate data from the microservice, send a POST request to the following endpoint:

``` bash
http://localhost:5000/weather
The request body should include the following JSON data:
```

``` json
{
  "city": "city_name",
  "state": "state_name"
}
```
where city_name is the name of the city you want to retrieve climate data for, and state_name is the name of the state the city is located in.

For example, to retrieve climate data for San Francisco, California using JavaScript, you would make the following request:

```javascript
fetch('http://localhost:5000/weather', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    city: 'San Francisco',
    state: 'California'
  })
})
  .then(response => response.json())
  .then(data => {
    // process the returned data
  })
  .catch(error => {
    // handle any errors
  });
  ```
  
Receiving Data from the Microservice:

The microservice will respond to a successful request with a JSON object containing the climate data for the given city and state. The JSON data will have the following format:

```json
{
  "category_1": {
    "month_1": "value",
    "month_2": "value",
    ...
  },
  "category_2": {
    "month_1": "value",
    "month_2": "value",
    ...
  },
  ...
}
```
where month_1, month_2, etc. are the names of the months, and category_1, category_2, etc. are the categories of climate data for that month. The values for each category will be strings.

For example, the following JSON data represents climate data for the city of San Francisco in the state of California:

```json
{
    "Record high °F (°C)": {
        "Jan": "79 (26)",
        "Feb": "81 (27)",
        "Mar": "87 (31)",
        ...
    },
    "Mean maximum °F (°C)": {
        "Jan": "67.1 (19.5)",
        "Feb": "71.8 (22.1)",
        "Mar": "76.4 (24.7)",
       ...
    },
    "Average high °F (°C)": {
        "Jan": "57.8 (14.3)",
        "Feb": "60.4 (15.8)",
        ...
```
Note that the microservice may respond with an error message if there is an issue with the request or if the climate data for the given city and state could not be found.

UML Sequence: 

![image](https://user-images.githubusercontent.com/97201029/218585966-08ee6498-01b3-4df7-89f5-0ce576c3919a.png)

