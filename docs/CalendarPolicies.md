# CalendarPolicies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **UUID** |  | 
**max_meeting_duration_mins** | **int** |  | [optional] 
**working_hours_start** | **str** |  | [optional] 
**working_hours_end** | **str** |  | [optional] 
**booking_window_days** | **int** |  | [optional] 
**recurring_meeting_limit** | **int** |  | [optional] 
**resource_approval_mode** | **str** |  | [optional] 
**external_invites_allowed** | **bool** |  | [optional] 
**external_sharing_allowed** | **bool** |  | [optional] 
**public_links_enabled** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.calendar_policies import CalendarPolicies

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarPolicies from a JSON string
calendar_policies_instance = CalendarPolicies.from_json(json)
# print the JSON string representation of the object
print(CalendarPolicies.to_json())

# convert the object into a dict
calendar_policies_dict = calendar_policies_instance.to_dict()
# create an instance of CalendarPolicies from a dict
calendar_policies_from_dict = CalendarPolicies.from_dict(calendar_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


