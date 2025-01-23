# dexie-browser
Browser for administration of Dexie.js databases


## Candidates for exploration

1. Sequence Analysis
BioJS: A collection of JavaScript components for visualizing biological data. BioJS provides a wide range of modules for tasks like sequence alignment, structure visualization, and more.
SeqViz: A library for visualizing DNA and protein sequences, plasmid maps, and more. It works well with synthetic biology tools.
2. Genomic Data
Genoverse: A genome browser built with JavaScript and HTML5. It allows you to visualize and interact with genomic data.
JBrowse: A genome browser implemented in JavaScript, designed for fast and dynamic exploration of genomic data.
3. Visualization
D3.js: While not specific to bioinformatics, D3.js is a powerful library for creating dynamic and interactive data visualizations, including bioinformatics data.
Plotly.js: A graphing library that can be used to visualize complex bioinformatics datasets in 2D and 3D.
4. Molecular Visualization
3Dmol.js: A molecular visualization library for 3D structures such as proteins, nucleic acids, and small molecules.
NGL Viewer: A web-based molecular viewer for visualizing macromolecular structures.
5. Phylogenetics
PhyloCanvas: A JavaScript library for visualizing phylogenetic trees.
jsPhyloSVG: A library for drawing and customizing phylogenetic trees in SVG format.
6. Data Parsing and Processing
biojs-io-parser: A suite of parsers for bioinformatics file formats such as FASTA, GFF, and GenBank.
bio-pv: A JavaScript library for parsing and visualizing protein data bank (PDB) files.
7. Workflow and Computational Biology
Cytoscape.js: A library for graph theory analysis and visualization, often used for biological network data.


## Bootstrap Database

`npx dexie-cloud create`
`npx dexie-cloud whitelist http://localhost:3000`

Create `roles.json`
`npx dexie-cloud import roles.json`
