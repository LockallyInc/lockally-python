# GetAddOnStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**eligible** | **bool** |  | 
**active** | **bool** |  | 

## Example

```python
from lockally.models.get_add_on_status200_response import GetAddOnStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAddOnStatus200Response from a JSON string
get_add_on_status200_response_instance = GetAddOnStatus200Response.from_json(json)
# print the JSON string representation of the object
print(GetAddOnStatus200Response.to_json())

# convert the object into a dict
get_add_on_status200_response_dict = get_add_on_status200_response_instance.to_dict()
# create an instance of GetAddOnStatus200Response from a dict
get_add_on_status200_response_from_dict = GetAddOnStatus200Response.from_dict(get_add_on_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


