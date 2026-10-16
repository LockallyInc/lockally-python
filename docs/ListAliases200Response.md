# ListAliases200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Alias]**](Alias.md) |  | 

## Example

```python
from lockally.models.list_aliases200_response import ListAliases200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAliases200Response from a JSON string
list_aliases200_response_instance = ListAliases200Response.from_json(json)
# print the JSON string representation of the object
print(ListAliases200Response.to_json())

# convert the object into a dict
list_aliases200_response_dict = list_aliases200_response_instance.to_dict()
# create an instance of ListAliases200Response from a dict
list_aliases200_response_from_dict = ListAliases200Response.from_dict(list_aliases200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


