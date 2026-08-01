# GetContactList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**ContactList**](ContactList.md) |  | [optional] 
**members** | [**List[GetContactList200ResponseMembersInner]**](GetContactList200ResponseMembersInner.md) |  | [optional] 

## Example

```python
from lockally.models.get_contact_list200_response import GetContactList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetContactList200Response from a JSON string
get_contact_list200_response_instance = GetContactList200Response.from_json(json)
# print the JSON string representation of the object
print(GetContactList200Response.to_json())

# convert the object into a dict
get_contact_list200_response_dict = get_contact_list200_response_instance.to_dict()
# create an instance of GetContactList200Response from a dict
get_contact_list200_response_from_dict = GetContactList200Response.from_dict(get_contact_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


