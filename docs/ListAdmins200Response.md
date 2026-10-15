# ListAdmins200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminFull]**](AdminFull.md) |  | 

## Example

```python
from lockally.models.list_admins200_response import ListAdmins200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAdmins200Response from a JSON string
list_admins200_response_instance = ListAdmins200Response.from_json(json)
# print the JSON string representation of the object
print(ListAdmins200Response.to_json())

# convert the object into a dict
list_admins200_response_dict = list_admins200_response_instance.to_dict()
# create an instance of ListAdmins200Response from a dict
list_admins200_response_from_dict = ListAdmins200Response.from_dict(list_admins200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


