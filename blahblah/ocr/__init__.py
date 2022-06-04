import easyocr

reader = easyocr.Reader(['ko'], gpu=False)

source_list = ['간장','고추장','된장','쌈장','참기름','계란','밀가루']