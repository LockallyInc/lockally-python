# UpdateMigrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**settings** | [**MigrationSettings**](MigrationSettings.md) |  | [optional] 

## Example

```python
from lockally.models.update_migration_request import UpdateMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMigrationRequest from a JSON string
update_migration_request_instance = UpdateMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMigrationRequest.to_json())

# convert the object into a dict
update_migration_request_dict = update_migration_request_instance.to_dict()
# create an instance of UpdateMigrationRequest from a dict
update_migration_request_from_dict = UpdateMigrationRequest.from_dict(update_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


