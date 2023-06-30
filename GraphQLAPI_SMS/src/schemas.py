import strawberry
from resolvers import schema

schema = strawberry.Schema(query=schema.Query, mutation=schema.Mutation)
