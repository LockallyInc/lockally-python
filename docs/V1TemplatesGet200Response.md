# V1TemplatesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Template]**](Template.md) |  | [optional] 

## Example

```python
from lockally.models.v1_templates_get200_response import V1TemplatesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1TemplatesGet200Response from a JSON string
v1_templates_get200_response_instance = V1TemplatesGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1TemplatesGet200Response.to_json())

# convert the object into a dict
v1_templates_get200_response_dict = v1_templates_get200_response_instance.to_dict()
# create an instance of V1TemplatesGet200Response from a dict
v1_templates_get200_response_from_dict = V1TemplatesGet200Response.from_dict(v1_templates_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


