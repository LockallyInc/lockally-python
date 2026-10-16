# GetDomainsStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[GetDomainsStatus200ResponseDomainsInner]**](GetDomainsStatus200ResponseDomainsInner.md) |  | [optional] 
**generated_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_domains_status200_response import GetDomainsStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainsStatus200Response from a JSON string
get_domains_status200_response_instance = GetDomainsStatus200Response.from_json(json)
# print the JSON string representation of the object
print(GetDomainsStatus200Response.to_json())

# convert the object into a dict
get_domains_status200_response_dict = get_domains_status200_response_instance.to_dict()
# create an instance of GetDomainsStatus200Response from a dict
get_domains_status200_response_from_dict = GetDomainsStatus200Response.from_dict(get_domains_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


