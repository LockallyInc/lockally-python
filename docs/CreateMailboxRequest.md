# CreateMailboxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** | Optional; lockally generates if absent. | [optional] 
**quota_bytes** | **int** | 5 GB default. | [optional] [default to 5368709120]

## Example

```python
from lockally.models.create_mailbox_request import CreateMailboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMailboxRequest from a JSON string
create_mailbox_request_instance = CreateMailboxRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMailboxRequest.to_json())

# convert the object into a dict
create_mailbox_request_dict = create_mailbox_request_instance.to_dict()
# create an instance of CreateMailboxRequest from a dict
create_mailbox_request_from_dict = CreateMailboxRequest.from_dict(create_mailbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


