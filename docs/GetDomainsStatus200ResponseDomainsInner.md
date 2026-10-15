# GetDomainsStatus200ResponseDomainsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**checks** | [**List[GetDomainsStatus200ResponseDomainsInnerChecksInner]**](GetDomainsStatus200ResponseDomainsInnerChecksInner.md) |  | [optional] 

## Example

```python
from lockally.models.get_domains_status200_response_domains_inner import GetDomainsStatus200ResponseDomainsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainsStatus200ResponseDomainsInner from a JSON string
get_domains_status200_response_domains_inner_instance = GetDomainsStatus200ResponseDomainsInner.from_json(json)
# print the JSON string representation of the object
print(GetDomainsStatus200ResponseDomainsInner.to_json())

# convert the object into a dict
get_domains_status200_response_domains_inner_dict = get_domains_status200_response_domains_inner_instance.to_dict()
# create an instance of GetDomainsStatus200ResponseDomainsInner from a dict
get_domains_status200_response_domains_inner_from_dict = GetDomainsStatus200ResponseDomainsInner.from_dict(get_domains_status200_response_domains_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


