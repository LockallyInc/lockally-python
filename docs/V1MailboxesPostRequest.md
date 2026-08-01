# V1MailboxesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** | Optional; lockally generates if absent. | [optional] 
**quota_bytes** | **int** | 5 GB default. | [optional] [default to 5368709120]

## Example

```python
from lockally.models.v1_mailboxes_post_request import V1MailboxesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1MailboxesPostRequest from a JSON string
v1_mailboxes_post_request_instance = V1MailboxesPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1MailboxesPostRequest.to_json())

# convert the object into a dict
v1_mailboxes_post_request_dict = v1_mailboxes_post_request_instance.to_dict()
# create an instance of V1MailboxesPostRequest from a dict
v1_mailboxes_post_request_from_dict = V1MailboxesPostRequest.from_dict(v1_mailboxes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


