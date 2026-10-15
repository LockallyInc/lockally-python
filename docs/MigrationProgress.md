# MigrationProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_id** | **UUID** |  | 
**status** | **str** |  | 
**total_mailboxes** | **int** |  | 
**completed_mailboxes** | **int** |  | 
**failed_mailboxes** | **int** |  | 
**total_messages** | **int** |  | 
**synced_messages** | **int** |  | 
**failed_messages** | **int** |  | 
**percent_complete** | **float** |  | 
**mailboxes** | [**List[MigrationProgressMailboxesInner]**](MigrationProgressMailboxesInner.md) |  | 

## Example

```python
from lockally.models.migration_progress import MigrationProgress

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationProgress from a JSON string
migration_progress_instance = MigrationProgress.from_json(json)
# print the JSON string representation of the object
print(MigrationProgress.to_json())

# convert the object into a dict
migration_progress_dict = migration_progress_instance.to_dict()
# create an instance of MigrationProgress from a dict
migration_progress_from_dict = MigrationProgress.from_dict(migration_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


