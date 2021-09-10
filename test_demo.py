###
"""
####################################################################
################# DeepPhaseUnw demonstration #######################
####################################################################

Created on Thu Apr 1 2021

@authors: 
Francesco Calvanese
Francescopaolo Sica


Microwaves and Radar Institute
German Aerospace Center (DLR)
Münchener Str. 20, 82234 Weßling

email: name.surname@dlr.de

The present code is implemented on the basis of the paper:
Sica, F., Calvanese, F., Scarpa, G., & Rizzoli, P. (2020). 
"A CNN-Based Coherence-Driven Approach for InSAR Phase Unwrapping." 
IEEE Geoscience and Remote Sensing Letters.

#################################################################
"""

import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"  # assign the GPU's identification number to the processor
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"  # INFO, WARNING messages are not printed (default is 0)


import sys
import argparse
import time
import numpy as np
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
from keras.models import load_model
import DeepPhaseUnw
sys.stderr = stderr 



def parse_args():
    parser = argparse.ArgumentParser()
#    ====================== INPUT DATA FOLDER ====================
    parser.add_argument('--input_dir', default='./input/', type=str, help='directory of test data')
#    ====================== MODEL FOLDER ====================
    parser.add_argument('--model_dir', default='./trained_model/', type=str, help='directory of the model')
    parser.add_argument('--model_name_x', default='DeepPhaseUnw_x.hdf5', type=str, help='the model name - x-axis')
    parser.add_argument('--model_name_y', default='DeepPhaseUnw_y.hdf5', type=str, help='the model name - y-axis')
#    ====================== OUTPUT DATA FOLDER ====================
    parser.add_argument('--output_dir', default='./output/', type=str, help='directory of unwrapped phase')

    return parser.parse_args()


   
if __name__ == '__main__':    
    
    
    args = parse_args()
    DeepPhaseUnw.check_inputs(args)

    print('============== Read input file ================')
    phase, coher, m_, n_ = DeepPhaseUnw.read_data(args.input_dir, 'phase.npy', 'coherence.npy')
    m, n = np.shape(phase)

    print('========= Load DeepPhaseUnw trained models ==========')
    model_x = DeepPhaseUnw.load_the_model(os.path.join(args.model_dir, args.model_name_x), m, n)
    model_y = DeepPhaseUnw.load_the_model(os.path.join(args.model_dir, args.model_name_y), m, n)
      
    print('================ Estimation ===================')
    start_time = time.time()
    unwPh = DeepPhaseUnw.inference(phase,coher,model_x,model_y, m_, n_)
    elapsed_time = time.time() - start_time
    print('%10s : %2.4f second'%('time:',elapsed_time))
    
    print('================ Save output ==================')
    print('File: %s' % os.path.join(args.output_dir, 'unwrapped_phase.npy'))
    np.save(os.path.join(args.output_dir,'unwrapped_phase.npy'), unwPh)
        
    print('=================== DONE ======================')
    sys.exit(0)
