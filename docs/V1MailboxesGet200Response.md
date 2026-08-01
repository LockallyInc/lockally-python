# V1MailboxesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Mailbox]**](Mailbox.md) |  | 
**limit** | **int** |  | 

## Example

```python
from lockally.models.v1_mailboxes_get200_response import V1MailboxesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1MailboxesGet200Response from a JSON string
v1_mailboxes_get200_response_instance = V1MailboxesGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1MailboxesGet200Response.to_json())

# convert the object into a dict
v1_mailboxes_get200_response_dict = v1_mailboxes_get200_response_instance.to_dict()
# create an instance of V1MailboxesGet200Response from a dict
v1_mailboxes_get200_response_from_dict = V1MailboxesGet200Response.from_dict(v1_mailboxes_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


