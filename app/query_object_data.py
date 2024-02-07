# Fetch objects from Weaviate
try:
    query = '{ Get { Article { title content datePublished url } } }'
    result = client.query.raw(query)
    
    # Extracting the 'Article' objects from the result
    articles = result['data']['Get']['Article']
    
    # Writing data to a file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
    
    print(f"Exported {len(articles)} articles to {OUTPUT_FILE}")

except Exception as e:
    print(f"An error occurred: {str(e)}")