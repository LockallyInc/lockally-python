# AddOn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**price_naira** | **int** |  | 
**pricing_model** | **str** |  | 
**active** | **bool** |  | 

## Example

```python
from lockally.models.add_on import AddOn

# TODO update the JSON string below
json = "{}"
# create an instance of AddOn from a JSON string
add_on_instance = AddOn.from_json(json)
# print the JSON string representation of the object
print(AddOn.to_json())

# convert the object into a dict
add_on_dict = add_on_instance.to_dict()
# create an instance of AddOn from a dict
add_on_from_dict = AddOn.from_dict(add_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


