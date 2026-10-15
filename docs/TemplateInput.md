# TemplateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Template name (1–120 chars). | 
**subject** | **str** | May contain {{variable}} placeholders. | [optional] 
**html** | **str** | HTML body; {{variable}} values are HTML-escaped. | [optional] 
**text** | **str** | Plain-text body. | [optional] 

## Example

```python
from lockally.models.template_input import TemplateInput

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateInput from a JSON string
template_input_instance = TemplateInput.from_json(json)
# print the JSON string representation of the object
print(TemplateInput.to_json())

# convert the object into a dict
template_input_dict = template_input_instance.to_dict()
# create an instance of TemplateInput from a dict
template_input_from_dict = TemplateInput.from_dict(template_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


