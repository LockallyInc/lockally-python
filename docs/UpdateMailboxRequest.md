# UpdateMailboxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**quota_bytes** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 

## Example

```python
from lockally.models.update_mailbox_request import UpdateMailboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMailboxRequest from a JSON string
update_mailbox_request_instance = UpdateMailboxRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMailboxRequest.to_json())

# convert the object into a dict
update_mailbox_request_dict = update_mailbox_request_instance.to_dict()
# create an instance of UpdateMailboxRequest from a dict
update_mailbox_request_from_dict = UpdateMailboxRequest.from_dict(update_mailbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


