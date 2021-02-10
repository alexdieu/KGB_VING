# KGB_VING
KGB_VING is an open-source package installer for python .

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
