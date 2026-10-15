# MailboxGrantList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grants** | [**List[MailboxGrant]**](MailboxGrant.md) |  | 

## Example

```python
from lockally.models.mailbox_grant_list import MailboxGrantList

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxGrantList from a JSON string
mailbox_grant_list_instance = MailboxGrantList.from_json(json)
# print the JSON string representation of the object
print(MailboxGrantList.to_json())

# convert the object into a dict
mailbox_grant_list_dict = mailbox_grant_list_instance.to_dict()
# create an instance of MailboxGrantList from a dict
mailbox_grant_list_from_dict = MailboxGrantList.from_dict(mailbox_grant_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


