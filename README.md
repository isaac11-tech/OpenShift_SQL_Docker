Building a service that returns everything in a single table (called data)
to a GET request.

The project includes the following:
A MySQL database running on OpenShift (use the image downloaded from DockerHub)
Implementation of a data access layer (Class DataLoader)
Setting up a FastAPI server - which accesses MySQL and returns the table data to a dedicated endpoint.
The API is exposed via a route so you can open a browser and see it arrive from the DB.
(Or using another way of testing - Python script, CURL, postman, etc.)
thank you !!!!!!