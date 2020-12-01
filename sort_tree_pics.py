import pandas as pd
import os
import shutil
label_df = pd.read_csv('tree-data/train.csv')
labels = list(label_df['label'].unique())


def get_label(label_df, x):
    #label = label_df[label_df['image_id'] == x].label
    label = label_df[label_df['image_id'] ==x]['label']
    #label = label_df.query('image_id==' + str(x))['label']
    #label = label_df.loc[label_df.columns[0] == x, label_df.columns[1]].iloc[0]                 
    return label





directory = 'tree-data/train_images/'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filename = str(filename)
        print(os.path.join(directory, filename))
        label = get_label(label_df, filename)
        print(int(label)) #pics/
        old_path_str = os.path.join(directory, filename)
        new_directory = str(directory+str(int(label))
        new_path_str = os.path.join(directory+str(int(label)))
        print(label)
        shutil.move(old_path_str, new_path_str)
        break
    else:
        continue

directory='tree-data/train_images/'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filename = str(filename)
        print(os.path.join(directory, filename))
        label = get_label(label_df, filename)
        print(int(label))
        old_path_str = os.path.join(directory, filename)
        #new_directory = str(directory+str(int(label)))
        new_path_str = os.path.join(directory+str(int(label)))
        print(label)
        shutil.move(old_path_str, new_path_str)

directory='tree-data/train_images/'
files = os.listdir(directory)
sub_sample = files.random.sample(files, int(.1*len(files)))
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filename = str(filename)
        print(os.path.join(directory, filename))


for l in labels:
    os.mkdir('tree-data-mini-10/train_images/' + str(int(l)) 


import pandas as pd
import os
import shutil
label_df = pd.read_csv('tree-data/train.csv')
labels = list(label_df['label'].unique())


def get_label(label_df, x):
    #label = label_df[label_df['image_id'] == x].label
    label = label_df[label_df['image_id'] ==x]['label']
    #label = label_df.query('image_id==' + str(x))['label']
    #label = label_df.loc[label_df.columns[0] == x, label_df.columns[1]].iloc[0]                 
    return label


directory='tree-data-2/train_images/'
files = os.listdir(directory)

sub_sample = random.sample(files, int(.85*len(files)))

for filename in sub_sample:
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filename = str(filename)
        print(os.path.join(directory, filename))
        label = get_label(label_df, filename)
        print(int(label))
        old_path_str = os.path.join(directory, filename)
        #new_directory = str(directory+str(int(label)))
        new_path_str = os.path.join('tree-data-mini-10/train_images/'+str(int(label)))
        print(label)
        shutil.move(old_path_str, new_path_str)



, a kind of lightweight “philosophy.” This analytical approach allows a very unique -- and perhaps truly the most powerful -- literary invention of all time. Dickens usinged narrative to make common that which was not. Approached from a literary angle, Dickens then figures as a great author who accomplished one of the most challenging written pieces ever. However, approached from a philosophical perspective, Dickens adapted the popular understanding of the bible -- what I would understand as a godly action. A story written with this objective from a writerly standpoint ought to be criticized as a foolish endeavour. Indeed one might even criticize a writer with such lofty aspirations entirely ill-informed and under-read. However as a philosopher, Dickens’ attempt seems perfectly natural. Many philosophers proffer ideas in which they claim to entirely believe. The philosopher must, however, understand all ideas may not work. The ideas that do make it must ascend beyond a level of “popularity,” instead, achieving a status of “reality” (likely believed to have come about for some other philosophical reason such as “utility”).

\
