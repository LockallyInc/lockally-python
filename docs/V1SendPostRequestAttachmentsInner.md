# V1SendPostRequestAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**content_type** | **str** |  | 
**content_base64** | **str** | Base64-encoded body, max 10 MB decoded per attachment. | 

## Example

```python
from lockally.models.v1_send_post_request_attachments_inner import V1SendPostRequestAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1SendPostRequestAttachmentsInner from a JSON string
v1_send_post_request_attachments_inner_instance = V1SendPostRequestAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(V1SendPostRequestAttachmentsInner.to_json())

# convert the object into a dict
v1_send_post_request_attachments_inner_dict = v1_send_post_request_attachments_inner_instance.to_dict()
# create an instance of V1SendPostRequestAttachmentsInner from a dict
v1_send_post_request_attachments_inner_from_dict = V1SendPostRequestAttachmentsInner.from_dict(v1_send_post_request_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


