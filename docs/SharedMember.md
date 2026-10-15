# SharedMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**mailbox_id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**member_email** | **str** |  | 
**role** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from lockally.models.shared_member import SharedMember

# TODO update the JSON string below
json = "{}"
# create an instance of SharedMember from a JSON string
shared_member_instance = SharedMember.from_json(json)
# print the JSON string representation of the object
print(SharedMember.to_json())

# convert the object into a dict
shared_member_dict = shared_member_instance.to_dict()
# create an instance of SharedMember from a dict
shared_member_from_dict = SharedMember.from_dict(shared_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


