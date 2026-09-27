---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines high-level legal concepts for use in other FIBO ontology elements. These concepts include
      law and constitution, both of which are framed at a more abstract level than national or state laws and constitutions,
      so that law forms the basis both for statutes and for company by-laws, and constitution forms the basis both for national
      or state constitutions and for instruments which are constitutive of incorporated legal entities. This ontology also
      defines some of the variants of these such as governmental constitutions and ordinances. Court of Law is also defined
      here.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2025 EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group, Inc.\n\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Legal Core Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20130801/Law/LegalCore.rdf version of the ontology was was modified per
      the issue resolutions identified in the FIBO FND 1.0 FTF report and in http://www.omg.org/spec/EDMC-FIBO/FND/1.0/AboutFND-1.0/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Law/LegalCore.rdf version of the ontology was was modified per
      the FIBO 2.0 RFC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "The http://www.omg.org/spec/FIBO/Foundations/20130601/Law/LegalCore.owl version of the ontology was revised in\
      \ advance of the September 2013 New Brunswick, NJ meeting, as follows:\n\t(1) to use slash style URI/IRIss (also called\
      \ 303 URIs, vs. hash style) as required to support server side processing \n\t(2) to use version-independent IRIs for\
      \ all definitions internally as opposed to version-specific IRIs\n\t(3) to change the file suffix from .owl to .rdf\
      \ to increase usability in RDF tools\n\t(4) to use 4-level abbreviations and corresponding namespace prefixes for all\
      \ FIBO ontologies, reflecting a family/specification/module/ontology structure\n\t(5) to incorporate changes to the\
      \ specification metadata to support documentation at the family, specification, module, and ontology level, similar\
      \ to the abbreviations.\n\t(6) to revise some of the text definitions using more formal sources."
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Law/LegalCore.rdf version of the ontology was revised
      to correct the camel case name of hasInForce (was hasInforce).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200501/Law/LegalCore.rdf version of the ontology was revised
      to eliminate circular and ambiguous definitions, and simplify the ontology by eliminating unused concepts, including
      GovernmentalConstitution, Ordinance and narrowly defined and unused properties - constrains and isConstrainedBy.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210101/Law/LegalCore.rdf version of the ontology was revised
      to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Law/LegalCore.rdf version of the ontology was modified
      to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Law/LegalCore.rdf version of this ontology was modified
      to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating
      redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Law/LegalCore.rdf version of the ontology was modified
      to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Law/LegalCore/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/
sources:
- id: fibo-source-31fe191c06
  resource: references/fibo/FND/Law/LegalCore.rdf
  sha256: 31fe191c06f11a104ba752303784bfd17673c9e515a6e3d3ed538b19a5da37e9
  title: FIBO source FND/Law/LegalCore.rdf
title: Legal Core Ontology
type: Ontology Definition
---

# Legal Core Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/>

## Relationships

- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [LegalCore](<https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Law/LegalCore/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines high-level legal concepts for use in other FIBO ontology elements. These concepts include law and constitution, both of which are framed at a more abstract level than national or state laws and constitutions, so that law forms the basis both for statutes and for company by-laws, and constitution forms the basis both for national or state constitutions and for instruments which are constitutive of incorporated legal entities. This ontology also defines some of the variants of these such as governmental constitutions and ordinances. Court of Law is also defined here.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Legal Core Ontology
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20130801/Law/LegalCore.rdf version of the ontology was was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in http://www.omg.org/spec/EDMC-FIBO/FND/1.0/AboutFND-1.0/.
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Law/LegalCore.rdf version of the ontology was was modified per the FIBO 2.0 RFC.
- **changeNote**: The http://www.omg.org/spec/FIBO/Foundations/20130601/Law/LegalCore.owl version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows: 	(1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing  	(2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs 	(3) to change the file suffix from .owl to .rdf to increase usability in RDF tools 	(4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure 	(5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations. 	(6) to revise some of the text definitions using more formal sources.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Law/LegalCore.rdf version of the ontology was revised to correct the camel case name of hasInForce (was hasInforce).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200501/Law/LegalCore.rdf version of the ontology was revised to eliminate circular and ambiguous definitions, and simplify the ontology by eliminating unused concepts, including GovernmentalConstitution, Ordinance and narrowly defined and unused properties - constrains and isConstrainedBy.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210101/Law/LegalCore.rdf version of the ontology was revised to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Law/LegalCore.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Law/LegalCore.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Law/LegalCore.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
