# ExternalContactInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** | Defaults to the email address when empty. | [optional] 
**phone** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**contact_type** | **str** |  | [optional] [default to 'external']
**department** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'active']

## Example

```python
from lockally.models.external_contact_input import ExternalContactInput

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalContactInput from a JSON string
external_contact_input_instance = ExternalContactInput.from_json(json)
# print the JSON string representation of the object
print(ExternalContactInput.to_json())

# convert the object into a dict
external_contact_input_dict = external_contact_input_instance.to_dict()
# create an instance of ExternalContactInput from a dict
external_contact_input_from_dict = ExternalContactInput.from_dict(external_contact_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


