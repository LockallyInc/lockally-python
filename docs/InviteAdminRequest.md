# InviteAdminRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**role** | **str** |  | [optional] [default to 'admin']

## Example

```python
from lockally.models.invite_admin_request import InviteAdminRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InviteAdminRequest from a JSON string
invite_admin_request_instance = InviteAdminRequest.from_json(json)
# print the JSON string representation of the object
print(InviteAdminRequest.to_json())

# convert the object into a dict
invite_admin_request_dict = invite_admin_request_instance.to_dict()
# create an instance of InviteAdminRequest from a dict
invite_admin_request_from_dict = InviteAdminRequest.from_dict(invite_admin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


