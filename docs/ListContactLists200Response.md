# ListContactLists200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ContactList]**](ContactList.md) |  | [optional] 

## Example

```python
from lockally.models.list_contact_lists200_response import ListContactLists200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListContactLists200Response from a JSON string
list_contact_lists200_response_instance = ListContactLists200Response.from_json(json)
# print the JSON string representation of the object
print(ListContactLists200Response.to_json())

# convert the object into a dict
list_contact_lists200_response_dict = list_contact_lists200_response_instance.to_dict()
# create an instance of ListContactLists200Response from a dict
list_contact_lists200_response_from_dict = ListContactLists200Response.from_dict(list_contact_lists200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


