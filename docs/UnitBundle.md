# UnitBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**units** | **int** |  | 
**display_name** | **str** |  | 
**price_naira** | **int** |  | 
**display_price** | **str** |  | 

## Example

```python
from lockally.models.unit_bundle import UnitBundle

# TODO update the JSON string below
json = "{}"
# create an instance of UnitBundle from a JSON string
unit_bundle_instance = UnitBundle.from_json(json)
# print the JSON string representation of the object
print(UnitBundle.to_json())

# convert the object into a dict
unit_bundle_dict = unit_bundle_instance.to_dict()
# create an instance of UnitBundle from a dict
unit_bundle_from_dict = UnitBundle.from_dict(unit_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


