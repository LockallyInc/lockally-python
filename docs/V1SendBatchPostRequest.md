# V1SendBatchPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[SendMessage]**](SendMessage.md) |  | 

## Example

```python
from lockally.models.v1_send_batch_post_request import V1SendBatchPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SendBatchPostRequest from a JSON string
v1_send_batch_post_request_instance = V1SendBatchPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1SendBatchPostRequest.to_json())

# convert the object into a dict
v1_send_batch_post_request_dict = v1_send_batch_post_request_instance.to_dict()
# create an instance of V1SendBatchPostRequest from a dict
v1_send_batch_post_request_from_dict = V1SendBatchPostRequest.from_dict(v1_send_batch_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


