# GetIntegrationsSummary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_requests_today** | **int** |  | [optional] 
**active_api_keys** | **int** |  | [optional] 
**api_keys** | [**List[GetIntegrationsSummary200ResponseApiKeysInner]**](GetIntegrationsSummary200ResponseApiKeysInner.md) |  | [optional] 
**webhook_failures** | **int** |  | [optional] 
**webhooks_total** | **int** |  | [optional] 
**webhooks** | [**List[GetIntegrationsSummary200ResponseWebhooksInner]**](GetIntegrationsSummary200ResponseWebhooksInner.md) |  | [optional] 
**generated_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_integrations_summary200_response import GetIntegrationsSummary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIntegrationsSummary200Response from a JSON string
get_integrations_summary200_response_instance = GetIntegrationsSummary200Response.from_json(json)
# print the JSON string representation of the object
print(GetIntegrationsSummary200Response.to_json())

# convert the object into a dict
get_integrations_summary200_response_dict = get_integrations_summary200_response_instance.to_dict()
# create an instance of GetIntegrationsSummary200Response from a dict
get_integrations_summary200_response_from_dict = GetIntegrationsSummary200Response.from_dict(get_integrations_summary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


