# GetCurrentAdmin200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | [**Admin**](Admin.md) |  | 
**tenant** | [**Tenant**](Tenant.md) |  | 

## Example

```python
from lockally.models.get_current_admin200_response import GetCurrentAdmin200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrentAdmin200Response from a JSON string
get_current_admin200_response_instance = GetCurrentAdmin200Response.from_json(json)
# print the JSON string representation of the object
print(GetCurrentAdmin200Response.to_json())

# convert the object into a dict
get_current_admin200_response_dict = get_current_admin200_response_instance.to_dict()
# create an instance of GetCurrentAdmin200Response from a dict
get_current_admin200_response_from_dict = GetCurrentAdmin200Response.from_dict(get_current_admin200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


