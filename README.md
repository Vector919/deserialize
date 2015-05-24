# deserialize
Create generic objects from XML or JSON data

Take complicated or deeply nested JSON/XML data, and transform it into generic objects

Example
======
```python
	api_data = '{"user":
			{"profile":
				{"description": "a basic user profile description"}{
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
