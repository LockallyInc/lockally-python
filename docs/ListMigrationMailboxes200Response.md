# ListMigrationMailboxes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MigrationMailbox]**](MigrationMailbox.md) |  | 

## Example

```python
from lockally.models.list_migration_mailboxes200_response import ListMigrationMailboxes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMigrationMailboxes200Response from a JSON string
list_migration_mailboxes200_response_instance = ListMigrationMailboxes200Response.from_json(json)
# print the JSON string representation of the object
print(ListMigrationMailboxes200Response.to_json())

# convert the object into a dict
list_migration_mailboxes200_response_dict = list_migration_mailboxes200_response_instance.to_dict()
# create an instance of ListMigrationMailboxes200Response from a dict
list_migration_mailboxes200_response_from_dict = ListMigrationMailboxes200Response.from_dict(list_migration_mailboxes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


