# MigrationProgressMailboxesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_email** | **str** |  | 
**dest_email** | **str** |  | [optional] 
**status** | **str** |  | 
**source_message_count** | **int** |  | [optional] 
**synced_message_count** | **int** |  | 
**failed_message_count** | **int** |  | 
**percent_complete** | **float** |  | 

## Example

```python
from lockally.models.migration_progress_mailboxes_inner import MigrationProgressMailboxesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationProgressMailboxesInner from a JSON string
migration_progress_mailboxes_inner_instance = MigrationProgressMailboxesInner.from_json(json)
# print the JSON string representation of the object
print(MigrationProgressMailboxesInner.to_json())

# convert the object into a dict
migration_progress_mailboxes_inner_dict = migration_progress_mailboxes_inner_instance.to_dict()
# create an instance of MigrationProgressMailboxesInner from a dict
migration_progress_mailboxes_inner_from_dict = MigrationProgressMailboxesInner.from_dict(migration_progress_mailboxes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


