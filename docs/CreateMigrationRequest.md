# CreateMigrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**credential_id** | **UUID** |  | 
**source_provider** | **str** |  | 
**settings** | [**MigrationSettings**](MigrationSettings.md) |  | [optional] 

## Example

```python
from lockally.models.create_migration_request import CreateMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMigrationRequest from a JSON string
create_migration_request_instance = CreateMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMigrationRequest.to_json())

# convert the object into a dict
create_migration_request_dict = create_migration_request_instance.to_dict()
# create an instance of CreateMigrationRequest from a dict
create_migration_request_from_dict = CreateMigrationRequest.from_dict(create_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


