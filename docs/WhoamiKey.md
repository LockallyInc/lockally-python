# WhoamiKey

Present only when auth is api_key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from lockally.models.whoami_key import WhoamiKey

# TODO update the JSON string below
json = "{}"
# create an instance of WhoamiKey from a JSON string
whoami_key_instance = WhoamiKey.from_json(json)
# print the JSON string representation of the object
print(WhoamiKey.to_json())

# convert the object into a dict
whoami_key_dict = whoami_key_instance.to_dict()
# create an instance of WhoamiKey from a dict
whoami_key_from_dict = WhoamiKey.from_dict(whoami_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


