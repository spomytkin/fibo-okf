---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology originally defined the fundamental concepts for companies incorporated by the issuance of shares.
      Terms defined in this ontology are those which are applicable to all such entities. Many of these concepts form the
      basis of the relationships of ownership and control which obtain between entities of this type.
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
    value: Corporations Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/Corporations/Corporations.rdf version of this ontology
      was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/Corporations/Corporations.rdf version of this ontology
      was modified per the FIBO 2.0 RFC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20180901/Corporations/Corporations.rdf version of this ontology
      was modified per the FIBO 2.0 RFC to generalize certain unions where they were no longer required.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190101/Corporations/Corporations.rdf version of this ontology
      was modified to reflect moving hasObjective to FND.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190401/Corporations/Corporations.rdf version of this ontology
      was modified to replace hasDefinition with isDefinedIn to clarify intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190701/Corporations/Corporations.rdf version of this ontology
      was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190901/Corporations/Corporations.rdf version of this ontology
      was modified to eliminate duplication of concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200201/Corporations/Corporations.rdf version of this ontology
      was modified to eliminate references to external dictionary sites that no longer resolve, eliminate circular and ambiguous
      definitions and make incorporation date and registration date explicit dates.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20210301/Corporations/Corporations.rdf version of this ontology
      was modified to reflect the move of some organization-specific concepts from BE to FND and to clean up typos.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20211201/Corporations/Corporations.rdf version of this ontology
      was modified to address text formatting hygiene issues and eliminate a dead link.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20220801/Corporations/Corporations.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary and revise definitions to be ISO 704 compliant as needed.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/Corporations/Corporations.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC)
      and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/Corporations/Corporations.rdf version of the ontology
      was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2
      (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20250301/Corporations/Corporations.rdf version of the ontology
      was modified to merge all constructs that were originally in this ontology with corporate bodies under legal entities
      for consistency and useability (BE-259).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20251001/Corporations/Corporations/
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Corporations/Corporations/
sources:
- id: fibo-source-5b0f0804b9
  resource: references/fibo/BE/Corporations/Corporations.rdf
  sha256: 5b0f0804b9756805e1d0acc2ea9066854d1fa189a0bfae51c5392cead774157c
  title: FIBO source BE/Corporations/Corporations.rdf
title: Corporations Ontology
type: Ontology Definition
---

# Corporations Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Corporations/Corporations/>

## Relationships

- **Related to**: [CorporateBodies](/concepts/fibo/BE/LegalEntities/CorporateBodies.md)
- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [LegalPersons](/concepts/fibo/BE/LegalEntities/LegalPersons.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [Corporations](<https://spec.edmcouncil.org/fibo/ontology/BE/20251001/Corporations/Corporations/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology originally defined the fundamental concepts for companies incorporated by the issuance of shares. Terms defined in this ontology are those which are applicable to all such entities. Many of these concepts form the basis of the relationships of ownership and control which obtain between entities of this type.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Corporations Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/Corporations/Corporations.rdf version of this ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/Corporations/Corporations.rdf version of this ontology was modified per the FIBO 2.0 RFC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20180901/Corporations/Corporations.rdf version of this ontology was modified per the FIBO 2.0 RFC to generalize certain unions where they were no longer required.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190101/Corporations/Corporations.rdf version of this ontology was modified to reflect moving hasObjective to FND.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190401/Corporations/Corporations.rdf version of this ontology was modified to replace hasDefinition with isDefinedIn to clarify intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190701/Corporations/Corporations.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190901/Corporations/Corporations.rdf version of this ontology was modified to eliminate duplication of concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200201/Corporations/Corporations.rdf version of this ontology was modified to eliminate references to external dictionary sites that no longer resolve, eliminate circular and ambiguous definitions and make incorporation date and registration date explicit dates.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20210301/Corporations/Corporations.rdf version of this ontology was modified to reflect the move of some organization-specific concepts from BE to FND and to clean up typos.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20211201/Corporations/Corporations.rdf version of this ontology was modified to address text formatting hygiene issues and eliminate a dead link.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20220801/Corporations/Corporations.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary and revise definitions to be ISO 704 compliant as needed.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/Corporations/Corporations.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/Corporations/Corporations.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20250301/Corporations/Corporations.rdf version of the ontology was modified to merge all constructs that were originally in this ontology with corporate bodies under legal entities for consistency and useability (BE-259).
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
