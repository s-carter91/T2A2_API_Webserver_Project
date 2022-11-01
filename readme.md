## Brief Planning

#### 1. Identification of the problem you are trying to solve by building this particular app

This API is being created to provide convenience when playing the Teamfight Tactics video game. Teamfight Tactics is a strategy game that relies on building a team that compliments itself by selecting the right units and sticking to a game plan. The API will allow users to store team compilations (kind of like team blueprints) that they like or want to play which they can recall at a moments notice. Alongside this, the API will also have an option to provide users with highly rated team comps if they would like to try new and learn new comps.

#### 2. Why is it a problem that needs solving?

This solves a problem for newer or casual players of the game that may not have complete knowledge of the games units and which ones work best together. It will also assist more experienced players by giving an insight into which team comps are best in the current meta (Most Effective Tactics Available). 

#### 3. Why have you chosen this database system. What are the drawbacks compared to others?

#### 4. Identify and discuss the key functionalities and benefits of an ORM

#### 5. Document all endpoints for your API

The endpoints of the api are displayed in the table below:  

| Endpoints      | Description | HTTP Requests |
| ---------      | ------------| ------------- |
| /register      | Allows for user registration | POST |
| /login         | Allows user to login | POST |
| /comps         | User can create a comp | POST |
| /comps/all     | User can view all of their created comps | GET |
| /comps/\<id:int>| User can view a specific comp | GET |
| /comps/\<id:int>| User can edit a specific comp | PATCH |
| /comps/\<id:int>| User can delete a specific comp | DELETE |
| /comps/stier   | User can view the S tier comps | GET |
| /champs        | User can view all champions | GET |
| /champs        | Admin can create a champion | POST |
| /champs/\<id:int>| Admin can delete a champion | DELETE |
| /traits        | User can view all traits and a description | GET |
| /traits        | Admin can create a trait | POST |
| /traits/\<id:int>| Admin can delete a trait | DELETE |

#### 6. An ERD for your app

#### 7. Detail any third party services that your app will use

#### 8. Describe your projects models in terms of the relationships they have with each other

#### 9.	Discuss the database relations to be implemented in your application

#### 10.	Describe the way tasks are allocated and tracked in your project