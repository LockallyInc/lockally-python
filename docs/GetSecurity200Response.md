# GetSecurity200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_status** | **str** |  | [optional] 
**stats** | [**List[GetSecurity200ResponseStatsInner]**](GetSecurity200ResponseStatsInner.md) |  | [optional] 
**alerts** | [**List[GetSecurity200ResponseAlertsInner]**](GetSecurity200ResponseAlertsInner.md) |  | [optional] 

## Example

```python
from lockally.models.get_security200_response import GetSecurity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSecurity200Response from a JSON string
get_security200_response_instance = GetSecurity200Response.from_json(json)
# print the JSON string representation of the object
print(GetSecurity200Response.to_json())

# convert the object into a dict
get_security200_response_dict = get_security200_response_instance.to_dict()
# create an instance of GetSecurity200Response from a dict
get_security200_response_from_dict = GetSecurity200Response.from_dict(get_security200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


