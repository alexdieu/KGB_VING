# KGB_VING
KGB_VING is an open-source package installer/Manager for python .

## HOW DO I CREATE PACKAGE ?

Create your own json file

```
{
        "author":"Alexdieu",
        "name":"urlscanner",
	"blurb": "Scanning an URL and gather information about .",
	"package":["https://raw.githubusercontent.com/alexdieu/PyurlscannerLIB/master/urlscanner.py"]
}
```

You can have mutiple packages . (like ` "package":["https://raw.githubusercontent.com/alexdieu/PyurlscannerLIB/master/urlscanner.py", "other1.com/example.py", "other.com/exmaple.py]`)

PLEASE MAKE SURE THE CONTENT IS RAW . DO NOT SEND WITH CUSTOM POLICIES OR ELSE. JUST UPLOAD THE FILE AND GET THE RAW URL .

### FOR WHAT UTILISATION WAS IT CREATED ?

It was created in the goal of creating packages in python than you can easily install and create in a short time .


## HOW DO I DELETE INSTALLED EXTENSION ?

Choose first option then type extension name (better Ctrl+C/Ctrl+V the name)
It will remove it and all its files
