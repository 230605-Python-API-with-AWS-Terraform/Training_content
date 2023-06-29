#Schema

```graphql
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
}

type Query {
  getUser(id: ID!): User
  getPost(id: ID!): Post
  getAllUsers: [User!]!
  getAllPosts: [Post!]!
}

type Mutation {
  createUser(name: String!, email: String!): User!
  createPost(title: String!, content: String!, authorId: ID!): Post!
  updateUser(id: ID!, name: String, email: String): User!
  updatePost(id: ID!, title: String, content: String): Post!
  deleteUser(id: ID!): Boolean!
  deletePost(id: ID!): Boolean!
}
```

Queries:

**Get a user by ID:**
```graphql

query {
  getUser(id: "user_id") {
    id
    name
    email
    posts {
      id
      title
    }
  }
}
```
**Get a post by ID:**
```graphql

query {
  getPost(id: "post_id") {
    id
    title
    content
    author {
      id
      name
    }
  }
}
```
**Get all users:**
```graphql

query {
  getAllUsers {
    id
    name
    email
    posts {
      id
      title
    }
  }
}
```

**Get all posts:**

```graphql

query {
  getAllPosts {
    id
    title
    content
    author {
      id
      name
    }
  }
}
```

**Mutations:**

*Create a user:*
```graphql

mutation {
  createUser(name: "John Doe", email: "john@example.com") {
    id
    name
    email
  }
}
```
*Create a post:*

```graphql

mutation {
  createPost(title: "New Post", content: "This is the content", authorId: "user_id") {
    id
    title
    content
    author {
      id
      name
    }
  }
}
```
**Update a user:**
```graphql

mutation {
  updateUser(id: "user_id", name: "Jane Doe", email: "jane@example.com") {
    id
    name
    email
  }
}
```
**Update a post:**
```graphql

mutation {
  updatePost(id: "post_id", title: "Updated Title", content: "Updated content") {
    id
    title
    content
    author {
      id
      name
    }
  }
}
```
**Delete a user:**
```graphql

mutation {
  deleteUser(id: "user_id")
}
```
**Delete a post:**
```graphql

mutation {
  deletePost(id: "post_id")
}
```
**Get the number of users:**
```graphql

query {
  getAllUsers {
    totalCount
  }
}
```
**Get the number of posts:**
```graphql

query {
  getAllPosts {
    totalCount
  }
}
```
**Get users with their posts:**
```graphql

query {
  getAllUsers {
    id
    name
    email
    posts {
      id
      title
      content
    }
  }
}
```
**Get posts authored by a specific user:**
```graphql

query {
  getUser(id: "user_id") {
    id
    name
    email
    posts {
      id
      title
      content
    }
  }
}
```
**Get the latest posts:**
```graphql

query {
  getAllPosts {
    id
    title
    content
    author {
      id
      name
    }
  }
}
```
**Get posts with a specific keyword in the title:**
```graphql

query {
  getAllPosts(filter: { keyword: "GraphQL" }) {
    id
    title
    content
    author {
      id
      name
    }
  }
}
```
**Get users with a certain email domain:**
```graphql

query {
  getAllUsers(filter: { email_contains: "example.com" }) {
    id
    name
    email
    posts {
      id
      title
    }
  }
}
```
**Get posts created within a specific time range:**
```graphql

query {
  getAllPosts(filter: { createdAt_gte: "2023-01-01", createdAt_lte: "2023-06-30" }) {
    id
    title
    content
    author {
      id
      name
    }
  }
}
```
**Get the total count of posts for each user:**
```graphql

query {
  getAllUsers {
    id
    name
    email
    postCount: posts_aggregate {
      aggregate {
        count
      }
    }
  }
}
```
**Get the average length of posts for a user:**
```graphql

query {
  getUser(id: "user_id") {
    id
    name
    email
    averagePostLength: posts_aggregate {
      aggregate {
        avg {
          content_length
        }
      }
    }
  }
}
```
**Get the most recent posts for each user:**
```graphql

query {
  getAllUsers {
    id
    name
    email
    recentPosts: posts(order_by: { createdAt: desc }, limit: 5) {
      id
      title
      createdAt
    }
  }
}
```


**Get posts sorted by the number of comments they have:**
```graphql
query {
  getAllPosts {
    id
    title
    content
    commentCount: comments_aggregate {
      aggregate {
        count
      }
    }
  }
}
```

**Get users and their posts with pagination:**
```graphql
query {
  getAllUsers {
    id
    name
    email
    posts(first: 5, after: "cursor") {
      edges {
        node {
          id
          title
        }
        cursor
      }
      pageInfo {
        endCursor
        hasNextPage
      }
    }
  }
}
```

**Search for posts based on a keyword in the title or content:**
```graphql
query {
  searchPosts(keyword: "GraphQL") {
    id
    title
    content
    author {
      id
      name
    }
  }
}
```

**Get the most active users based on the number of posts they have:**
```graphql
query {
  getMostActiveUsers {
    id
    name
    email
    postCount
  }
}
```

**Get posts created by multiple authors:**
```graphql
query {
  getPostsByAuthors(authorIds: ["author_id1", "author_id2"]) {
    id
    title
    content
    author {
      id
      name
    }
  }
}
```

