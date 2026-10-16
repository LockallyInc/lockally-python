# Annotations

Signals computed at ingest, before an agent sees the message. A key is absent when its check did not fire. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_types** | **List[str]** |  | [optional] 
**meeting_request** | **bool** |  | [optional] 
**injection_risk** | [**InjectionRisk**](InjectionRisk.md) |  | [optional] 

## Example

```python
from lockally.models.annotations import Annotations

# TODO update the JSON string below
json = "{}"
# create an instance of Annotations from a JSON string
annotations_instance = Annotations.from_json(json)
# print the JSON string representation of the object
print(Annotations.to_json())

# convert the object into a dict
annotations_dict = annotations_instance.to_dict()
# create an instance of Annotations from a dict
annotations_from_dict = Annotations.from_dict(annotations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


