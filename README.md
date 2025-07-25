# SuGaR + Gaussian Grouping
## Combine SuGaR and Gaussian Grouping to jointly learn semantic features while binding Gaussian Splatting with mesh geometry

### Description
(1) Baseline Code: [SuGaR](https://github.com/Anttwo/SuGaR.git) <br>
(2) Rasterization Code: [Gaussian-Grouping](https://github.com/lkeab/gaussian-grouping.git) <br>
(3) Modified the refinement pipeline in SuGaR (Only GS binding related) <br>

---
### Preparing Dataset
(1) Same as SuGaR process: COLMAP based dataset <br>
(2) Object mask dataset: Following Gaussian-Grouping [prepare_pseudo_label.sh](https://github.com/lkeab/gaussian-grouping/blob/0ab60afed3385b717c985af1d30a20f7b0884c89/script/prepare_pseudo_label.sh) <br>
(3) both dataset all same folder <br>
(4) Mesh result (trained from (1) dataset)

---
### Installation
(1) Pull Docker 
  ```
    $ docker pull pootti524/3dgs_reloc
  ```

(2) clone githubs in src
  ```
    $ cd ./src
    $ git clone --recursive https://github.com/SungJaeShin/SuGaR_SemanticGS.git
    $ git clone https://github.com/facebookresearch/pytorch3d.git
    $ cd pytorch3d
    $ git checkout v0.7.4
    $ cd ../../
  ```

(3) install dependencies
  ```
    $ pip3 install -e ./src/pytorch3d
    $ pip3 install plotly==5.18.0
    $ pip3 install rich==13.7.0
    $ pip3 install ./src/SuGaR_SemanticGS/gaussian_splatting/submodules/diff-gaussian-rasterization
    $ pip3 install ./src/SuGaR_SemanticGS/gaussian_splatting/submodules/simple-knn
  ```

---
### Binding Mesh + Semantic GS
```
  $ TORCH_USE_CUDA_DSA=1 CUDA_LAUNCH_BLOCKING=1 python3 train_refined.py --add_semantic true --scene_path ${SCENE_PATH} --checkpoint_path ${CHECKPOINT_PATH} --mesh_path ${MESH}.ply --output_dir ${RESULT_PATH}
```

---
### Parameters related semantic 
(1) `num_classes`: Number of semantic categories for training; default is **256.** <br>
(2) `num_objects`: Number of object-level semantic feature channels used for training and rendering; default is **16.**

---
### License
This project inherits its license terms from the **SuGaR** and **Gaussian-Grouping** repository.
Accordingly, this work is licensed for research and evaluation purposes only, under the same non-commercial license as Gaussian Splatting and SuGaR.
Commercial use, distribution, or sublicensing is not permitted without prior and explicit consent from the original authors.
Please contact the original authors (Inria, MPII) for any licensing inquiries related to commercial applications.
For more information, refer to the **Gaussian Splatting** License.



