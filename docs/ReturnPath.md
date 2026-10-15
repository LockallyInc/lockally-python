# ReturnPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**host** | **str** |  | 
**records** | [**List[DNSRecord]**](DNSRecord.md) |  | 
**check** | [**ReturnPathCheck**](ReturnPathCheck.md) |  | [optional] 
**requested_at** | **datetime** |  | [optional] 
**verified_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.return_path import ReturnPath

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPath from a JSON string
return_path_instance = ReturnPath.from_json(json)
# print the JSON string representation of the object
print(ReturnPath.to_json())

# convert the object into a dict
return_path_dict = return_path_instance.to_dict()
# create an instance of ReturnPath from a dict
return_path_from_dict = ReturnPath.from_dict(return_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


