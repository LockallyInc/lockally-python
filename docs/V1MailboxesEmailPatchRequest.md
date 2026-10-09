# V1MailboxesEmailPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**quota_bytes** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 

## Example

```python
from lockally.models.v1_mailboxes_email_patch_request import V1MailboxesEmailPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1MailboxesEmailPatchRequest from a JSON string
v1_mailboxes_email_patch_request_instance = V1MailboxesEmailPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1MailboxesEmailPatchRequest.to_json())

# convert the object into a dict
v1_mailboxes_email_patch_request_dict = v1_mailboxes_email_patch_request_instance.to_dict()
# create an instance of V1MailboxesEmailPatchRequest from a dict
v1_mailboxes_email_patch_request_from_dict = V1MailboxesEmailPatchRequest.from_dict(v1_mailboxes_email_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


