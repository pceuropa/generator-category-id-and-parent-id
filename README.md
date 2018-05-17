# generator-category-id-and-parend-id
Generating the id and parent_id category from csv list (python3)

This method need manual prepare of categories tree 
   
```
CsvRead('csv/categories_example.csv').toList()
categories = generatorIDCategory(c)
CsvRead('csv/export_categories.csv').save(categories)
# or another method save categories name, id, parent_id
```

[Example categories](csv/categories_example.csv) before generate id/parent_id  
[Example categories](csv/export_categories.csv) after
