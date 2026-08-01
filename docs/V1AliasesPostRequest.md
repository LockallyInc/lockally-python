# V1AliasesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias_address** | **str** |  | 
**alias_target** | **str** |  | 

## Example

```python
from lockally.models.v1_aliases_post_request import V1AliasesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AliasesPostRequest from a JSON string
v1_aliases_post_request_instance = V1AliasesPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AliasesPostRequest.to_json())

# convert the object into a dict
v1_aliases_post_request_dict = v1_aliases_post_request_instance.to_dict()
# create an instance of V1AliasesPostRequest from a dict
v1_aliases_post_request_from_dict = V1AliasesPostRequest.from_dict(v1_aliases_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


