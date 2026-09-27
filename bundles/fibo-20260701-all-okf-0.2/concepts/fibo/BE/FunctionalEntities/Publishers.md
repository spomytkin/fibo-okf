---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: The concept of a publisher is central to the notion of a data provider in financial markets. This ontology defines
      the fundamental concepts for publishers of information, including entities whose primary function is to publish, and
      those (whether or not they are publishers in that sense) that play the role of the publisher of some information.
  - predicate: http://purl.org/dc/terms/license
    value: "2013-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group, Inc.\n\t\t\n\
      Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation\
      \ files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use,\
      \ copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to\
      \ whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this\
      \ permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED\
      \ 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Publishers Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20140501/FunctionalEntities/Publishers.rdf version of this ontology
      was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/FunctionalEntities/Publishers.rdf version of this ontology
      was modified per the FIBO 2.0 RFC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/FunctionalEntities/Publishers.rdf version of this ontology
      was modified to eliminate references to external dictionary sites that no longer resolve.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20210101/FunctionalEntities/Publishers.rdf version of this ontology
      was modified to deprecate publishing house rather than having two disconnected concepts, clean up the related restrictions,
      and add market data provider (originally in IND).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20221001/FunctionalEntities/Publishers.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary and revise definitions to be ISO 704 compliant as needed.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/FunctionalEntities/Publishers.rdf version of the ontology
      was modified to eliminate deprecations that are more than 6 months old.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20231101/FunctionalEntities/Publishers.rdf version of the ontology
      was modified to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology
      Library (Commons) v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20231201/FunctionalEntities/Publishers.rdf version of the ontology
      was modified to replace additional concepts from several FIBO FND ontologies with their counterparts added to the Commons
      Ontology Library (Commons) v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20250301/FunctionalEntities/Publishers.rdf version of the ontology
      was modified to loosen various constraints to better reflect use case requirements (SEC-205).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20260101/FunctionalEntities/Publishers.rdf version of the ontology
      was modified to add market data provider discrimination required for examples (FND-407).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20260601/FunctionalEntities/Publishers/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
sources:
- id: fibo-source-c08bba6665
  resource: references/fibo/BE/FunctionalEntities/Publishers.rdf
  sha256: c08bba6665f5e8fa0f777c7625413d35aa10a63353e739c085127bbbe73c5d28
  title: FIBO source BE/FunctionalEntities/Publishers.rdf
title: Publishers Ontology
type: Ontology Definition
---

# Publishers Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/>

## Relationships

- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [Publishers](<https://spec.edmcouncil.org/fibo/ontology/BE/20260601/FunctionalEntities/Publishers/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: The concept of a publisher is central to the notion of a data provider in financial markets. This ontology defines the fundamental concepts for publishers of information, including entities whose primary function is to publish, and those (whether or not they are publishers in that sense) that play the role of the publisher of some information.
- **license**: 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Publishers Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20140501/FunctionalEntities/Publishers.rdf version of this ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/FunctionalEntities/Publishers.rdf version of this ontology was modified per the FIBO 2.0 RFC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/FunctionalEntities/Publishers.rdf version of this ontology was modified to eliminate references to external dictionary sites that no longer resolve.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20210101/FunctionalEntities/Publishers.rdf version of this ontology was modified to deprecate publishing house rather than having two disconnected concepts, clean up the related restrictions, and add market data provider (originally in IND).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20221001/FunctionalEntities/Publishers.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary and revise definitions to be ISO 704 compliant as needed.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/FunctionalEntities/Publishers.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20231101/FunctionalEntities/Publishers.rdf version of the ontology was modified to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20231201/FunctionalEntities/Publishers.rdf version of the ontology was modified to replace additional concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20250301/FunctionalEntities/Publishers.rdf version of the ontology was modified to loosen various constraints to better reflect use case requirements (SEC-205).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20260101/FunctionalEntities/Publishers.rdf version of the ontology was modified to add market data provider discrimination required for examples (FND-407).
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
