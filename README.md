# Description
A simple python script for replacing the same char, string, or for adding the same strings on the head/queue of different files, configurable through a json file.

# Use
1. Put your files (you can put entire directories) in the src folder;
2. configure the `replacing-settings.json` inside `conf` folder.

# Configuration example
The next is an example that led me to write such script.<br>
I need to add to head/queue of different SOAP body requests/responses, the same SOAP headers.<br>
In some cases, I may need to replace some namespace id, with specific others.<br>
The following configuration help me to obtain my needs. 

```json
{
    "add_to_head_queue" : {
        "head":"<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\n\t<soap:Body>\n",
        "queue":"\n\t</soap:Body>\n</soap:Envelope>",
        "if_miss":"soap",
        "and": {
            "if_not_miss" : "Fault",
            "head" : "<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\n\t<soap:Body>\n\t\t<soap:Fault>\n\t\t<faultcode>soap:Server</faultcode>\n\t\t<faultstring>SET CORRECT ERROR STRING</faultstring>\n\t\t<detail>\n",
            "queue" : "\n\t\t</detail>\n\t\t</soap:Fault>\n\t</soap:Body>\n</soap:Envelope>"
        }
    },
    "replacing": [
        {
            "source": "v40:",
            "out": "ns3:"
        },
        {
            "source": "v99:",
            "out": "ns4:"
        }
    ]
}
```

The field `add_to_head_queue` let me to add in the head/queue of the files inside `src` folder accordingly some conditions.<br>
The field `if_miss` is a word that is checked inside the script to add the `head`/`queue` only if that word missing inside the files.<br>
The field `and` let me to check a second condition: if the word `Fault` is not missing, I need to use different header.<br>
You can read the configuration in this way:
- if `soap` is missing;
    - and if `Fault` is present: add SOAP fault headers;
- else: add normal SOAP headers.
