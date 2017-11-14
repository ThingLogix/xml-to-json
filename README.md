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
   <book id="bk104">
      <author>Corets, Eva</author>
      <title>Oberon's Legacy</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2001-03-10</publish_date>
      <description>In post-apocalypse England, the mysterious
      agent known only as Oberon helps to create a new life
      for the inhabitants of London. Sequel to Maeve
      Ascendant.</description>
   </book>
   <book id="bk105">
      <author>Corets, Eva</author>
      <title>The Sundered Grail</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2001-09-10</publish_date>
      <description>The two daughters of Maeve, half-sisters,
      battle one another for control of England. Sequel to
      Oberon's Legacy.</description>
   </book>
   <book id="bk106">
      <author>Randall, Cynthia</author>
      <title>Lover Birds</title>
      <genre>Romance</genre>
      <price>4.95</price>
      <publish_date>2000-09-02</publish_date>
      <description>When Carla meets Paul at an ornithology
      conference, tempers fly as feathers get ruffled.</description>
   </book>
   <book id="bk107">
      <author>Thurman, Paula</author>
      <title>Splish Splash</title>
      <genre>Romance</genre>
      <price>4.95</price>
      <publish_date>2000-11-02</publish_date>
      <description>A deep sea diver finds true love twenty
      thousand leagues beneath the sea.</description>
   </book>
   <book id="bk108">
      <author>Knorr, Stefan</author>
      <title>Creepy Crawlies</title>
      <genre>Horror</genre>
      <price>4.95</price>
      <publish_date>2000-12-06</publish_date>
      <description>An anthology of horror stories about roaches,
      centipedes, scorpions  and other insects.</description>
   </book>
   <book id="bk109">
      <author>Kress, Peter</author>
      <title>Paradox Lost</title>
      <genre>Science Fiction</genre>
      <price>6.95</price>
      <publish_date>2000-11-02</publish_date>
      <description>After an inadvertant trip through a Heisenberg
      Uncertainty Device, James Salway discovers the problems
      of being quantum.</description>
   </book>
   <book id="bk110">
      <author>O'Brien, Tim</author>
      <title>Microsoft .NET: The Programming Bible</title>
      <genre>Computer</genre>
      <price>36.95</price>
      <publish_date>2000-12-09</publish_date>
      <description>Microsoft's .NET initiative is explored in
      detail in this deep programmer's reference.</description>
   </book>
   <book id="bk111">
      <author>O'Brien, Tim</author>
      <title>MSXML3: A Comprehensive Guide</title>
      <genre>Computer</genre>
      <price>36.95</price>
      <publish_date>2000-12-01</publish_date>
      <description>The Microsoft MSXML3 parser is covered in
      detail, with attention to XML DOM interfaces, XSLT processing,
      SAX and more.</description>
   </book>
   <book id="bk112">
      <author>Galos, Mike</author>
      <title>Visual Studio 7: A Comprehensive Guide</title>
      <genre>Computer</genre>
      <price>49.95</price>
      <publish_date>2001-04-16</publish_date>
      <description>Microsoft Visual Studio 7 is explored in depth,
      looking at how Visual Basic, Visual C++, C#, and ASP+ are
      integrated into a comprehensive development
      environment.</description>
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
         },
         {
            "@id":"bk104",
            "author":{
               "$":"Corets, Eva"
            },
            "title":{
               "$":"Oberon's Legacy"
            },
            "genre":{
               "$":"Fantasy"
            },
            "price":{
               "$":5.95
            },
            "publish_date":{
               "$":"2001-03-10"
            },
            "description":{
               "$":"In post-apocalypse England, the mysterious \n      agent known only as Oberon helps to create a new life \n      for the inhabitants of London. Sequel to Maeve \n      Ascendant."
            }
         },
         {
            "@id":"bk105",
            "author":{
               "$":"Corets, Eva"
            },
            "title":{
               "$":"The Sundered Grail"
            },
            "genre":{
               "$":"Fantasy"
            },
            "price":{
               "$":5.95
            },
            "publish_date":{
               "$":"2001-09-10"
            },
            "description":{
               "$":"The two daughters of Maeve, half-sisters, \n      battle one another for control of England. Sequel to \n      Oberon's Legacy."
            }
         },
         {
            "@id":"bk106",
            "author":{
               "$":"Randall, Cynthia"
            },
            "title":{
               "$":"Lover Birds"
            },
            "genre":{
               "$":"Romance"
            },
            "price":{
               "$":4.95
            },
            "publish_date":{
               "$":"2000-09-02"
            },
            "description":{
               "$":"When Carla meets Paul at an ornithology \n      conference, tempers fly as feathers get ruffled."
            }
         },
         {
            "@id":"bk107",
            "author":{
               "$":"Thurman, Paula"
            },
            "title":{
               "$":"Splish Splash"
            },
            "genre":{
               "$":"Romance"
            },
            "price":{
               "$":4.95
            },
            "publish_date":{
               "$":"2000-11-02"
            },
            "description":{
               "$":"A deep sea diver finds true love twenty \n      thousand leagues beneath the sea."
            }
         },
         {
            "@id":"bk108",
            "author":{
               "$":"Knorr, Stefan"
            },
            "title":{
               "$":"Creepy Crawlies"
            },
            "genre":{
               "$":"Horror"
            },
            "price":{
               "$":4.95
            },
            "publish_date":{
               "$":"2000-12-06"
            },
            "description":{
               "$":"An anthology of horror stories about roaches,\n      centipedes, scorpions  and other insects."
            }
         },
         {
            "@id":"bk109",
            "author":{
               "$":"Kress, Peter"
            },
            "title":{
               "$":"Paradox Lost"
            },
            "genre":{
               "$":"Science Fiction"
            },
            "price":{
               "$":6.95
            },
            "publish_date":{
               "$":"2000-11-02"
            },
            "description":{
               "$":"After an inadvertant trip through a Heisenberg\n      Uncertainty Device, James Salway discovers the problems \n      of being quantum."
            }
         },
         {
            "@id":"bk110",
            "author":{
               "$":"O'Brien, Tim"
            },
            "title":{
               "$":"Microsoft .NET: The Programming Bible"
            },
            "genre":{
               "$":"Computer"
            },
            "price":{
               "$":36.95
            },
            "publish_date":{
               "$":"2000-12-09"
            },
            "description":{
               "$":"Microsoft's .NET initiative is explored in \n      detail in this deep programmer's reference."
            }
         },
         {
            "@id":"bk111",
            "author":{
               "$":"O'Brien, Tim"
            },
            "title":{
               "$":"MSXML3: A Comprehensive Guide"
            },
            "genre":{
               "$":"Computer"
            },
            "price":{
               "$":36.95
            },
            "publish_date":{
               "$":"2000-12-01"
            },
            "description":{
               "$":"The Microsoft MSXML3 parser is covered in \n      detail, with attention to XML DOM interfaces, XSLT processing, \n      SAX and more."
            }
         },
         {
            "@id":"bk112",
            "author":{
               "$":"Galos, Mike"
            },
            "title":{
               "$":"Visual Studio 7: A Comprehensive Guide"
            },
            "genre":{
               "$":"Computer"
            },
            "price":{
               "$":49.95
            },
            "publish_date":{
               "$":"2001-04-16"
            },
            "description":{
               "$":"Microsoft Visual Studio 7 is explored in depth,\n      looking at how Visual Basic, Visual C++, C#, and ASP+ are \n      integrated into a comprehensive development \n      environment."
            }
         }
      ]
   }
}
```
