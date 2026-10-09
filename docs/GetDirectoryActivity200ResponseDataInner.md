# GetDirectoryActivity200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_directory_activity200_response_data_inner import GetDirectoryActivity200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDirectoryActivity200ResponseDataInner from a JSON string
get_directory_activity200_response_data_inner_instance = GetDirectoryActivity200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetDirectoryActivity200ResponseDataInner.to_json())

# convert the object into a dict
get_directory_activity200_response_data_inner_dict = get_directory_activity200_response_data_inner_instance.to_dict()
# create an instance of GetDirectoryActivity200ResponseDataInner from a dict
get_directory_activity200_response_data_inner_from_dict = GetDirectoryActivity200ResponseDataInner.from_dict(get_directory_activity200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


