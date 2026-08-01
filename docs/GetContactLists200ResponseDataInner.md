# GetContactLists200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 

## Example

```python
from lockally.models.get_contact_lists200_response_data_inner import GetContactLists200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetContactLists200ResponseDataInner from a JSON string
get_contact_lists200_response_data_inner_instance = GetContactLists200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetContactLists200ResponseDataInner.to_json())

# convert the object into a dict
get_contact_lists200_response_data_inner_dict = get_contact_lists200_response_data_inner_instance.to_dict()
# create an instance of GetContactLists200ResponseDataInner from a dict
get_contact_lists200_response_data_inner_from_dict = GetContactLists200ResponseDataInner.from_dict(get_contact_lists200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


