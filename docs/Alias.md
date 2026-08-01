# Alias


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**alias_address** | **str** |  | 
**alias_target** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from lockally.models.alias import Alias

# TODO update the JSON string below
json = "{}"
# create an instance of Alias from a JSON string
alias_instance = Alias.from_json(json)
# print the JSON string representation of the object
print(Alias.to_json())

# convert the object into a dict
alias_dict = alias_instance.to_dict()
# create an instance of Alias from a dict
alias_from_dict = Alias.from_dict(alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


