# VacationResponder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox_email** | **str** |  | 
**enabled** | **bool** |  | 
**params** | [**VacationParams**](VacationParams.md) |  | 
**script** | **str** | Pre-rendered Sieve script (RFC 5230). | 
**synced_at** | **datetime** | Null &#x3D; stored on lockally but not yet pushed to the mail server. | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from lockally.models.vacation_responder import VacationResponder

# TODO update the JSON string below
json = "{}"
# create an instance of VacationResponder from a JSON string
vacation_responder_instance = VacationResponder.from_json(json)
# print the JSON string representation of the object
print(VacationResponder.to_json())

# convert the object into a dict
vacation_responder_dict = vacation_responder_instance.to_dict()
# create an instance of VacationResponder from a dict
vacation_responder_from_dict = VacationResponder.from_dict(vacation_responder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


