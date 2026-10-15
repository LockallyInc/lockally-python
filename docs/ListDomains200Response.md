# ListDomains200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Domain]**](Domain.md) |  | 

## Example

```python
from lockally.models.list_domains200_response import ListDomains200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDomains200Response from a JSON string
list_domains200_response_instance = ListDomains200Response.from_json(json)
# print the JSON string representation of the object
print(ListDomains200Response.to_json())

# convert the object into a dict
list_domains200_response_dict = list_domains200_response_instance.to_dict()
# create an instance of ListDomains200Response from a dict
list_domains200_response_from_dict = ListDomains200Response.from_dict(list_domains200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


