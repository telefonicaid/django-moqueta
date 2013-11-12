{% if url_params.book_id == "752" %}
{
	"id": 752,
	"title": "Nineteen Eighty-Four",
	"author": "George Orwell",
	"published": 1949,
	"language": "English",
	"creation_time" : "2012-11-27T09:19:14Z",
	"update_time" : "2012-11-27T09:43:16Z"
}
{% else %}
{
	"id": {{url_params.book_id}},
	"title": "Brave New World",
	"author": "Aldous Huxley",
	"published": 1931,
	"language": "English",
	"creation_time" : "2012-08-14T11:15:21Z",
	"update_time" : "2012-11-16T16:53:41Z"
}
{% endif %}