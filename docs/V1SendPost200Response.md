# V1SendPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Present on a test-mode send; absent when suppressed. | [optional] 
**message_id** | **str** | RFC 5322 Message-ID. On a test send the domain is test.lockally.com. Absent when suppressed. | [optional] 
**status** | **str** |  | 
**warning** | **str** | On a suppressed send, explains that nothing was sent. | [optional] 

## Example

```python
from lockally.models.v1_send_post200_response import V1SendPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1SendPost200Response from a JSON string
v1_send_post200_response_instance = V1SendPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1SendPost200Response.to_json())

# convert the object into a dict
v1_send_post200_response_dict = v1_send_post200_response_instance.to_dict()
# create an instance of V1SendPost200Response from a dict
v1_send_post200_response_from_dict = V1SendPost200Response.from_dict(v1_send_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


