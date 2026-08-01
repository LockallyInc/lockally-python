# V1WebhooksPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | HTTPS recommended (HTTP allowed for local development). | 
**events** | **List[str]** |  | 

## Example

```python
from lockally.models.v1_webhooks_post_request import V1WebhooksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1WebhooksPostRequest from a JSON string
v1_webhooks_post_request_instance = V1WebhooksPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1WebhooksPostRequest.to_json())

# convert the object into a dict
v1_webhooks_post_request_dict = v1_webhooks_post_request_instance.to_dict()
# create an instance of V1WebhooksPostRequest from a dict
v1_webhooks_post_request_from_dict = V1WebhooksPostRequest.from_dict(v1_webhooks_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


