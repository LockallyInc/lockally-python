# SetVacationResponderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**params** | [**VacationParams**](VacationParams.md) |  | 

## Example

```python
from lockally.models.set_vacation_responder_request import SetVacationResponderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetVacationResponderRequest from a JSON string
set_vacation_responder_request_instance = SetVacationResponderRequest.from_json(json)
# print the JSON string representation of the object
print(SetVacationResponderRequest.to_json())

# convert the object into a dict
set_vacation_responder_request_dict = set_vacation_responder_request_instance.to_dict()
# create an instance of SetVacationResponderRequest from a dict
set_vacation_responder_request_from_dict = SetVacationResponderRequest.from_dict(set_vacation_responder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


