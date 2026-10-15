# MailboxGrant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **UUID** |  | [optional] 
**mailbox_id** | **UUID** |  | [optional] 
**mailbox** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.mailbox_grant import MailboxGrant

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxGrant from a JSON string
mailbox_grant_instance = MailboxGrant.from_json(json)
# print the JSON string representation of the object
print(MailboxGrant.to_json())

# convert the object into a dict
mailbox_grant_dict = mailbox_grant_instance.to_dict()
# create an instance of MailboxGrant from a dict
mailbox_grant_from_dict = MailboxGrant.from_dict(mailbox_grant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


