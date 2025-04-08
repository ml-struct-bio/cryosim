# cryosim: Tools for generating synthetic cryo-EM images

### Dependencies:
* cryodrgn version 0.1+
* healpy (for project3d.py)

### Example usage:
```
  # Generate 10k projection images of a volume
  $ python project3d.py input_volume.mrc -N 10000 -o output_projections.mrcs --out-pose poses.pkl --t-extent 10

  # No noise addition, default CTF values added
  $ python add_ctf.py input_particles.mrcs --Apix 6 --s1 0 --s2 0 -o output_particles_w_ctf.mrcs
  
  # Add gaussian noise to SNR of 0.1
  $ python add_noise.py input_noiseless_particles.mrcs -o output_noisy_particles.mrcs --snr .1
```
### See also:

See the `cryosim` submodule within the CryoBench repo for additional features, scripts, and usage:

https://github.com/ml-struct-bio/CryoBench/tree/main/cryosim

### References:

If you find `cryosim` useful, please consider citing the [CryoBench](https://cryobench.cs.princeton.edu/) manuscript:

```
@inproceedings{jeon2024cryobench,
 author = {Jeon, Minkyu and Raghu, Rishwanth and Astore, Miro and Woollard, Geoffrey and Feathers, Ryan and Kaz, Alkin and Hanson, Sonya M. and Cossio, Pilar and Zhong, Ellen D.},
 booktitle = {Advances in Neural Information Processing Systems},
 title = {CryoBench: Diverse and challenging datasets for the heterogeneity problem in cryo-EM},
 year = {2024}
}
```
