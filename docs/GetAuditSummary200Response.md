# GetAuditSummary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_actions_today** | **int** |  | [optional] 
**recent_logins** | [**List[AuditEvent]**](AuditEvent.md) |  | [optional] 
**recent_exports** | [**List[AuditEvent]**](AuditEvent.md) |  | [optional] 
**deleted_mailboxes** | [**List[AuditEvent]**](AuditEvent.md) |  | [optional] 
**generated_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_audit_summary200_response import GetAuditSummary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuditSummary200Response from a JSON string
get_audit_summary200_response_instance = GetAuditSummary200Response.from_json(json)
# print the JSON string representation of the object
print(GetAuditSummary200Response.to_json())

# convert the object into a dict
get_audit_summary200_response_dict = get_audit_summary200_response_instance.to_dict()
# create an instance of GetAuditSummary200Response from a dict
get_audit_summary200_response_from_dict = GetAuditSummary200Response.from_dict(get_audit_summary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


