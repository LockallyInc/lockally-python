# GetDirectoryActivity200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetDirectoryActivity200ResponseDataInner]**](GetDirectoryActivity200ResponseDataInner.md) |  | [optional] 

## Example

```python
from lockally.models.get_directory_activity200_response import GetDirectoryActivity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDirectoryActivity200Response from a JSON string
get_directory_activity200_response_instance = GetDirectoryActivity200Response.from_json(json)
# print the JSON string representation of the object
print(GetDirectoryActivity200Response.to_json())

# convert the object into a dict
get_directory_activity200_response_dict = get_directory_activity200_response_instance.to_dict()
# create an instance of GetDirectoryActivity200Response from a dict
get_directory_activity200_response_from_dict = GetDirectoryActivity200Response.from_dict(get_directory_activity200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


