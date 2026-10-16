# GetIntegrationsSummary200ResponseWebhooksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**paused** | **bool** |  | [optional] 
**consecutive_failures** | **int** |  | [optional] 
**last_failure_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_integrations_summary200_response_webhooks_inner import GetIntegrationsSummary200ResponseWebhooksInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIntegrationsSummary200ResponseWebhooksInner from a JSON string
get_integrations_summary200_response_webhooks_inner_instance = GetIntegrationsSummary200ResponseWebhooksInner.from_json(json)
# print the JSON string representation of the object
print(GetIntegrationsSummary200ResponseWebhooksInner.to_json())

# convert the object into a dict
get_integrations_summary200_response_webhooks_inner_dict = get_integrations_summary200_response_webhooks_inner_instance.to_dict()
# create an instance of GetIntegrationsSummary200ResponseWebhooksInner from a dict
get_integrations_summary200_response_webhooks_inner_from_dict = GetIntegrationsSummary200ResponseWebhooksInner.from_dict(get_integrations_summary200_response_webhooks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


