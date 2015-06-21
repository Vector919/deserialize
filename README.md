# deserialize
Create generic objects from XML or JSON data, and do basic transformations/mutations

Take complicated or deeply nested JSON/XML data, and transform it into generic objects

Example
======
```python
api_data = '{
    "user":{
        "profile":{
            "description":"a basic user profile description",
            "user_profile_id":2063090311
        },
        "preferences":{
            "screen_resolution":"800x600",
            "ishygddt":true
        }
    }
}'
	user_data = deseralize.fromJSON(api_data)
	
	print user_data.user.profile.description # prints "a basic user profile description"
```
you can also do some basic trasnformations to your data with lambda functions

```python
data_config = {
    'time': lambda x: strftime(x)
}
gen_obj = deserialize.from_json(data, config=data_config)

# gen_obj.thing.time == datetime object

```
