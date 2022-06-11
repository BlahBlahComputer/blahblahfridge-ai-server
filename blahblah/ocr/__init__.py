import easyocr

reader = easyocr.Reader(['ko'], gpu=False)

# reader = Reader(['ko'], gpu=True,
#                     model_storage_directory='./model',
#                     user_network_directory='./user_net',
#                     recog_network='korean_g2')

# reader = Reader(['ko'], gpu=True,
#                     model_storage_directory='./model',
#                     user_network_directory='./user_net',
#                     recog_network='custom')


source_list = ['간장','고추장','된장','쌈장','참기름','계란','밀가루','오이','두부','떡']