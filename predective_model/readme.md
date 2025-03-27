Aquí encontrarás la información relacionada con el modelo predictivo. 

El archivo *fpkm_all_samples_with_genes_wiso_mean_L1.csv* es la matriz de expresión de los transcritos en valores de [FPKM's](https://www.rna-seqblog.com/rpkm-fpkm-and-tpm-clearly-explained/) (Fragments Per Kilobase of transcript per Million mapped reads ). Las filas corresponden a los transcritos y las columnas corresponden a la condición experimental evaluada junto con el número de replica, los números impares (1,3,5) coresponden a replicas biológicas y los pares (2,4,6)corresponden a replicas técnicas de cada una de las biólogicas. Es decir, las replicas van en pares, por cada replica biológica tenemos una replica técnica (1:2,3:4,5:6). 

Nuestras condicones experimentales corresponden a macrófagos entrenados por el micromabiente tumoral (TME) del cáncer de mama. Algunos de ellos se consideran agresivos y otros no agresivos.

| TME | Definición |
|--------------|-------------|
| MCF7 | No agresivo |
| T47D | No agresivo |
| UIVC-1 | Mo agresivo |
| UIVC-4 | Agresivo | 
| MDA-MB-231 | Agresivo |


Los macrófagos UIVC-1 son controversiales porque a nivel transcriptómico he observado que se asocian con las condiciones no agresivas. Sin embargo, a nivel fenotipo, mediante una caracterización funcional se determinarón como agresivos. 

Nota: los macrófagos UIVC-1 & UIVC-4 son de gran valor biológico porque provienen de muestras de pacientes con cáncer de mama. En cambio, las demás condiciones corresponden a líneas celulares.

En la matriz verás una condición basal y UIVC-GM-CSF, la primera representa a la población de monocitos y la segunda son monocitos estímulados con GM-CSF para inducir la diferenciación de monocitos a macrófagos.Estas dos condiciones no represetan macrófagos entrenados por el microambiente tumoral así que es importante tener esto en cuenta para los análisis.   
