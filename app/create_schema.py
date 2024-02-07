schema = {
  "classes": [
    {
      "class": "Article",
      "description": "A class to store articles",
      "properties": [
        {"name": "title", "dataType": ["string"], "description": "The title of the article"},
        {"name": "content", "dataType": ["text"], "description": "The content of the article"},
        {"name": "datePublished", "dataType": ["date"], "description": "The date the article was published"},
        {"name": "url", "dataType": ["string"], "description": "The URL of the article"}
      ]
    },
    {
      "class": "Author",
      "description": "A class to store authors",
      "properties": [
        {"name": "name", "dataType": ["string"], "description": "The name of the author"},
        {"name": "articles", "dataType": ["Article"], "description": "The articles written by the author"}
      ]
    }
  ]
}
client.schema.delete_class('Article')
client.schema.delete_class('Author')
client.schema.create(schema)
client.schema.get()