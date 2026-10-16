# CreateUnitsCheckout200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** |  | 
**reference** | **str** |  | 
**units** | **int** |  | 

## Example

```python
from lockally.models.create_units_checkout200_response import CreateUnitsCheckout200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUnitsCheckout200Response from a JSON string
create_units_checkout200_response_instance = CreateUnitsCheckout200Response.from_json(json)
# print the JSON string representation of the object
print(CreateUnitsCheckout200Response.to_json())

# convert the object into a dict
create_units_checkout200_response_dict = create_units_checkout200_response_instance.to_dict()
# create an instance of CreateUnitsCheckout200Response from a dict
create_units_checkout200_response_from_dict = CreateUnitsCheckout200Response.from_dict(create_units_checkout200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


