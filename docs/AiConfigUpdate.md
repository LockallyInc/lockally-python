# AiConfigUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**model** | **str** |  | 

## Example

```python
from lockally.models.ai_config_update import AiConfigUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AiConfigUpdate from a JSON string
ai_config_update_instance = AiConfigUpdate.from_json(json)
# print the JSON string representation of the object
print(AiConfigUpdate.to_json())

# convert the object into a dict
ai_config_update_dict = ai_config_update_instance.to_dict()
# create an instance of AiConfigUpdate from a dict
ai_config_update_from_dict = AiConfigUpdate.from_dict(ai_config_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


