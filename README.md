## General

Automated pipeline for preparation and execution of Molecular Dynamics (MD) in cloud 

**Pipeline Workflow:**
Raw Data (from pdb) ➔ 3D structure preparation ➔ Creation of Topology File ➔ Solvation and Ionization ➔ Energy Minimization ➔ Equilibration ➔ Production ➔ Analytics

graph LR
    A[Raw Data] --> B[3D Preparation]
    B --> C[Topology File]
    C --> D[Solvation/Ionization]
    D --> E[Minimization]
    E --> F[Equilibration]
    F --> G[Production]
    G --> H[Analytics]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#bbf,stroke:#333,stroke-width:2px
