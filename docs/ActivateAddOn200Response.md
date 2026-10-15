# ActivateAddOn200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**add_on** | **str** |  | 
**status** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from lockally.models.activate_add_on200_response import ActivateAddOn200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateAddOn200Response from a JSON string
activate_add_on200_response_instance = ActivateAddOn200Response.from_json(json)
# print the JSON string representation of the object
print(ActivateAddOn200Response.to_json())

# convert the object into a dict
activate_add_on200_response_dict = activate_add_on200_response_instance.to_dict()
# create an instance of ActivateAddOn200Response from a dict
activate_add_on200_response_from_dict = ActivateAddOn200Response.from_dict(activate_add_on200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


