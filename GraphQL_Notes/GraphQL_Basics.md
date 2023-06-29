**What is GraphQL?**

- GraphQL is a new API standard that provides a more efficient, powerful and flexible alternative to REST (Representational State Transfer).
- It was developed and open sourced by Facebook, and is now maintained by a large community of companies and individuals from all over the world.
- At its core, GraphQL enables declarative data fetching where a client can specify exactly what data it needs from an API.
- Instead of multiple endpoints that return fixed data structures, a GraphQL server only exposes a single endpoint and responds with precisely the data that a client asked for.

**How does it all work?**

- Most applications today have the need to fetch data that's stored remotely in some database that's accessible over the Internet.
- That's what servers are used for.
- Whenever a client needs some information that it wants to display to the user, it sends a request to the server.
- The server is programmed in a way that it can respond to the request by retrieving the appropriate information from the database, and then sends it back to the client.

**History**

- REST has been a popular way to expose data from a server.When the concept of REST APIs was developed, client applications were relatively simple and the development speed wasn't nearly where it is today.REST thus was a good fit for many applications however the API landscape has radically changed over the last couple of years.In particular there are three factors that have been challenging the way how APIs are designed. Increased mobile usage, low-power devices and sloppy networks were the initial reasons why Facebook developed GraphQL.GraphQL minimizes the amount of data that needs to be transferred over the network and thus majorly improves applications operating under these conditions.The heterogeneous landscape of front-end frameworks and platforms that run client applications make it difficult to build and maintain one API that would fit the requirements of all the different clients. With GraphQL each client can access precisely the data it needs.Continuous Deployment has become a standard for many companies.Rapid iterations and frequent product updates are indispensable.
- With REST APIs the way how data is exposed by the server often needs to be modified to account for specific requirements and design changes on the client-side. This hinders fast development practices and product iterations.

- Facebook started using GraphQL already in 2012 in their native mobile apps.The first time Facebook publicly spoke about GraphQL was at React.js Conf 2015.And shortly after they announced their plans to open source it. Because Facebook always used to speak about GraphQL in the context of React, it took a while for non-React developers to understand that GraphQL was by no means a technology that was limited to usage with React. In fact, GraphQL is a technology that can be used everywhere where a client communicates with an API. It's interesting to note that other companies like Netflix or Coursera were working on comparable ideas to make API interactions more efficient. Coursera envisioned a similar technology to let a client specify its data requirements and Netflix even open sourced their solution called Falcor.

- After GraphQL was open sourced, Coursera completely canceled their own efforts and hopped on the GraphQL train.
Today GraphQL is used in production by lots of different companies such as GitHub, Twitter, Yelp or Shopify to name only a few.


**Why GraphQL is the better REST?.**

- GraphQL is more of an evolution of what REST already brings to the table.Now, REST has really been the standard for designing web APIs.However, there are many shortcomings as a result of various different types of clients, things like mobile apps, smart TV applications, and so many others. There was a need for an API which provided a little bit more flexibility than what REST provides. And this is where GraphQL really shines.
- To really see what are the major differences between the two, let's take a blogging app as an example.

- So we want to fetch the posts of a user and their three most recent followers.
- In a RESTful API, you would need to make requests to three different endpoints.
- To fetch the user themselves, you could use the /users/< id > endpoint.
- To fetch their posts, you could use the /users/< id >/posts.
- And the same with followers (/user/< id >/followers).

- Now, as you noticed, the user endpoint returned their ID, name, address, and birthday.

*However, what if we really only needed their name?*

- We don't really get much of a choice. And same thing with the post.We just needed the title of the post, but we got a bunch of other details, like comments.
- Now let's take a look at how to do that in GraphQL.
```graphql
query
{
    User(id:"er3tg439frjw")
    {
        name
        posts
        {
            title
        }
        followers(last:3)
        {
            name
        }
    }
} 
```
- In this Query, the user ID gets specified, and then we just request the name, and then we just want to get the posts of that user, just the title of those posts, and then the followers.
Now, a couple of key things to note here is we only made a single request, and we got back exactly the data that we asked for.Additionally, GraphQL only has a single endpoint.

- We have an *`over-fetching`* problem with the RESTful APIs. What that meant was... we got a lot of additional information that the client really did not need.Now, if you have applications with very tight resource requirements and they don't have too much memory, having to process additional data can be a huge problem.

- With REST APIs, we could also have an `*under-fetching*` problem. For instance, let's say we wanted to get the posts of multiple users and the followers of those users. We would need to make a request to the user's endpoint to fetch the list of users, and then loop through each of those users, get their IDs, and then fetch the posts and followers. So you could imagine how many requests the client would need to make just to get that information.
Now with GraphQL, you can simply request the user's query and specify the posts of those users, as well as the followers, in a single query.

---
<blockquote>
A common pattern with RESTful APIs is to create endpoints that are tailor-made for views that are inside your app.
Now, if those requirements change, or if new clients need to access information, you would either need to ask the backend engineers to make changes to the existing API,or create new endpoints to meet the additional requirements.
With GraphQL, this is no longer an issue because the client can specify exactly the fields they need and if anything changes,they just need to update the query without needing to ask the backend engineers to make changes.
Because each client specifies exactly the information it needs, you can gain a lot of insights around what information is being requested,and what are the performance bottlenecks, so you can intelligently remove unnecessary pieces of information and optimize the speed of your application.

GraphQL uses a strong type system to define the capability of the API, and it does so using what is known as the Schema Definition Language, or the SDL.The SDL acts as a contract between the frontend and backend engineers, so that frontend developers know exactly what information they can query for,and the backend engineers can just implement how that information can be accessed.
</blockquote>

---

