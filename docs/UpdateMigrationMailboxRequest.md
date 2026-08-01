# UpdateMigrationMailboxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_email** | **str** |  | [optional] 
**status** | **str** | Can only be set to \&quot;skipped\&quot;. | [optional] 

## Example

```python
from lockally.models.update_migration_mailbox_request import UpdateMigrationMailboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMigrationMailboxRequest from a JSON string
update_migration_mailbox_request_instance = UpdateMigrationMailboxRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMigrationMailboxRequest.to_json())

# convert the object into a dict
update_migration_mailbox_request_dict = update_migration_mailbox_request_instance.to_dict()
# create an instance of UpdateMigrationMailboxRequest from a dict
update_migration_mailbox_request_from_dict = UpdateMigrationMailboxRequest.from_dict(update_migration_mailbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


