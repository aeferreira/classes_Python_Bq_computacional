
Informação obtida por acesso à Internet: (módulo ``requests``).
===============================================================

.. code:: ipython3

    import requests
    r = requests.get('http://www.uniprot.org/uniprot/P00924.fasta')
    print(r.text)


.. parsed-literal::

    >sp|P00924|ENO1_YEAST Enolase 1 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) OX=559292 GN=ENO1 PE=1 SV=3
    MAVSKVYARSVYDSRGNPTVEVELTTEKGVFRSIVPSGASTGVHEALEMRDGDKSKWMGK
    GVLHAVKNVNDVIAPAFVKANIDVKDQKAVDDFLISLDGTANKSKLGANAILGVSLAASR
    AAAAEKNVPLYKHLADLSKSKTSPYVLPVPFLNVLNGGSHAGGALALQEFMIAPTGAKTF
    AEALRIGSEVYHNLKSLTKKRYGASAGNVGDEGGVAPNIQTAEEALDLIVDAIKAAGHDG
    KIKIGLDCASSEFFKDGKYDLDFKNPNSDKSKWLTGPQLADLYHSLMKRYPIVSIEDPFA
    EDDWEAWSHFFKTAGIQIVADDLTVTNPKRIATAIEKKAADALLLKVNQIGTLSESIKAA
    QDSFAAGWGVMVSHRSGETEDTFIADLVVGLRTGQIKTGAPARSERLAKLNQLLRIEEEL
    GDNAVFAGENFHHGDKL
    
    

.. code:: ipython3

    linhas = r.text.split('\n')
    
    if linhas[0].startswith('>'):
        cab = linhas[0]
        seq = ''.join(linhas[1:])
    else:
        cab = ""
        seq = ''.join(linhas)
    
    print("cabeçalho: ", cab)
    print("sequência:")
    print(seq)


.. parsed-literal::

    cabeçalho:  >sp|P00924|ENO1_YEAST Enolase 1 OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) OX=559292 GN=ENO1 PE=1 SV=3
    sequência:
    MAVSKVYARSVYDSRGNPTVEVELTTEKGVFRSIVPSGASTGVHEALEMRDGDKSKWMGKGVLHAVKNVNDVIAPAFVKANIDVKDQKAVDDFLISLDGTANKSKLGANAILGVSLAASRAAAAEKNVPLYKHLADLSKSKTSPYVLPVPFLNVLNGGSHAGGALALQEFMIAPTGAKTFAEALRIGSEVYHNLKSLTKKRYGASAGNVGDEGGVAPNIQTAEEALDLIVDAIKAAGHDGKIKIGLDCASSEFFKDGKYDLDFKNPNSDKSKWLTGPQLADLYHSLMKRYPIVSIEDPFAEDDWEAWSHFFKTAGIQIVADDLTVTNPKRIATAIEKKAADALLLKVNQIGTLSESIKAAQDSFAAGWGVMVSHRSGETEDTFIADLVVGLRTGQIKTGAPARSERLAKLNQLLRIEEELGDNAVFAGENFHHGDKL
    

.. code:: ipython3

    import requests
    r = requests.get('http://www.uniprot.org/uniprot/P00924.txt')
    print(r.text)


.. parsed-literal::

    ID   ENO1_YEAST              Reviewed;         437 AA.
    AC   P00924; D6VV34; P99013;
    DT   21-JUL-1986, integrated into UniProtKB/Swiss-Prot.
    DT   05-OCT-2010, sequence version 3.
    DT   28-MAR-2018, entry version 203.
    DE   RecName: Full=Enolase 1;
    DE            EC=4.2.1.11;
    DE   AltName: Full=2-phospho-D-glycerate hydro-lyase 1;
    DE   AltName: Full=2-phosphoglycerate dehydratase 1;
    GN   Name=ENO1; Synonyms=ENOA, HSP48; OrderedLocusNames=YGR254W;
    GN   ORFNames=G9160;
    OS   Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
    OC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina;
    OC   Saccharomycetes; Saccharomycetales; Saccharomycetaceae; Saccharomyces.
    OX   NCBI_TaxID=559292;
    RN   [1]
    RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].
    RX   PubMed=6256394;
    RA   Holland M.J., Holland J.P., Thill G.P., Jackson K.A.;
    RT   "The primary structures of two yeast enolase genes. Homology between
    RT   the 5' noncoding flanking regions of yeast enolase and glyceraldehyde-
    RT   3-phosphate dehydrogenase genes.";
    RL   J. Biol. Chem. 256:1385-1395(1981).
    RN   [2]
    RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].
    RC   STRAIN=ATCC 204508 / S288c;
    RX   PubMed=9133741;
    RX   DOI=10.1002/(SICI)1097-0061(19970330)13:4<369::AID-YEA81>3.0.CO;2-V;
    RA   Mazzoni C., Ruzzi M., Rinaldi T., Solinas F., Montebove F.,
    RA   Frontali L.;
    RT   "Sequence analysis of a 10.5 kb DNA fragment from the yeast chromosome
    RT   VII reveals the presence of three new open reading frames and of a
    RT   tRNAThr gene.";
    RL   Yeast 13:369-372(1997).
    RN   [3]
    RP   NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA].
    RC   STRAIN=ATCC 204508 / S288c;
    RX   PubMed=9169869;
    RA   Tettelin H., Agostoni-Carbone M.L., Albermann K., Albers M.,
    RA   Arroyo J., Backes U., Barreiros T., Bertani I., Bjourson A.J.,
    RA   Brueckner M., Bruschi C.V., Carignani G., Castagnoli L., Cerdan E.,
    RA   Clemente M.L., Coblenz A., Coglievina M., Coissac E., Defoor E.,
    RA   Del Bino S., Delius H., Delneri D., de Wergifosse P., Dujon B.,
    RA   Durand P., Entian K.-D., Eraso P., Escribano V., Fabiani L.,
    RA   Fartmann B., Feroli F., Feuermann M., Frontali L., Garcia-Gonzalez M.,
    RA   Garcia-Saez M.I., Goffeau A., Guerreiro P., Hani J., Hansen M.,
    RA   Hebling U., Hernandez K., Heumann K., Hilger F., Hofmann B.,
    RA   Indge K.J., James C.M., Klima R., Koetter P., Kramer B., Kramer W.,
    RA   Lauquin G., Leuther H., Louis E.J., Maillier E., Marconi A.,
    RA   Martegani E., Mazon M.J., Mazzoni C., McReynolds A.D.K.,
    RA   Melchioretto P., Mewes H.-W., Minenkova O., Mueller-Auer S.,
    RA   Nawrocki A., Netter P., Neu R., Nombela C., Oliver S.G., Panzeri L.,
    RA   Paoluzi S., Plevani P., Portetelle D., Portillo F., Potier S.,
    RA   Purnelle B., Rieger M., Riles L., Rinaldi T., Robben J.,
    RA   Rodrigues-Pousada C., Rodriguez-Belmonte E., Rodriguez-Torres A.M.,
    RA   Rose M., Ruzzi M., Saliola M., Sanchez-Perez M., Schaefer B.,
    RA   Schaefer M., Scharfe M., Schmidheini T., Schreer A., Skala J.,
    RA   Souciet J.-L., Steensma H.Y., Talla E., Thierry A., Vandenbol M.,
    RA   van der Aart Q.J.M., Van Dyck L., Vanoni M., Verhasselt P., Voet M.,
    RA   Volckaert G., Wambutt R., Watson M.D., Weber N., Wedler E., Wedler H.,
    RA   Wipfli P., Wolf K., Wright L.F., Zaccaria P., Zimmermann M.,
    RA   Zollner A., Kleine K.;
    RT   "The nucleotide sequence of Saccharomyces cerevisiae chromosome VII.";
    RL   Nature 387:81-84(1997).
    RN   [4]
    RP   GENOME REANNOTATION.
    RC   STRAIN=ATCC 204508 / S288c;
    RX   PubMed=24374639; DOI=10.1534/g3.113.008995;
    RA   Engel S.R., Dietrich F.S., Fisk D.G., Binkley G., Balakrishnan R.,
    RA   Costanzo M.C., Dwight S.S., Hitz B.C., Karra K., Nash R.S., Weng S.,
    RA   Wong E.D., Lloyd P., Skrzypek M.S., Miyasato S.R., Simison M.,
    RA   Cherry J.M.;
    RT   "The reference genome sequence of Saccharomyces cerevisiae: Then and
    RT   now.";
    RL   G3 (Bethesda) 4:389-398(2014).
    RN   [5]
    RP   PROTEIN SEQUENCE OF 2-437.
    RX   PubMed=7005235;
    RA   Chin C.C.Q., Brewer J.M., Wold F.;
    RT   "The amino acid sequence of yeast enolase.";
    RL   J. Biol. Chem. 256:1377-1384(1981).
    RN   [6]
    RP   PROTEIN SEQUENCE OF 2-12.
    RC   STRAIN=ATCC 26786 / X2180-1A;
    RA   Sanchez J.-C., Golaz O., Schaller D., Morch F., Frutiger S.,
    RA   Hughes G.J., Appel R.D., Deshusses J., Hochstrasser D.F.;
    RL   Submitted (AUG-1995) to UniProtKB.
    RN   [7]
    RP   PROTEIN SEQUENCE OF 30-47.
    RC   STRAIN=ATCC 204508 / S288c;
    RX   PubMed=7895733; DOI=10.1002/elps.11501501210;
    RA   Garrels J.I., Futcher B., Kobayashi R., Latter G.I., Schwender B.,
    RA   Volpe T., Warner J.R., McLaughlin C.S.;
    RT   "Protein identifications for a Saccharomyces cerevisiae protein
    RT   database.";
    RL   Electrophoresis 15:1466-1486(1994).
    RN   [8]
    RP   PROTEIN SEQUENCE OF 69-79.
    RC   STRAIN=ATCC 38531 / Y41;
    RX   PubMed=7737086; DOI=10.1002/elps.1150160124;
    RA   Norbeck J., Blomberg A.;
    RT   "Gene linkage of two-dimensional polyacrylamide gel electrophoresis
    RT   resolved proteins from isogene families in Saccharomyces cerevisiae by
    RT   microsequencing of in-gel trypsin generated peptides.";
    RL   Electrophoresis 16:149-156(1995).
    RN   [9]
    RP   MUTAGENESIS OF LYS-346.
    RX   PubMed=8634301; DOI=10.1021/bi952186y;
    RA   Poyner R.R., Laughlin L.T., Sowa G.A., Reed G.H.;
    RT   "Toward identification of acid/base catalysts in the active site of
    RT   enolase: comparison of the properties of K345A, E168Q, and E211Q
    RT   variants.";
    RL   Biochemistry 35:1692-1699(1996).
    RN   [10]
    RP   MUTAGENESIS OF HIS-160.
    RX   PubMed=11027610; DOI=10.1006/bbrc.2000.3618;
    RA   Brewer J.M., Holland M.J., Lebioda L.;
    RT   "The H159A mutant of yeast enolase 1 has significant activity.";
    RL   Biochem. Biophys. Res. Commun. 276:1199-1202(2000).
    RN   [11]
    RP   SUBCELLULAR LOCATION.
    RX   PubMed=11502169; DOI=10.1021/bi010277r;
    RA   Grandier-Vazeille X., Bathany K., Chaignepain S., Camougrand N.,
    RA   Manon S., Schmitter J.-M.;
    RT   "Yeast mitochondrial dehydrogenases are associated in a supramolecular
    RT   complex.";
    RL   Biochemistry 40:9758-9769(2001).
    RN   [12]
    RP   MUTAGENESIS OF HIS-160 AND ASN-208.
    RX   PubMed=13678299; DOI=10.1023/A:1025390123761;
    RA   Brewer J.M., Glover C.V., Holland M.J., Lebioda L.;
    RT   "Enzymatic function of loop movement in enolase: preparation and some
    RT   properties of H159N, H159A, H159F, and N207A enolases.";
    RL   J. Protein Chem. 22:353-361(2003).
    RN   [13]
    RP   LEVEL OF PROTEIN EXPRESSION [LARGE SCALE ANALYSIS].
    RX   PubMed=14562106; DOI=10.1038/nature02046;
    RA   Ghaemmaghami S., Huh W.-K., Bower K., Howson R.W., Belle A.,
    RA   Dephoure N., O'Shea E.K., Weissman J.S.;
    RT   "Global analysis of protein expression in yeast.";
    RL   Nature 425:737-741(2003).
    RN   [14]
    RP   PHOSPHORYLATION [LARGE SCALE ANALYSIS] AT SER-119, AND IDENTIFICATION
    RP   BY MASS SPECTROMETRY [LARGE SCALE ANALYSIS].
    RX   PubMed=17287358; DOI=10.1073/pnas.0607084104;
    RA   Chi A., Huttenhower C., Geer L.Y., Coon J.J., Syka J.E.P., Bai D.L.,
    RA   Shabanowitz J., Burke D.J., Troyanskaya O.G., Hunt D.F.;
    RT   "Analysis of phosphorylation sites on proteins from Saccharomyces
    RT   cerevisiae by electron transfer dissociation (ETD) mass
    RT   spectrometry.";
    RL   Proc. Natl. Acad. Sci. U.S.A. 104:2193-2198(2007).
    RN   [15]
    RP   UBIQUITINATION [LARGE SCALE ANALYSIS] AT LYS-358, AND IDENTIFICATION
    RP   BY MASS SPECTROMETRY [LARGE SCALE ANALYSIS].
    RX   PubMed=22106047; DOI=10.1002/pmic.201100166;
    RA   Starita L.M., Lo R.S., Eng J.K., von Haller P.D., Fields S.;
    RT   "Sites of ubiquitin attachment in Saccharomyces cerevisiae.";
    RL   Proteomics 12:236-240(2012).
    RN   [16]
    RP   X-RAY CRYSTALLOGRAPHY (2.25 ANGSTROMS).
    RX   PubMed=3374614; DOI=10.1038/333683a0;
    RA   Lebioda L., Stec B.;
    RT   "Crystal structure of enolase indicates that enolase and pyruvate
    RT   kinase evolved from a common ancestor.";
    RL   Nature 333:683-686(1988).
    RN   [17]
    RP   X-RAY CRYSTALLOGRAPHY (2.25 ANGSTROMS).
    RX   PubMed=2645275;
    RA   Lebioda L., Stec B., Brewer J.M.;
    RT   "The structure of yeast enolase at 2.25-A resolution. An 8-fold beta +
    RT   alpha-barrel with a novel beta beta alpha alpha (beta alpha)6
    RT   topology.";
    RL   J. Biol. Chem. 264:3685-3693(1989).
    RN   [18]
    RP   X-RAY CRYSTALLOGRAPHY (2.25 ANGSTROMS).
    RX   PubMed=2405163; DOI=10.1016/0022-2836(90)90023-F;
    RA   Stec B., Lebioda L.;
    RT   "Refined structure of yeast apo-enolase at 2.25-A resolution.";
    RL   J. Mol. Biol. 211:235-248(1990).
    RN   [19]
    RP   X-RAY CRYSTALLOGRAPHY (1.8 ANGSTROMS) IN COMPLEX WITH SUBSTRATE AND
    RP   MAGNESIUM IONS.
    RX   PubMed=8605183; DOI=10.1021/bi952859c;
    RA   Larsen T.M., Wedekind J.E., Rayment I., Reed G.H.;
    RT   "A carboxylate oxygen of the substrate bridges the magnesium ions at
    RT   the active site of enolase: structure of the yeast enzyme complexed
    RT   with the equilibrium mixture of 2-phosphoglycerate and
    RT   phosphoenolpyruvate at 1.8-A resolution.";
    RL   Biochemistry 35:4349-4358(1996).
    RN   [20]
    RP   X-RAY CRYSTALLOGRAPHY (2.0 ANGSTROMS) IN COMPLEX WITH SUBSTRATE.
    RX   PubMed=9376357; DOI=10.1021/bi9712450;
    RA   Zhang E., Brewer J.M., Minor W., Carreira L.A., Lebioda L.;
    RT   "Mechanism of enolase: the crystal structure of asymmetric dimer
    RT   enolase-2-phospho-D-glycerate/enolase-phosphoenolpyruvate at 2.0-A
    RT   resolution.";
    RL   Biochemistry 36:12526-12534(1997).
    RN   [21]
    RP   X-RAY CRYSTALLOGRAPHY (2.1 ANGSTROMS) OF MUTANT ALA-40 IN COMPLEX WITH
    RP   MAGNESIUM IONS AND SUBSTRATE ANALOG.
    RX   PubMed=12054465; DOI=10.1016/S0003-9861(02)00024-3;
    RA   Poyner R.R., Larsen T.M., Wong S.-W., Reed G.H.;
    RT   "Functional and structural changes due to a serine to alanine mutation
    RT   in the active-site flap of enolase.";
    RL   Arch. Biochem. Biophys. 401:155-163(2002).
    RN   [22]
    RP   X-RAY CRYSTALLOGRAPHY (1.8 ANGSTROMS) OF MUTANT GLN-212 AND MUTANT
    RP   GLN-169.
    RX   PubMed=12846578; DOI=10.1021/bi0346345;
    RA   Sims P.A., Larsen T.M., Poyner R.R., Cleland W.W., Reed G.H.;
    RT   "Reverse protonation is the key to general acid-base catalysis in
    RT   enolase.";
    RL   Biochemistry 42:8298-8306(2003).
    CC   -!- CATALYTIC ACTIVITY: 2-phospho-D-glycerate = phosphoenolpyruvate +
    CC       H(2)O.
    CC   -!- COFACTOR:
    CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
    CC       Note=Mg(2+) is required for catalysis and for stabilizing the
    CC       dimer.;
    CC   -!- PATHWAY: Carbohydrate degradation; glycolysis; pyruvate from D-
    CC       glyceraldehyde 3-phosphate: step 4/5.
    CC   -!- SUBUNIT: Homodimer. {ECO:0000269|PubMed:12054465,
    CC       ECO:0000269|PubMed:8605183, ECO:0000269|PubMed:9376357}.
    CC   -!- INTERACTION:
    CC       P11484:SSB1; NbExp=3; IntAct=EBI-6468, EBI-8627;
    CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:11502169}.
    CC   -!- MISCELLANEOUS: Present with 76700 molecules/cell in log phase SD
    CC       medium. {ECO:0000269|PubMed:14562106}.
    CC   -!- SIMILARITY: Belongs to the enolase family. {ECO:0000305}.
    CC   -----------------------------------------------------------------------
    CC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms
    CC   Distributed under the Creative Commons Attribution-NoDerivs License
    CC   -----------------------------------------------------------------------
    DR   EMBL; J01322; AAA88712.1; -; Genomic_DNA.
    DR   EMBL; X99228; CAA67616.1; -; Genomic_DNA.
    DR   EMBL; Z73039; CAA97283.1; -; Genomic_DNA.
    DR   EMBL; BK006941; DAA08345.1; -; Genomic_DNA.
    DR   PIR; S64586; NOBY.
    DR   RefSeq; NP_011770.3; NM_001181383.3.
    DR   PDB; 1EBG; X-ray; 2.10 A; A/B=2-437.
    DR   PDB; 1EBH; X-ray; 1.90 A; A/B=2-437.
    DR   PDB; 1ELS; X-ray; 2.40 A; A=2-437.
    DR   PDB; 1L8P; X-ray; 2.10 A; A/B/C/D=2-437.
    DR   PDB; 1NEL; X-ray; 2.60 A; A=2-437.
    DR   PDB; 1ONE; X-ray; 1.80 A; A/B=2-437.
    DR   PDB; 1P43; X-ray; 1.80 A; A/B=2-437.
    DR   PDB; 1P48; X-ray; 2.00 A; A/B=2-437.
    DR   PDB; 2AL1; X-ray; 1.50 A; A/B=2-437.
    DR   PDB; 2AL2; X-ray; 1.85 A; A/B=2-437.
    DR   PDB; 2ONE; X-ray; 2.00 A; A/B=2-437.
    DR   PDB; 2XGZ; X-ray; 1.80 A; A/B=2-437.
    DR   PDB; 2XH0; X-ray; 1.70 A; A/B/C/D=2-437.
    DR   PDB; 2XH2; X-ray; 1.80 A; A/B/C/D=2-437.
    DR   PDB; 2XH4; X-ray; 1.70 A; A/B/C/D=2-437.
    DR   PDB; 2XH7; X-ray; 1.80 A; A/B=2-437.
    DR   PDB; 3ENL; X-ray; 2.25 A; A=2-437.
    DR   PDB; 4ENL; X-ray; 1.90 A; A=2-437.
    DR   PDB; 5ENL; X-ray; 2.20 A; A=2-437.
    DR   PDB; 6ENL; X-ray; 2.20 A; A=2-437.
    DR   PDB; 7ENL; X-ray; 2.20 A; A=2-437.
    DR   PDBsum; 1EBG; -.
    DR   PDBsum; 1EBH; -.
    DR   PDBsum; 1ELS; -.
    DR   PDBsum; 1L8P; -.
    DR   PDBsum; 1NEL; -.
    DR   PDBsum; 1ONE; -.
    DR   PDBsum; 1P43; -.
    DR   PDBsum; 1P48; -.
    DR   PDBsum; 2AL1; -.
    DR   PDBsum; 2AL2; -.
    DR   PDBsum; 2ONE; -.
    DR   PDBsum; 2XGZ; -.
    DR   PDBsum; 2XH0; -.
    DR   PDBsum; 2XH2; -.
    DR   PDBsum; 2XH4; -.
    DR   PDBsum; 2XH7; -.
    DR   PDBsum; 3ENL; -.
    DR   PDBsum; 4ENL; -.
    DR   PDBsum; 5ENL; -.
    DR   PDBsum; 6ENL; -.
    DR   PDBsum; 7ENL; -.
    DR   ProteinModelPortal; P00924; -.
    DR   SMR; P00924; -.
    DR   BioGrid; 33505; 132.
    DR   DIP; DIP-5561N; -.
    DR   IntAct; P00924; 105.
    DR   MINT; P00924; -.
    DR   STRING; 4932.YGR254W; -.
    DR   Allergome; 786; Sac c Enolase.
    DR   CarbonylDB; P00924; -.
    DR   iPTMnet; P00924; -.
    DR   COMPLUYEAST-2DPAGE; P00924; -.
    DR   SWISS-2DPAGE; P00924; -.
    DR   UCD-2DPAGE; P00924; -.
    DR   MaxQB; P00924; -.
    DR   PaxDb; P00924; -.
    DR   PRIDE; P00924; -.
    DR   TopDownProteomics; P00924; -.
    DR   EnsemblFungi; YGR254W; YGR254W; YGR254W.
    DR   GeneID; 853169; -.
    DR   KEGG; sce:YGR254W; -.
    DR   EuPathDB; FungiDB:YGR254W; -.
    DR   SGD; S000003486; ENO1.
    DR   GeneTree; ENSGT00910000144064; -.
    DR   HOGENOM; HOG000072174; -.
    DR   InParanoid; P00924; -.
    DR   KO; K01689; -.
    DR   OMA; EFMIIPV; -.
    DR   OrthoDB; EOG092C2W5X; -.
    DR   BioCyc; YEAST:YGR254W-MONOMER; -.
    DR   BRENDA; 4.2.1.11; 984.
    DR   SABIO-RK; P00924; -.
    DR   UniPathway; UPA00109; UER00187.
    DR   EvolutionaryTrace; P00924; -.
    DR   PRO; PR:P00924; -.
    DR   Proteomes; UP000002311; Chromosome VII.
    DR   GO; GO:0000324; C:fungal-type vacuole; IDA:SGD.
    DR   GO; GO:0005739; C:mitochondrion; IDA:SGD.
    DR   GO; GO:0000015; C:phosphopyruvate hydratase complex; IDA:SGD.
    DR   GO; GO:0000287; F:magnesium ion binding; IEA:InterPro.
    DR   GO; GO:0004634; F:phosphopyruvate hydratase activity; IMP:SGD.
    DR   GO; GO:0006094; P:gluconeogenesis; IEP:SGD.
    DR   GO; GO:0006096; P:glycolytic process; IMP:SGD.
    DR   GO; GO:0032889; P:regulation of vacuole fusion, non-autophagic; IDA:SGD.
    DR   CDD; cd03313; enolase; 1.
    DR   Gene3D; 3.20.20.120; -; 1.
    DR   Gene3D; 3.30.390.10; -; 1.
    DR   HAMAP; MF_00318; Enolase; 1.
    DR   InterPro; IPR000941; Enolase.
    DR   InterPro; IPR036849; Enolase-like_C_sf.
    DR   InterPro; IPR029017; Enolase-like_N.
    DR   InterPro; IPR034390; Enolase-like_superfamily.
    DR   InterPro; IPR020810; Enolase_C.
    DR   InterPro; IPR020809; Enolase_CS.
    DR   InterPro; IPR020811; Enolase_N.
    DR   PANTHER; PTHR11902; PTHR11902; 1.
    DR   Pfam; PF00113; Enolase_C; 1.
    DR   Pfam; PF03952; Enolase_N; 1.
    DR   PIRSF; PIRSF001400; Enolase; 1.
    DR   PRINTS; PR00148; ENOLASE.
    DR   SFLD; SFLDG00178; enolase; 1.
    DR   SFLD; SFLDS00001; Enolase; 1.
    DR   SMART; SM01192; Enolase_C; 1.
    DR   SMART; SM01193; Enolase_N; 1.
    DR   SUPFAM; SSF51604; SSF51604; 1.
    DR   TIGRFAMs; TIGR01060; eno; 1.
    DR   PROSITE; PS00164; ENOLASE; 1.
    PE   1: Evidence at protein level;
    KW   3D-structure; Complete proteome; Cytoplasm; Direct protein sequencing;
    KW   Glycolysis; Isopeptide bond; Lyase; Magnesium; Metal-binding;
    KW   Phosphoprotein; Reference proteome; Ubl conjugation.
    FT   INIT_MET      1      1       Removed. {ECO:0000269|PubMed:7005235,
    FT                                ECO:0000269|Ref.6}.
    FT   CHAIN         2    437       Enolase 1.
    FT                                /FTId=PRO_0000134062.
    FT   REGION      373    376       Substrate binding.
    FT   ACT_SITE    212    212       Proton donor. {ECO:0000305}.
    FT   ACT_SITE    346    346       Proton acceptor.
    FT   METAL       247    247       Magnesium. {ECO:0000269|PubMed:8605183}.
    FT   METAL       296    296       Magnesium. {ECO:0000269|PubMed:8605183}.
    FT   METAL       321    321       Magnesium. {ECO:0000269|PubMed:8605183}.
    FT   BINDING     160    160       Substrate. {ECO:0000269|PubMed:8605183,
    FT                                ECO:0000269|PubMed:9376357}.
    FT   BINDING     169    169       Substrate. {ECO:0000269|PubMed:8605183,
    FT                                ECO:0000269|PubMed:9376357}.
    FT   BINDING     296    296       Substrate. {ECO:0000269|PubMed:8605183,
    FT                                ECO:0000269|PubMed:9376357}.
    FT   BINDING     321    321       Substrate. {ECO:0000269|PubMed:8605183,
    FT                                ECO:0000269|PubMed:9376357}.
    FT   BINDING     397    397       Substrate. {ECO:0000269|PubMed:8605183,
    FT                                ECO:0000269|PubMed:9376357}.
    FT   MOD_RES     119    119       Phosphoserine.
    FT                                {ECO:0000244|PubMed:17287358}.
    FT   MOD_RES     138    138       Phosphoserine.
    FT                                {ECO:0000250|UniProtKB:P00925}.
    FT   MOD_RES     188    188       Phosphoserine.
    FT                                {ECO:0000250|UniProtKB:P00925}.
    FT   MOD_RES     313    313       Phosphothreonine.
    FT                                {ECO:0000250|UniProtKB:P00925}.
    FT   MOD_RES     324    324       Phosphothreonine.
    FT                                {ECO:0000250|UniProtKB:P00925}.
    FT   CROSSLNK     60     60       Glycyl lysine isopeptide (Lys-Gly)
    FT                                (interchain with G-Cter in ubiquitin).
    FT                                {ECO:0000250|UniProtKB:P00925}.
    FT   CROSSLNK    243    243       Glycyl lysine isopeptide (Lys-Gly)
    FT                                (interchain with G-Cter in ubiquitin).
    FT                                {ECO:0000250|UniProtKB:P00925}.
    FT   CROSSLNK    358    358       Glycyl lysine isopeptide (Lys-Gly)
    FT                                (interchain with G-Cter in ubiquitin).
    FT                                {ECO:0000244|PubMed:22106047}.
    FT   MUTAGEN      40     40       S->A: Reduces activity by 99.9%.
    FT   MUTAGEN     160    160       H->A,F,N: Reduces activity by 99%.
    FT                                {ECO:0000269|PubMed:11027610,
    FT                                ECO:0000269|PubMed:13678299}.
    FT   MUTAGEN     169    169       E->Q: Reduces Kcat over 100000-fold.
    FT   MUTAGEN     208    208       N->A: Reduces activity by 44%.
    FT                                {ECO:0000269|PubMed:13678299}.
    FT   MUTAGEN     212    212       E->Q: Reduces Kcat over 100000-fold.
    FT   MUTAGEN     346    346       K->A: Reduces Kcat over 100000-fold.
    FT                                Abolishes of the proton exchange reaction
    FT                                that initiates the enzymatic reaction.
    FT                                {ECO:0000269|PubMed:8634301}.
    FT   CONFLICT    242    242       I -> V (in Ref. 1; AAA88712).
    FT                                {ECO:0000305}.
    FT   STRAND        5     12       {ECO:0000244|PDB:2AL1}.
    FT   STRAND       18     26       {ECO:0000244|PDB:2AL1}.
    FT   STRAND       29     34       {ECO:0000244|PDB:2AL1}.
    FT   STRAND       43     45       {ECO:0000244|PDB:1EBH}.
    FT   HELIX        57     59       {ECO:0000244|PDB:2AL1}.
    FT   HELIX        63     71       {ECO:0000244|PDB:2AL1}.
    FT   HELIX        73     80       {ECO:0000244|PDB:2AL1}.
    FT   HELIX        87     98       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      100    102       {ECO:0000244|PDB:1EBH}.
    FT   TURN        104    106       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       108    125       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       130    138       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      145    147       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      152    156       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       158    160       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      161    164       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      169    173       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       180    202       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       204    207       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      213    215       {ECO:0000244|PDB:1P48}.
    FT   HELIX       222    236       {ECO:0000244|PDB:2AL1}.
    FT   TURN        239    241       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      243    247       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       250    253       {ECO:0000244|PDB:2AL1}.
    FT   TURN        261    264       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       270    272       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       276    289       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      292    296       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       304    311       {ECO:0000244|PDB:2AL1}.
    FT   TURN        312    314       {ECO:0000244|PDB:2AL2}.
    FT   STRAND      316    321       {ECO:0000244|PDB:2AL1}.
    FT   TURN        322    326       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       328    336       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      341    345       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       347    350       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       353    365       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      369    373       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       383    390       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      394    397       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       404    420       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       421    423       {ECO:0000244|PDB:2AL1}.
    FT   STRAND      424    426       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       428    430       {ECO:0000244|PDB:2AL1}.
    FT   HELIX       434    436       {ECO:0000244|PDB:2AL1}.
    SQ   SEQUENCE   437 AA;  46816 MW;  69F45214DBD375BE CRC64;
         MAVSKVYARS VYDSRGNPTV EVELTTEKGV FRSIVPSGAS TGVHEALEMR DGDKSKWMGK
         GVLHAVKNVN DVIAPAFVKA NIDVKDQKAV DDFLISLDGT ANKSKLGANA ILGVSLAASR
         AAAAEKNVPL YKHLADLSKS KTSPYVLPVP FLNVLNGGSH AGGALALQEF MIAPTGAKTF
         AEALRIGSEV YHNLKSLTKK RYGASAGNVG DEGGVAPNIQ TAEEALDLIV DAIKAAGHDG
         KIKIGLDCAS SEFFKDGKYD LDFKNPNSDK SKWLTGPQLA DLYHSLMKRY PIVSIEDPFA
         EDDWEAWSHF FKTAGIQIVA DDLTVTNPKR IATAIEKKAA DALLLKVNQI GTLSESIKAA
         QDSFAAGWGV MVSHRSGETE DTFIADLVVG LRTGQIKTGA PARSERLAKL NQLLRIEEEL
         GDNAVFAGEN FHHGDKL
    //
    
    

**Problema:**

-  obter a informação relativa à proteína P00924
-  filtar a linha começada por **SQ**
-  mostar o numero de aminoácidos e a massa molecular.

A informação relativa ao formato desta linha (embora seja evidente
olhando para um exemplo) está descrita na `documentação da
UniProt <http://web.expasy.org/docs/userman.html#SQ_line>`__

A linha tem o formato

``SQ   SEQUENCE XXXX AA; XXXXX MW; XXXXXXXXXXXXXXXX CRC64;``

.. code:: ipython3

    import requests
    info = requests.get('http://www.uniprot.org/uniprot/P00924.txt').text
    
    linhas = info.split('\n')
    
    sq = ''
    for i in linhas:
        if i.startswith('SQ'):
            sq = i
    
    print('linha SQ:')
    print(sq)
    
    # SQ   SEQUENCE XXXX AA; XXXXX MW; XXXXXXXXXXXXXXXX CRC64;
    partes = sq.split()
    print(partes[2], 'aminoácidos')
    print(partes[4], 'Da')


.. parsed-literal::

    linha SQ:
    SQ   SEQUENCE   437 AA;  46816 MW;  69F45214DBD375BE CRC64;
    437 aminoácidos
    46816 Da
    

Na `documentação da
UniProt <http://web.expasy.org/docs/userman.html#FT_keys>`__, realtiva
às linhas começadas por ``FT`` pode-se ler...

::

    INIT_MET - Initiator methionine.

    This feature key is associated with a '1' value in the 'FROM' and 'TO' fields to indicate that the initiator methionine has been cleaved off:


        FT   INIT_MET      1      1       Removed.

    It is not used when the initiator methionine is not cleaved off

**Problema:**

Para as seguintes proteínas,

``Q96UH7, Q8J0N6, Q9URB4, Q9C2U0, P36580, P14540``

gerar uma tabela com

``AC       AA         MW       init M cleaved``
