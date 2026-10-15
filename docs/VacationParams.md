# VacationParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** |  | 
**body** | **str** |  | 
**starts_at** | **datetime** |  | [optional] 
**ends_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.vacation_params import VacationParams

# TODO update the JSON string below
json = "{}"
# create an instance of VacationParams from a JSON string
vacation_params_instance = VacationParams.from_json(json)
# print the JSON string representation of the object
print(VacationParams.to_json())

# convert the object into a dict
vacation_params_dict = vacation_params_instance.to_dict()
# create an instance of VacationParams from a dict
vacation_params_from_dict = VacationParams.from_dict(vacation_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


