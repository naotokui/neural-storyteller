"""
Configuration for the generate module
"""

#-----------------------------------------------------------------------------#
# Flags for running on CPU
#-----------------------------------------------------------------------------#
FLAG_CPU_MODE = False

#-----------------------------------------------------------------------------#
# Paths to models and biases
#-----------------------------------------------------------------------------#
paths = dict()

# Skip-thoughts
paths['skmodels'] = './skip-thoughts-models/'
paths['sktables'] = './skip-thoughts-models/'

# Decoder
paths['decmodel'] = 'neural_storyteller/romance.npz'
paths['dictionary'] = 'neural_storyteller/romance_dictionary.pkl'

# Image-sentence embedding
paths['vsemodel'] = 'neural_storyteller/coco_embedding.npz'

# VGG-19 convnet
paths['vgg'] = 'models/vgg19.pkl'
paths['pycaffe'] = '/usr/local/DL-Box/digits-2.0/caffe/python'
paths['vgg_proto_caffe'] = './models/vgg19/VGG_19_deploy.prototxt'
paths['vgg_model_caffe'] = './models/vgg19/VGG_ILSVRC_19_layers.caffemodel'

# COCO training captions
paths['captions'] = 'neural_storyteller/coco_train_caps.txt'

# Biases
paths['negbias'] = 'neural_storyteller/caption_style.npy'
paths['posbias'] = 'neural_storyteller/romance_style.npy'
#paths['posbias'] = 'neural_storyteller/swift_style.npy'
