# GetEncryptionStatus200ResponseMailboxesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**has_key** | **bool** |  | [optional] 
**key_created_at** | **datetime** |  | [optional] 
**has_recovery** | **bool** |  | [optional] 
**recovery_set_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_encryption_status200_response_mailboxes_inner import GetEncryptionStatus200ResponseMailboxesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncryptionStatus200ResponseMailboxesInner from a JSON string
get_encryption_status200_response_mailboxes_inner_instance = GetEncryptionStatus200ResponseMailboxesInner.from_json(json)
# print the JSON string representation of the object
print(GetEncryptionStatus200ResponseMailboxesInner.to_json())

# convert the object into a dict
get_encryption_status200_response_mailboxes_inner_dict = get_encryption_status200_response_mailboxes_inner_instance.to_dict()
# create an instance of GetEncryptionStatus200ResponseMailboxesInner from a dict
get_encryption_status200_response_mailboxes_inner_from_dict = GetEncryptionStatus200ResponseMailboxesInner.from_dict(get_encryption_status200_response_mailboxes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


