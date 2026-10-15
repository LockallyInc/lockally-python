# GetContactList200ResponseMembersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from lockally.models.get_contact_list200_response_members_inner import GetContactList200ResponseMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetContactList200ResponseMembersInner from a JSON string
get_contact_list200_response_members_inner_instance = GetContactList200ResponseMembersInner.from_json(json)
# print the JSON string representation of the object
print(GetContactList200ResponseMembersInner.to_json())

# convert the object into a dict
get_contact_list200_response_members_inner_dict = get_contact_list200_response_members_inner_instance.to_dict()
# create an instance of GetContactList200ResponseMembersInner from a dict
get_contact_list200_response_members_inner_from_dict = GetContactList200ResponseMembersInner.from_dict(get_contact_list200_response_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


