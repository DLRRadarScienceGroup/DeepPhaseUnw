--------

Summary
-------

The present code implements the Phase Unwrapping of Synthetic Aperture Radar (SAR) interferograms.
This procedure is rephrased as a Semantic Segmentation task.  
As additional input feature, we used the interferometric coherence, which provides information about the local noise level 
and further increase the robustness to noise.

The code has been developed at the Microwaves and Radar Institute of the 
German Aerospace Center (DLR). Münchener Str. 20, 82234 Weßling.


Academic publications
---------------------

The present code is implemented on the basis of the paper:

* F\. Sica, F. Calvanese, G. Scarpa and P. Rizzoli, *A CNN-Based Coherence-Driven Approach for InSAR Phase Unwrapping*, in IEEE Transactions on Geoscience and Remote Sensing, doi: 10.1109/TGRS.2020.3020427.

If you use this code in your own research, please cite `our paper describing it <https://www.researchgate.net/publication/344889815_A_CNN-Based_Coherence-Driven_Approach_for_InSAR_Phase_Unwrapping>`_.

BibTex
@ARTICLE{9234534,

  author={Sica, Francescopaolo and Calvanese, Francesco and Scarpa, Giuseppe and Rizzoli, Paola},

  journal={IEEE Geoscience and Remote Sensing Letters}, 

  title={A CNN-Based Coherence-Driven Approach for InSAR Phase Unwrapping}, 

  year={2020},

  pages={1-5},
  
  doi={10.1109/LGRS.2020.3029565}}


Authors
-------

* Francesco Calvanese
* Francescopaolo Sica


HowTo
-----

Folders
````````

* `DeepPhaseUnw/input </DeepPhaseUnw/input>`_: input files `phase.npy` and `coherence.npy`.
* `DeepPhaseUnw/trained_model </DeepPhaseUnw/trained_model>`_: DeepPhaseUnw trained models.
* `DeepPhaseUnw/output </DeepPhaseUnw/output>`_: output files `unwrapped_phase.npy`.

The trained models can be downloaded here:
DeepPhaseUnw_x.hdf5: https://www.dropbox.com/s/quz8pwr6d8oinqx/DeepPhaseUnw_x.hdf5?dl=0
DeepPhaseUnw_y.hdf5: https://www.dropbox.com/s/2jdu758lhlvyipl/DeepPhaseUnw_y.hdf5?dl=0

Insert them in the corresponding folder: 
* `DeepPhaseUnw/trained_model </DeepPhaseUnw/trained_model>`_: DeepPhaseUnw trained models.

Demo steps (for Linux distribution)
````````````````````````````````````

1) Create environment from `YAML`::

  conda env create --name deepunw_env --file requirements.yml

2) Activate environment::

  source activate deepunw_env

3) Launch test::

  python test_demo.py

4) Visualize results obtained from the test::

  python visualize_results.py


Dependencies
------------

The ``requirements.yml`` file lists all packages necessary to run the
``test_demo.py`` file in the ``DeepPhaseUnw`` folder.

This package is developed under Python 3.7 with tensorflow 1.13.1. 

Acknowledgements 
----------------

The authors would like to acknowledge Philipp Posovszky and Andrea Pulella for their support in the set up of this repository.


License
-------

::

Copyright © 2021 Deutsches Zentrum für Luft und Raumfahrt e.V.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the “Software”), to deal in the Software without 
restriction, including without limitation the rights to use, copy, modify, merge, publish, 
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or 
substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING 
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

