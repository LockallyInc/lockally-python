# V1MailboxesEmailExportPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Relative download URL. Caller appends to the API host. | 
**expires_at** | **datetime** |  | 
**format** | **str** |  | 

## Example

```python
from lockally.models.v1_mailboxes_email_export_post201_response import V1MailboxesEmailExportPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1MailboxesEmailExportPost201Response from a JSON string
v1_mailboxes_email_export_post201_response_instance = V1MailboxesEmailExportPost201Response.from_json(json)
# print the JSON string representation of the object
print(V1MailboxesEmailExportPost201Response.to_json())

# convert the object into a dict
v1_mailboxes_email_export_post201_response_dict = v1_mailboxes_email_export_post201_response_instance.to_dict()
# create an instance of V1MailboxesEmailExportPost201Response from a dict
v1_mailboxes_email_export_post201_response_from_dict = V1MailboxesEmailExportPost201Response.from_dict(v1_mailboxes_email_export_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


