# MigrationMailbox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**migration_id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**source_email** | **str** |  | 
**dest_email** | **str** |  | [optional] 
**dest_mailbox_id** | **UUID** |  | [optional] 
**status** | **str** |  | 
**source_message_count** | **int** |  | [optional] 
**synced_message_count** | **int** |  | 
**failed_message_count** | **int** |  | 
**source_size_bytes** | **int** |  | [optional] 
**synced_size_bytes** | **int** |  | [optional] 
**last_synced_uid** | **str** |  | [optional] 
**last_synced_at** | **datetime** |  | [optional] 
**error_message** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from lockally.models.migration_mailbox import MigrationMailbox

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationMailbox from a JSON string
migration_mailbox_instance = MigrationMailbox.from_json(json)
# print the JSON string representation of the object
print(MigrationMailbox.to_json())

# convert the object into a dict
migration_mailbox_dict = migration_mailbox_instance.to_dict()
# create an instance of MigrationMailbox from a dict
migration_mailbox_from_dict = MigrationMailbox.from_dict(migration_mailbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


