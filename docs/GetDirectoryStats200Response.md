# GetDirectoryStats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_contacts** | **int** |  | [optional] 
**internal_users** | **int** |  | [optional] 
**external_contacts** | **int** |  | [optional] 
**synced_contacts** | **int** |  | [optional] 
**shared_lists** | **int** |  | [optional] 
**directory_groups** | **int** |  | [optional] 

## Example

```python
from lockally.models.get_directory_stats200_response import GetDirectoryStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDirectoryStats200Response from a JSON string
get_directory_stats200_response_instance = GetDirectoryStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetDirectoryStats200Response.to_json())

# convert the object into a dict
get_directory_stats200_response_dict = get_directory_stats200_response_instance.to_dict()
# create an instance of GetDirectoryStats200Response from a dict
get_directory_stats200_response_from_dict = GetDirectoryStats200Response.from_dict(get_directory_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


