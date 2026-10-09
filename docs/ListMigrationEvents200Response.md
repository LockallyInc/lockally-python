# ListMigrationEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MigrationEvent]**](MigrationEvent.md) |  | 

## Example

```python
from lockally.models.list_migration_events200_response import ListMigrationEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMigrationEvents200Response from a JSON string
list_migration_events200_response_instance = ListMigrationEvents200Response.from_json(json)
# print the JSON string representation of the object
print(ListMigrationEvents200Response.to_json())

# convert the object into a dict
list_migration_events200_response_dict = list_migration_events200_response_instance.to_dict()
# create an instance of ListMigrationEvents200Response from a dict
list_migration_events200_response_from_dict = ListMigrationEvents200Response.from_dict(list_migration_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


