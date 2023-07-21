# Union 

A Union type allows you to return different object types from a single field. It is useful when you want a field to be able to return more than one type of object.

For example, you may have a search query that can return different result types like Product or Article:

```python

import strawberry

@strawberry.type
class Product:
  id: strawberry.ID
  name: str
  price: float

@strawberry.type  
class Article:
  id: strawberry.ID
  title: str
  body: str
  
@strawberry.union
class SearchResult:
  @strawberry.type(Product)
  product: Product
  
  @strawberry.type(Article)
  article: Article
  
@strawberry.type
class Query:
  search: SearchResult

```

The SearchResult union defines two possible types - Product and Article.

When implementing the resolver, you can return either a Product or Article object:

``` python

@strawberry.type
class Query:
  def search(self, info) -> SearchResult:
    # Run search logic
    if product:
      return SearchResult(product=product)
      
    if article:  
      return SearchResult(article=article)

```

On the client, the search field will return either a Product or Article object.

This allows implementing generic search functionality that can return different object types in GraphQL.


---

# Interface

An Interface defines a common set of fields that different object types must implement. It's useful when you want to return related objects under a common type.

For example, you may have Product and Article types that both share common fields like id, title, description:

```python


import strawberry

@strawberry.interface
class Content:
  id: strawberry.ID
  title: str
  description: str

@strawberry.type
class Product(Content):
  price: float

@strawberry.type  
class Article(Content):
  body: str
```

Both Product and Article implement the Content interface.

You can then define a query that returns the interface type:

```python

@strawberry.type
class Query:
  contents: List[Content]
The resolver can return a list of mixed object types:

```

```python


@strawberry.type
class Query:
  def contents(self) -> List[Content]:
    return [
      Product(id=1, title="Product 1", price=9.99), 
      Article(id=2, title="Article 1", body="...")
    ]
```
On the client, the contents field will return the common Content fields for each object.

This allows implementing generic queries and sharing field definitions using interfaces in GraphQL with Strawberry.

---

# Fragments

*What are fragments?*

Fragments allow you to define reusable pieces of a GraphQL query.
You can extract common query fields into a fragment and reuse it in multiple queries.
Fragments are defined using the fragment keyword.

*Why are fragments useful?*

Remove duplicate code - Extract common fields into a fragment instead of repeating.
Split complex queries - Break down queries into smaller focused fragments.
Target specific types - Define fragments for a specific object type.

*How to use fragments?*

Define the fragment with named selection set:
<!---->

```
fragment userFields on User {
  id
  name
}
```

Include the fragment in queries using ...:
<!---->

```
query {
  user(id: 1) {
    ...userFields
  }
}

```

Fragments can be nested and combined.
Fragments can be defined inline or at root.
GraphQL fragments allow you to reuse selection sets in multiple queries. They help reduce duplication and decompose complex queries into modular pieces. Fragments are defined once then included using fragment spread.

*Example*


Here is an example to illustrate how fragments work in GraphQL:

First define a reusable fragment for fields on a User:

```
fragment userFields on User {
  id 
  name
  profilePic 
}

```

This fragment selects the id, name and profilePic for a User object.

You can then use this fragment in a query:

```

query {
  user(id: 4) {
    ...userFields
    email 
  }
}
```

The ...userFields includes the id, name and profilePic selection set defined in the fragment.

You can also use the same fragment in a different query:

```

query {
  users {
    ...userFields
  }
}
```
The fragment is reusable across multiple query operations.

Some key points:

Fragments remove duplicate field selections
Fragment name and type must match usage
Spread fragments using ...fragmentName
Can define fragments inline or in root
So fragments help decompose complex queries and reduce duplication.

---

