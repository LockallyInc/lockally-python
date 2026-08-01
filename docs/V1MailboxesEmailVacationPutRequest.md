# V1MailboxesEmailVacationPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**params** | [**VacationParams**](VacationParams.md) |  | 

## Example

```python
from lockally.models.v1_mailboxes_email_vacation_put_request import V1MailboxesEmailVacationPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1MailboxesEmailVacationPutRequest from a JSON string
v1_mailboxes_email_vacation_put_request_instance = V1MailboxesEmailVacationPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1MailboxesEmailVacationPutRequest.to_json())

# convert the object into a dict
v1_mailboxes_email_vacation_put_request_dict = v1_mailboxes_email_vacation_put_request_instance.to_dict()
# create an instance of V1MailboxesEmailVacationPutRequest from a dict
v1_mailboxes_email_vacation_put_request_from_dict = V1MailboxesEmailVacationPutRequest.from_dict(v1_mailboxes_email_vacation_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


