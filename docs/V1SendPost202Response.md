# V1SendPost202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Lockally identifier; use with GET /v1/messages/{id}. | 
**message_id** | **str** | RFC 5322 Message-ID (with angle brackets). | 
**status** | **str** | \&quot;scheduled\&quot; when send_at is in the future. | 
**warning** | **str** |  | [optional] 

## Example

```python
from lockally.models.v1_send_post202_response import V1SendPost202Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1SendPost202Response from a JSON string
v1_send_post202_response_instance = V1SendPost202Response.from_json(json)
# print the JSON string representation of the object
print(V1SendPost202Response.to_json())

# convert the object into a dict
v1_send_post202_response_dict = v1_send_post202_response_instance.to_dict()
# create an instance of V1SendPost202Response from a dict
v1_send_post202_response_from_dict = V1SendPost202Response.from_dict(v1_send_post202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


