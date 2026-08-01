# MigrationEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**migration_id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**mailbox_id** | **UUID** |  | [optional] 
**event_type** | **str** |  | 
**actor** | **str** |  | 
**old_status** | **str** |  | [optional] 
**new_status** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from lockally.models.migration_event import MigrationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationEvent from a JSON string
migration_event_instance = MigrationEvent.from_json(json)
# print the JSON string representation of the object
print(MigrationEvent.to_json())

# convert the object into a dict
migration_event_dict = migration_event_instance.to_dict()
# create an instance of MigrationEvent from a dict
migration_event_from_dict = MigrationEvent.from_dict(migration_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


