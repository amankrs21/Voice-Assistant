from subprocess import call
from google_trans_new import google_translator  

translator = google_translator()  
string = 'aapne khana khaya'
translate_text = translator.translate(string,lang_tgt='en')  
print(translate_text)
call(['espeak', '-v', 'mb-us1', translate_text])