# ListDedicatedIPRequests200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DedicatedIPRequest]**](DedicatedIPRequest.md) |  | 

## Example

```python
from lockally.models.list_dedicated_ip_requests200_response import ListDedicatedIPRequests200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDedicatedIPRequests200Response from a JSON string
list_dedicated_ip_requests200_response_instance = ListDedicatedIPRequests200Response.from_json(json)
# print the JSON string representation of the object
print(ListDedicatedIPRequests200Response.to_json())

# convert the object into a dict
list_dedicated_ip_requests200_response_dict = list_dedicated_ip_requests200_response_instance.to_dict()
# create an instance of ListDedicatedIPRequests200Response from a dict
list_dedicated_ip_requests200_response_from_dict = ListDedicatedIPRequests200Response.from_dict(list_dedicated_ip_requests200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


