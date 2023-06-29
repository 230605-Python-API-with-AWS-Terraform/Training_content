**What’s Strawberry GraphQL?**

Strawberry is a `code-first GraphQL server library` that uses Python type annotations to define GraphQL types.

💡GraphQL server libraries come in two general “flavors”: `code-first and schema-first.` 

- With a schema-first library, you create a static schema file using GraphQL’s schema definition language (SDL). You then define resolvers for your fields in your code.
- With a code-first library (such as Strawberry), you instead define your schema’s types and fields programmatically, using features of the library and language.

Let’s look at an example of generating GraphQL types with Strawberry. The first snippet below shows three object types defined using SDL. The second snippet shows those same three types defined using Strawberry:

```
type User
{
	id:ID!
}

type Product
{
	id:ID!
}

type Order
{
	id:ID!
	buyer:User!
	items:[Product!]!
	shippingCost:Float
}

```

```python

import strawberry

@strawberry.type
class User:
	id:strawberry.ID
@strawberry.type
class Product:
	id:strawberry.ID

@strawberry.type
class Order:
	id:strawberry.ID
	buyer:User
	items:list[Product]
	shipping_cost:float|None
```


These two snippets look pretty similar! Python’s syntax and type hints provide a `code-first experience` that’s very “SDL-like”.

Note the following about the Strawberry snippet:

- We annotate each type with `@strawberry.type`. This is specifically the annotation for defining object types. You can use `@strawberry.input` and `@strawberry.interface` for input types and interfaces, respectively.
As mentioned above, Strawberry takes advantage of Python type hints. For example, when writing buyer: User, we’re specifying that this class has a field called buyer of type User. This information is then used by Strawberry to create the GraphQL type.Strawberry automatically converts snake_case field names to camelCase in your schema, so you can use Python casing conventions in your code. When defining fields in SDL, we have to explicitly mark non-nullable fields using ! `(for example, buyer: User!)`. Python’s type system uses the opposite convention, meaning every field is non-nullable by default.To designate a field as nullable with Strawberry, we use the | operator with None, which indicates that the field’s value can also be None.

---

##Schema Types

*`Object type @strawberry.type (Object Type)`:*
```python

import strawberry

@strawberry.type
class User:
    id: int
    name: str
    email: str
```
In this example, we define an object type User with three fields: id, name, and email. Each field has a specific type (int and str) representing the data associated with a user.

*`Input type @strawberry.input (Input Type):`*
```python

import strawberry

@strawberry.input
class CreateUserInput:
    name: str
    email: str
    password: str
```

Here, we define an input type CreateUserInput with three fields: name, email, and password. Input types are used as arguments in mutations or queries to pass structured data.

*`Scalar type @strawberry.scalar (Scalar Type):`*

```python

import strawberry

@strawberry.scalar
class Date:
    @staticmethod
    def serialize(value):
        # Logic to serialize a Python value to a scalar value
        return str(value)

    @staticmethod
    def parse_literal(node):
        # Logic to parse a GraphQL literal value to a Python value
        return node.value

    @staticmethod
    def parse_value(value):
        # Logic to parse a GraphQL input value to a Python value
        return value
```
In this example, we define a custom scalar type Date. We provide methods (serialize, parse_literal, and parse_value) to handle serialization and parsing of values between GraphQL and Python representations.

*`Enum type @strawberry.enum (Enum Type):`*
```python

import strawberry

@strawberry.enum
class UserRole:
    ADMIN = "ADMIN"
    USER = "USER"
    MODERATOR = "MODERATOR"
```
Here, we define an enum type UserRole representing different roles a user can have. The enum values are defined as class attributes.

*`Interface type @strawberry.interface (Interface Type):`*

```python

import strawberry

@strawberry.interface
class Node:
    id: strawberry.ID

@strawberry.type
class User(Node):
    name: str
    email: str
```
In this example, we define an interface type Node with a single field id. We then create an object type User that implements the Node interface, along with additional fields (name and email).

*`Union type @strawberry.union (Union Type):`*

```python

import strawberry

@strawberry.type
class Dog:
    name: str
    breed: str

@strawberry.type
class Cat:
    name: str
    color: str

@strawberry.union
class Pet:
    # Union can include Dog and Cat types
    Dog
    Cat
```

In this example, we define two object types Dog and Cat, representing different types of pets. We then define a union type Pet that includes both Dog and Cat types. This indicates that a field of type Pet can return either a Dog or a Cat object.

---
**.graphql files**

GraphQL files, often referred to as .graphql files, are text files that contain GraphQL schema definitions, queries, mutations, subscriptions, and other GraphQL-related content. They follow the GraphQL syntax 

---

## Directives

**Operation directives**
GraphQL uses directives to modify the evaluation of an item in the schema or the operation. Operation directives can be included inside any operation (query, subscription, mutation) and can be used to modify the execution of the operation or the values returned by the operation.

Directives can help avoid having to create resolvers for values that can be computed via the values of additional fields.

All Directives are proceeded by `@ `symbol

**Default Operation directives**

Strawberry provides two default operation directives:

- `@skip(if: Boolean!)` - if Boolean is true, the given item is NOT resolved by the GraphQL Server

- `@include(if: Boolean!)` - if Boolean is false, the given item is NOT resolved by the GraphQL Server

📝 Note
`@deprecated(reason: String)` IS NOT compatible with Operation directives. @deprecated is exclusive to Schema Directives

*Examples of Default Operation directives*

```
# @include
query getPerson($includePoints: Boolean!) {
  person {
    name
    points @include(if: $includePoints)
  }
}

# @skip
query getPerson($hideName: Boolean!) {
  person {
    name @skip(if: $hideName)
    points
  }
}
```

**Custom Operation directives**

Custom directives must be defined in the schema to be used within the query and can be used to decorate other parts of the schema.

```
# Definition
@strawberry.directive(
    locations=[DirectiveLocation.FIELD], description="Make string uppercase"
)
def turn_uppercase(value: str):
    return value.upper()


@strawberry.directive(locations=[DirectiveLocation.FIELD])
def replace(value: str, old: str, new: str):
    return value.replace(old, new)

# Use
query People($identified: Boolean!) {
  person {
    name @turnUppercase
  }
  jess: person {
    name @replace(old: "Jess", new: "Jessica")
  }
  johnDoe: person {
    name @replace(old: "Jess", new: "John") @include(if: $identified)
  }
}
```

**Locations for Operation directives**

Directives can only appear in specific locations inside the query. These locations must be included in the directive's definition. In Strawberry the location is defined in the directive function's parameter locations.

```
@strawberry.directive(locations=[DirectiveLocation.FIELD])
```

**Operation directives possible locations**

Operation directives can be applied to many different parts of an operation. Here's the list of all the allowed locations:

- QUERY
- MUTATION
- SUBSCRIPTION
- FIELD
- FRAGMENT_DEFINITION
- FRAGMENT_SPREAD
- INLINE_FRAGMENT

---

**Resolvers**

In Strawberry, a resolver is a function or method that defines the logic for resolving GraphQL fields. Resolvers are responsible for fetching and returning the data associated with a specific field in the GraphQL schema.



Let's say we have a simple GraphQL schema with a User type and a Query type:

```python

import strawberry

@strawberry.type
class User:
    id: int
    name: str

@strawberry.type
class Query:
    @strawberry.field
    def user(self, user_id: int) -> User:
        # Logic to fetch user data from a data source
        user_data = fetch_user_from_database(user_id)
        return User(id=user_data.id, name=user_data.name)

```
In this example, we define a User type with id and name fields, and a Query type with a user field.

The resolver for the user field is the user method defined within the Query class. It takes an argument user_id of type int, which represents the ID of the user to fetch.

Inside the resolver, you would typically implement the logic to retrieve user data from a data source, such as a database. Here, the function fetch_user_from_database is a placeholder for the actual code that retrieves user data based on the provided user_id. The resolved data is then used to create an instance of the User type, which is returned as the result of the resolver.

When a query is executed that includes the user field with the user_id argument, the resolver function will be invoked, and the specified user will be fetched and returned.

---