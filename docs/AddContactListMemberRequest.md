# AddContactListMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **UUID** |  | 

## Example

```python
from lockally.models.add_contact_list_member_request import AddContactListMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddContactListMemberRequest from a JSON string
add_contact_list_member_request_instance = AddContactListMemberRequest.from_json(json)
# print the JSON string representation of the object
print(AddContactListMemberRequest.to_json())

# convert the object into a dict
add_contact_list_member_request_dict = add_contact_list_member_request_instance.to_dict()
# create an instance of AddContactListMemberRequest from a dict
add_contact_list_member_request_from_dict = AddContactListMemberRequest.from_dict(add_contact_list_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


