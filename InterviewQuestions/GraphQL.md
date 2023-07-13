# GraphQL interview Questions

1. Explain what GraphQL is? Does it belong under database technology?

While this may seem like a fundamental GraphQL interview question, you can make the answer interesting by adding your personal experience with the language.

GraphQL is a query language invented by Facebook in 2012 that offers a standard interface for data retrieval and modification between the client and the server. The client uses queries to request data from the GraphQL server. Client-specified inquiries are those in which the answer format is described in the query and determined by the client rather than the server.

As opposed to standard REST APIs, the data structure is not hardcoded, making data retrieval from the server more efficient for the client.

GraphQL is frequently misunderstood as database technology; however, this is a widespread misunderstanding. GraphQL is an API query language. In that respect, it's database agnostic, meaning it can work with any database or perhaps none at all.

---

2. How does GraphQL utilize the data loading process?
   
When users use GraphQL to request data, it merely retrieves the least amount of data necessary by the client. Even if the object model has a large number of fields, the client can only request the required fields.

---

3. What are the key concepts of GraphQL?


GraphQL has some key concepts. They are:

- Hierarchical
- Product-centric
- Strong-typing
- Client-specific queries
- Introspective

---

4. List down the primary operations that GraphQL supports.

The three sorts of operations supported by GraphQL are query, mutation, and subscription. The request is made using the query, which is a read action; mutation is used for write operations, and subscription is used to listen for any data changes. If the client is subscribed to that event, the server sends a notification message to the client whenever data changes.

---

5. What is Over-fetching in GraphQL?
   
Over-fetching is a response where the client gets too much data or extra data for an API request. In over-fetching, you have a lot of additional data in the response you don't use. Over-fetching unnecessarily increases the payload size.

---

6. What is Under-fetching?
   
Under-fetching is a response where the client doesn't get enough data. The under-fetching response doesn't have enough data with a call to an endpoint, so you have to call a second endpoint to fulfil your request or multiple API calls to fetch the complete data.

---

7. What is difference between REST and GraphQL?
   
While both REST and GraphQL can be used to get and post data from web service there are multiple differences between them but the the core difference between GraphQL and REST APIs is that GraphQL is a specification, a query language, while REST is an architectural concept and because of that GraphQL offers several advantage over REST. 

For example, with GraphQL you can reduce number of web service calls to the server. Suppose, if you need both Customer and Order data then instead of sending two query to customer and Order API over REST, you can just use one query to get both of these data using GraphQL. 

---

8. What can you tell us about authentication in GraphQL?
   
Authentication is basically a mechanism where you give permissions to authenticated users in your application. Using GraphQL, you can delegate the authorization using a business logic that describes whether a user has authorization for performing an action or not.

---

10. What are some of the features of authentication in GraphQL?
    
A GraphQL authentication must be able to authenticate schema at the field level. It must provide the context of the current user to the resolvers. The logic must also be hidden from the resolvers. 

---

11. How can you handle server-side caching in the GraphQL language?
    
In REST API, it is easy to implement caching as you are able to cache data for each endpoint since there is no change in data structures. But in GraphQL, the similar call is not known, and therefore it is difficult to cache. 

---

12. What kind of response do you get in the GraphQL language?
    
If you are using GraphQL, whenever a client requests something from the server, it sends back the response in the JSON format. 

---

13. What is Fragment in GraphQL?
    
When the query in GraphQL is huge and contains reusable components, the fragment is utilized. You may utilize the reusable portion to construct a fragment, which you can then use in the query. The notion of the fragment was created to make it easy to organize code and reduce duplication.

---

14. What are the main operations that GraphQL supports?

GraphQL supports three types of operations: query, mutation, and subscription. The query is used for the request, and it is a read operation, the mutation is used for write operations, and subscription is used for listening for any data changes. The server sends a notification message to the client after any data changes, if the client is subscribed to that event.

---

15.  What is difference between Mutation and Query?

Technically any GraphQL query could be implemented to cause a data write. But there is a convention that any operations that cause writes should be sent explicitly via a mutation.

Besides the difference in the semantic, there is one important technical difference:

Query fields can be executed in parallel by the GraphQL engine while Mutation top-level fields MUST execute serially according to the spec.

---

16. What is GraphQL schema?
    
Every GraphQL server has two core parts that determine how it works: a schema and resolve functions.

The schema is a model of the data that can be fetched through the GraphQL server. It defines what queries clients are allowed to make, what types of data can be fetched from the server, and what the relationships between these types are.

---

17. What is SDL, and what is the use of it?

SDL is an acronym that stands for Schema Definition Language. It is used for writing schemas. SDL is the language that is used to write GraphQL schemas.

---

18. What do you know by Fields in GraphQL?

The keys of an object that are used in the GraphQL query are known as Fields.

For example:

{  
employee{  
name  
salary  
}  
}  
In the above query, 'name' and 'salary' are fields.

---

19. What is the use of object types in GraphQL?
    
The resources that are accessed by a client is called Objects. Objects can contain a list of GraphQL fields.

---

20. What is the use of an interface in GraphQL?
    
In GraphQL, an interface is used to define a contract for a group of fields that objects can implement. It allows you to define a set of common fields and their return types, which multiple types can then implement.

The main purpose of an interface in GraphQL is to enable polymorphism and provide a way to query and access fields on different object types without explicitly knowing their concrete types. Interfaces are similar to abstract classes or protocols in other programming languages.

---

21. What is the union in GraphQL?
    
In GraphQL, sometimes we have to represent multiple objects, that's why the union is used. The user can define more than one type as return type using a union.

Union types are similar to interfaces however, while interfaces dictate fields that must be common to all implementations, unions do not. Unions only represent a selection of allowed types and make no requirements on those types.

---

22. What is resolvers in GrpahQL?

In Strawberry, resolvers are functions that are responsible for resolving the value of a field in a GraphQL schema. They determine how the data for a field is retrieved or computed. Resolvers are defined using the @strawberry.field decorator in Strawberry.

Here's an example of how to define resolvers in Strawberry:

```python

import strawberry

@strawberry.type
class User:
    name: str

@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        # Resolver logic to fetch user data
        return User(name="John Doe")
```

In this example, we define a User object type with a single field name. We then define a Query type with a field called user. The resolver for the user field is the method user within the Query class.

The resolver function (user in this case) can have any name, and it should be decorated with @strawberry.field. The return type of the resolver function (User in this case) should match the type of the field it is resolving.

The resolver function is responsible for fetching the data for the field. In this simple example, we are directly returning a User object with a predefined name. In real-world scenarios, the resolver would typically interact with a database, an API, or perform some computation to retrieve the data for the field.
---
