# Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
import json
Text={"Name":"Abhishek","Designation":"CEO of navgurukul","Gender":"male","Age":"29"}
text=open("my_text.json","w")
y=json.dump(Text,text,indent=4)
print(Text)