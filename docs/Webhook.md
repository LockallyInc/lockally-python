# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**url** | **str** |  | 
**events** | **List[str]** |  | 
**paused** | **bool** |  | 
**paused_at** | **datetime** |  | [optional] 
**last_success_at** | **datetime** |  | [optional] 
**last_failure_at** | **datetime** |  | [optional] 
**consecutive_failures** | **int** |  | 
**created_at** | **datetime** |  | 
**signing_secret** | **str** | Hex-encoded HMAC-SHA256 key. Present ONLY on POST response. | [optional] 

## Example

```python
from lockally.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


