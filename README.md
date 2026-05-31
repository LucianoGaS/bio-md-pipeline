## General

Automated pipeline for preparation and execution of Molecular Dynamics (MD) simulations in cloud 

**Pipeline Workflow:**
The pipeline follows standard MD protocols:
Raw Data (from pdb) ➔ 3D structure preparation ➔ Creation of Topology File ➔ Solvation and Ionization ➔ Energy Minimization ➔ Equilibration ➔ Production ➔ Analytics

Due to GitHub's file size restrictions for large data files, the simulation pipeline is hosted as an interactive **Google Colab notebook**. On this repository, I share only the Python codes necessary to plot graphs for Temperature, Density, Pressure and RMSD data.

plot.py is a script used to plot any GROMACS graph.
>Usage: python plot.py -f <file_name>.xvg

## Online Execution
To run this pipeline directly in your browser, access the link and please navigate to File > Save a copy in your Drive:
[Click here to open in Google Colab](https://colab.research.google.com/drive/1QPyvHEQnYBl6h_elTvyClfjNQ8h5yRvG#scrollTo=5USDRQB0Lrx3)
