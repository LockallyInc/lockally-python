# GetIPAssignment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_name** | **str** |  | [optional] 
**pool_kind** | **str** |  | [optional] 
**dedicated_ip** | **str** |  | [optional] 
**assigned_at** | **datetime** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from lockally.models.get_ip_assignment200_response import GetIPAssignment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIPAssignment200Response from a JSON string
get_ip_assignment200_response_instance = GetIPAssignment200Response.from_json(json)
# print the JSON string representation of the object
print(GetIPAssignment200Response.to_json())

# convert the object into a dict
get_ip_assignment200_response_dict = get_ip_assignment200_response_instance.to_dict()
# create an instance of GetIPAssignment200Response from a dict
get_ip_assignment200_response_from_dict = GetIPAssignment200Response.from_dict(get_ip_assignment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


