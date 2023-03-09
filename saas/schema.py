# schema.py
import os
import time

from ariadne import (
    QueryType,
    ScalarType,
    MutationType,
    make_executable_schema,
    load_schema_from_path,
    gql,
)

from users.query_resolvers import *
from app.query_resolvers import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
schema_path = os.path.join(BASE_DIR, "schema.graphql")

type_defs = gql(load_schema_from_path(schema_path))

# scaler types

datetime_scalar = ScalarType("Datetime")
image_scalar = ScalarType("Image")


@datetime_scalar.serializer
def serialize_datetime(value):

    timestamp = str(time.mktime(value.timetuple()))

    return timestamp


@image_scalar.serializer
def serialize_image(value):

    image = value.url

    return image


# query and mutation types

query = QueryType()
mutation = MutationType()

# resolvers

# # query resolvers

# # # user app query resolvers

query.set_field("getAllUsers", resolve_getAllUsers)
query.set_field("getUserByPublicId", resolve_getUserByPublicId)
query.set_field("getUserByUsername", resolve_getUserByUsername)

query.set_field("getAllProfiles", resolve_getAllProfiles)
query.set_field("getProfileByPublicId", resolve_getProfileByPublicId)

# # # app app query resolvers

query.set_field("getAllCategories", resolve_getAllCategories)
query.set_field("getCategoryByPublicId", resolve_getCategoryByPublicId)

query.set_field("getAllAccounts", resolve_getAllAccounts)
query.set_field("getAccountByPublicId", resolve_getAccountByPublicId)

query.set_field("getAllBudgets", resolve_getAllBudgets)
query.set_field("getBudgetByPublicId", resolve_getBudgetByPublicId)

query.set_field("getAllTransactions", resolve_getAllTransactions)
query.set_field("getTransactionByPublicId", resolve_getTransactionByPublicId)

query.set_field("getAllReports", resolve_getAllReports)
query.set_field("getReportByPublicId", resolve_getReportByPublicId)

schema = make_executable_schema(
    type_defs, [query, mutation, datetime_scalar, image_scalar]
)
