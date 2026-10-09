# GetContactLists200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetContactLists200ResponseDataInner]**](GetContactLists200ResponseDataInner.md) |  | [optional] 

## Example

```python
from lockally.models.get_contact_lists200_response import GetContactLists200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetContactLists200Response from a JSON string
get_contact_lists200_response_instance = GetContactLists200Response.from_json(json)
# print the JSON string representation of the object
print(GetContactLists200Response.to_json())

# convert the object into a dict
get_contact_lists200_response_dict = get_contact_lists200_response_instance.to_dict()
# create an instance of GetContactLists200Response from a dict
get_contact_lists200_response_from_dict = GetContactLists200Response.from_dict(get_contact_lists200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


