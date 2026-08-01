# GetUserInsights200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recently_added** | [**List[UserEvent]**](UserEvent.md) |  | [optional] 
**recently_suspended** | [**List[UserEvent]**](UserEvent.md) |  | [optional] 
**inactive_30d** | [**List[UserEvent]**](UserEvent.md) |  | [optional] 
**seats_used** | **int** |  | [optional] 
**seats_alloc** | **int** |  | [optional] 
**generated_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_user_insights200_response import GetUserInsights200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserInsights200Response from a JSON string
get_user_insights200_response_instance = GetUserInsights200Response.from_json(json)
# print the JSON string representation of the object
print(GetUserInsights200Response.to_json())

# convert the object into a dict
get_user_insights200_response_dict = get_user_insights200_response_instance.to_dict()
# create an instance of GetUserInsights200Response from a dict
get_user_insights200_response_from_dict = GetUserInsights200Response.from_dict(get_user_insights200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


