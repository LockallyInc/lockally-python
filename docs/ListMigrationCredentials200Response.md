# ListMigrationCredentials200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MigrationCredential]**](MigrationCredential.md) |  | 

## Example

```python
from lockally.models.list_migration_credentials200_response import ListMigrationCredentials200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMigrationCredentials200Response from a JSON string
list_migration_credentials200_response_instance = ListMigrationCredentials200Response.from_json(json)
# print the JSON string representation of the object
print(ListMigrationCredentials200Response.to_json())

# convert the object into a dict
list_migration_credentials200_response_dict = list_migration_credentials200_response_instance.to_dict()
# create an instance of ListMigrationCredentials200Response from a dict
list_migration_credentials200_response_from_dict = ListMigrationCredentials200Response.from_dict(list_migration_credentials200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


