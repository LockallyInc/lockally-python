# GetSecurity200ResponseStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**value** | **int** |  | [optional] 
**trend** | **str** |  | [optional] 

## Example

```python
from lockally.models.get_security200_response_stats_inner import GetSecurity200ResponseStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSecurity200ResponseStatsInner from a JSON string
get_security200_response_stats_inner_instance = GetSecurity200ResponseStatsInner.from_json(json)
# print the JSON string representation of the object
print(GetSecurity200ResponseStatsInner.to_json())

# convert the object into a dict
get_security200_response_stats_inner_dict = get_security200_response_stats_inner_instance.to_dict()
# create an instance of GetSecurity200ResponseStatsInner from a dict
get_security200_response_stats_inner_from_dict = GetSecurity200ResponseStatsInner.from_dict(get_security200_response_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


