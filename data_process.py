import glob
import numpy as np
from shutil import copyfile

path = 'F:\\WJ\\Speaker_Verification\\dataset\\LibriSpeech-SI\\train_audio'

audio_path = glob.glob(path + '/*')

train_speaker_num = len(audio_path)
tr =  open('./data_split/Libri/libri_tr.scp',"w")
te =  open('./data_split/Libri/libri_te.scp',"w")

dic = {}
print("*train speaker number: %d"%train_speaker_num)
for i, folder in enumerate(audio_path):
    print("%dth speaker processing..."%i)

    print(int(folder[-3:]))
    for j, utter_name in enumerate(glob.glob(folder+'/*')):
        # "spk001_002.flac"
        name = utter_name[-15:]
        copyfile(utter_name,"./data_split/Libri/dataset/"+name)
        dic[name]=int(folder[-3:])
        if j >80:
            tr.write(name+"\n")
        else:
            te.write(name+"\n")

np.save("./data_split/Libri/libri_dict.npy", dic)
        






