# ReturnPathCheck

Present after a verify call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mx** | **bool** |  | [optional] 
**spf** | **bool** |  | [optional] 

## Example

```python
from lockally.models.return_path_check import ReturnPathCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPathCheck from a JSON string
return_path_check_instance = ReturnPathCheck.from_json(json)
# print the JSON string representation of the object
print(ReturnPathCheck.to_json())

# convert the object into a dict
return_path_check_dict = return_path_check_instance.to_dict()
# create an instance of ReturnPathCheck from a dict
return_path_check_from_dict = ReturnPathCheck.from_dict(return_path_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


