# V1WebhooksIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**paused** | **bool** |  | [optional] 

## Example

```python
from lockally.models.v1_webhooks_id_patch_request import V1WebhooksIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1WebhooksIdPatchRequest from a JSON string
v1_webhooks_id_patch_request_instance = V1WebhooksIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1WebhooksIdPatchRequest.to_json())

# convert the object into a dict
v1_webhooks_id_patch_request_dict = v1_webhooks_id_patch_request_instance.to_dict()
# create an instance of V1WebhooksIdPatchRequest from a dict
v1_webhooks_id_patch_request_from_dict = V1WebhooksIdPatchRequest.from_dict(v1_webhooks_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


