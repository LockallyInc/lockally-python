# AiConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**model** | **str** |  | 
**byok_key_hint** | **str** |  | [optional] 
**units_balance** | **int** |  | [optional] 
**units_available** | **bool** | True when a platform model key is configured. | [optional] 

## Example

```python
from lockally.models.ai_config import AiConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AiConfig from a JSON string
ai_config_instance = AiConfig.from_json(json)
# print the JSON string representation of the object
print(AiConfig.to_json())

# convert the object into a dict
ai_config_dict = ai_config_instance.to_dict()
# create an instance of AiConfig from a dict
ai_config_from_dict = AiConfig.from_dict(ai_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


