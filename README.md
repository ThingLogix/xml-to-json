# ThingLogix  
### AWS Lambda function to convert an xml file to json   

## Installation guide  
Clone this repository and upload to AWS lambda with whatever name you see fit. The handler should be *xml-to-json.lambda_handler* and the runtime should be *python3.6*.   

## Usage  
After you have installed your function, actually running it is simple. You have to pass in a JSON of the following form:   
```
{
    "isFile": boolean,
    "xml": String,
    "attributes": boolean
}
```  
**isFile**: a boolean value (True/False) which specifies if the xml value is a file path or plain text.    
**xml**: the file path or text XML you want converted to JSON     
**attributes**: a boolean value which specifies if you want to keep the attributes on the XML file (id, b, etc)    

## Example     
If you uploaded the following JSON to the function:      
```
{
    "isFile": True,
    "xml": "sample_xml.xml",
    "attributes": True
}
```     

sample_xml.xml:       
```
<?xml version="1.0"?>
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications 
      with XML.</description>
   </book>
   <book id="bk102">
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies, 
      an evil sorceress, and her own childhood to become queen 
      of the world.</description>
   </book>
   <book id="bk103">
      <author>Corets, Eva</author>
      <title>Maeve Ascendant</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-11-17</publish_date>
      <description>After the collapse of a nanotechnology 
      society in England, the young survivors lay the 
      foundation for a new society.</description>
   </book>
</catalog>
```

Output:
```
{  
   "catalog":{  
      "book":[  
         {  
            "@id":"bk101",
            "author":{  
               "$":"Gambardella, Matthew"
            },
            "title":{  
               "$":"XML Developer's Guide"
            },
            "genre":{  
               "$":"Computer"
            },
            "price":{  
               "$":44.95
            },
            "publish_date":{  
               "$":"2000-10-01"
            },
            "description":{  
               "$":"An in-depth look at creating applications \n      with XML."
            }
         },
         {  
            "@id":"bk102",
            "author":{  
               "$":"Ralls, Kim"
            },
            "title":{  
               "$":"Midnight Rain"
            },
            "genre":{  
               "$":"Fantasy"
            },
            "price":{  
               "$":5.95
            },
            "publish_date":{  
               "$":"2000-12-16"
            },
            "description":{  
               "$":"A former architect battles corporate zombies, \n      an evil sorceress, and her own childhood to become queen \n      of the world."
            }
         },
         {  
            "@id":"bk103",
            "author":{  
               "$":"Corets, Eva"
            },
            "title":{  
               "$":"Maeve Ascendant"
            },
            "genre":{  
               "$":"Fantasy"
            },
            "price":{  
               "$":5.95
            },
            "publish_date":{  
               "$":"2000-11-17"
            },
            "description":{  
               "$":"After the collapse of a nanotechnology \n      society in England, the young survivors lay the \n      foundation for a new society."
            }
         }
      ]
   }
}
```
