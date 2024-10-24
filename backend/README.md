# backend

This is the Python backend component of tha inventory application. It is responsible for managing user authentication and items management. There are two main enpoints:

1. /auth: This route contains the endpoints for managing the user accounts
2. /items: This route exposes some endpoints to the authenticated users for reading, creating, updating and deleting items from their inventory.

The endpoints are exposed to the frontend throught FastAPI and the data is being stored in a postgresql database.