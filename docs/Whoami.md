# Whoami


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **UUID** |  | [optional] 
**tenant** | **str** |  | [optional] 
**label** | **str** | The API key&#39;s label. | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from lockally.models.whoami import Whoami

# TODO update the JSON string below
json = "{}"
# create an instance of Whoami from a JSON string
whoami_instance = Whoami.from_json(json)
# print the JSON string representation of the object
print(Whoami.to_json())

# convert the object into a dict
whoami_dict = whoami_instance.to_dict()
# create an instance of Whoami from a dict
whoami_from_dict = Whoami.from_dict(whoami_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


