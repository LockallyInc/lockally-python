# InjectionRisk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flagged** | **bool** |  | [optional] 
**signals** | **List[str]** | The phrases that tripped the check. | [optional] 

## Example

```python
from lockally.models.injection_risk import InjectionRisk

# TODO update the JSON string below
json = "{}"
# create an instance of InjectionRisk from a JSON string
injection_risk_instance = InjectionRisk.from_json(json)
# print the JSON string representation of the object
print(InjectionRisk.to_json())

# convert the object into a dict
injection_risk_dict = injection_risk_instance.to_dict()
# create an instance of InjectionRisk from a dict
injection_risk_from_dict = InjectionRisk.from_dict(injection_risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


