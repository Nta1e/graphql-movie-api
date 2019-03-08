import graphene
import initial.schema

class Query(initial.schema.Query, graphene.ObjectType):
    pass

class Mutation(initial.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
