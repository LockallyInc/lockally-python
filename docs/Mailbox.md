# Mailbox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**domain_id** | **UUID** |  | 
**email** | **str** |  | 
**quota_bytes** | **int** |  | 
**disabled** | **bool** |  | 
**disabled_at** | **datetime** |  | [optional] 
**soft_deleted_at** | **datetime** |  | [optional] 
**hard_delete_after** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**password** | **str** | ONLY present on POST response when lockally generated the password. Shown once. | [optional] 

## Example

```python
from lockally.models.mailbox import Mailbox

# TODO update the JSON string below
json = "{}"
# create an instance of Mailbox from a JSON string
mailbox_instance = Mailbox.from_json(json)
# print the JSON string representation of the object
print(Mailbox.to_json())

# convert the object into a dict
mailbox_dict = mailbox_instance.to_dict()
# create an instance of Mailbox from a dict
mailbox_from_dict = Mailbox.from_dict(mailbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


