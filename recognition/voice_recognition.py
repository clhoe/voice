#!/usr/bin/env python

from pocketsphinx.pocketsphinx import Decoder

config = Decoder.default_config()
config.set_string('-hmm', 'cmusphinx-es-5.2/model_parameters/voxforge_es_sphinx.cd_ptm_4000')
config.set_string('-lm', 'es-20k.lm.gz')
config.set_string('-dict', 'es.dict')
config.set_string('-logfn', '/dev/null')
decoder = Decoder(config)

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()
stream = open('message.wav', 'rb')
while True:
  buf = stream.read()
  if buf:
    print "Decode!"
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()

words=[seg.word for seg in decoder.seg()]

string=''
for w in words:
    if w in ["<s>", "</s>"]:
        continue
    if w in ["<sil>"]:
        continue
    string+=w+' '

print string


