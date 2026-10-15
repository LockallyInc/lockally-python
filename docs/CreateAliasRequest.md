# CreateAliasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias_address** | **str** |  | 
**alias_target** | **str** |  | 

## Example

```python
from lockally.models.create_alias_request import CreateAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAliasRequest from a JSON string
create_alias_request_instance = CreateAliasRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAliasRequest.to_json())

# convert the object into a dict
create_alias_request_dict = create_alias_request_instance.to_dict()
# create an instance of CreateAliasRequest from a dict
create_alias_request_from_dict = CreateAliasRequest.from_dict(create_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


