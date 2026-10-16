# MigrationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_concurrent_mailboxes** | **int** |  | [optional] 
**max_concurrent_messages** | **int** |  | [optional] 
**source_rate_limit** | **int** |  | [optional] 
**batch_size** | **int** |  | [optional] 
**skip_folders** | **List[str]** |  | [optional] 

## Example

```python
from lockally.models.migration_settings import MigrationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationSettings from a JSON string
migration_settings_instance = MigrationSettings.from_json(json)
# print the JSON string representation of the object
print(MigrationSettings.to_json())

# convert the object into a dict
migration_settings_dict = migration_settings_instance.to_dict()
# create an instance of MigrationSettings from a dict
migration_settings_from_dict = MigrationSettings.from_dict(migration_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


