# Migration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**credential_id** | **UUID** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**source_provider** | **str** |  | 
**source_summary** | **str** |  | [optional] 
**settings** | [**MigrationSettings**](MigrationSettings.md) |  | [optional] 
**error_message** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**mailbox_count** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from lockally.models.migration import Migration

# TODO update the JSON string below
json = "{}"
# create an instance of Migration from a JSON string
migration_instance = Migration.from_json(json)
# print the JSON string representation of the object
print(Migration.to_json())

# convert the object into a dict
migration_dict = migration_instance.to_dict()
# create an instance of Migration from a dict
migration_from_dict = Migration.from_dict(migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


