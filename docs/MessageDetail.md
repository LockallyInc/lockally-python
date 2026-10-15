# MessageDetail

A single message with the content captured at send time. Returned only by GET /v1/messages/{id} (the list stays summary-only). Attachments are not returned. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**message_id** | **str** | RFC 5322 Message-ID header, including angle brackets. | 
**sender** | **str** |  | 
**recipients** | **List[str]** |  | 
**subject** | **str** |  | [optional] 
**status** | **str** |  | 
**queued_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**bounce_reason** | **str** |  | [optional] 
**size_bytes** | **int** |  | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **List[str]** |  | [optional] 
**cc** | **List[str]** |  | [optional] 
**bcc** | **List[str]** |  | [optional] 
**text** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 

## Example

```python
from lockally.models.message_detail import MessageDetail

# TODO update the JSON string below
json = "{}"
# create an instance of MessageDetail from a JSON string
message_detail_instance = MessageDetail.from_json(json)
# print the JSON string representation of the object
print(MessageDetail.to_json())

# convert the object into a dict
message_detail_dict = message_detail_instance.to_dict()
# create an instance of MessageDetail from a dict
message_detail_from_dict = MessageDetail.from_dict(message_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


