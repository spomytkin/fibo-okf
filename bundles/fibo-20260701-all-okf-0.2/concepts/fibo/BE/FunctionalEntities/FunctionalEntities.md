---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines the fundamental concepts for entities defined by their function, such as the relationship
      to the various forms which one or another functionally-defined entity may take. It also includes a number of basic types
      of entity defined by function, such as business and non-profit. The concepts in this ontology are intended to be extensible
      in other ontologies which may be dedicated to specific kinds of functionally-defined business entity or organization.
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
    value: Functional Entities Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20150201/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified per the issue resolutions identified in the FIBO BE 1.1 RTF report. Changes include deprecation
      of the SoleProprietorship class and making it equivalent to the class with the same name in the Sole Proprietorships
      ontology. This version also introduces a new FunctionalEntity class, as the parent of FunctionalBusinessEntity in this
      ontology and as the parent of Government in the GovernmentEntities ontology.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20160801/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified by the FIBO 2.0 revision to address missing labels and definitions on the deprecated sole
      proprietorship class to match those in the equivalent class.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified to generalize certain unions where they were no longer required and eliminate an unused import.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190201/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190901/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified to eliminate duplication of concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200301/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified to revise and extend the definition of merchant, to support merchant category codes as needed
      for representation of credit card transactions, merge business and functional business entity and eliminate commerce
      and commercial activity (which are not used anywhere in FIBO), and to clean up definitions and make them ISO 704 compliant.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200901/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified to add the concept of an association.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified to address a circular definition on association.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20210201/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified to reflect the move of some organization-specific concepts from BE to FND.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20211001/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified to address text formatting hygiene issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20220801/FunctionalEntities/FunctionalEntities.rdf version of
      the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1
      (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/FunctionalEntities/FunctionalEntities.rdf version of
      this ontology was augmented to include general definitions for syndicate and syndicate member (LOAN-169).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20241101/FunctionalEntities/FunctionalEntities.rdf version of
      the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20250301/FunctionalEntities/FunctionalEntities.rdf version of
      the ontology was modified to loosen various constraints to better reflect use case requirements (SEC-205).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20251001/FunctionalEntities/FunctionalEntities.rdf version of
      the ontology was modified to replace references to the now deprecated hasTag property in Relations with its equivalent
      in OMG Commons (FND-412).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20260701/FunctionalEntities/FunctionalEntities/
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/FND/Arrangements/ClassificationSchemes.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/
sources:
- id: fibo-source-1a60609b6a
  resource: references/fibo/BE/FunctionalEntities/FunctionalEntities.rdf
  sha256: 1a60609b6ad170e85bb9424d06c7d8f740d0c98492e22a8c0c9e2e285ec47b5a
  title: FIBO source BE/FunctionalEntities/FunctionalEntities.rdf
title: Functional Entities Ontology
type: Ontology Definition
---

# Functional Entities Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/>

## Relationships

- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [ClassificationSchemes](/concepts/fibo/FND/Arrangements/ClassificationSchemes.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [CodesAndCodeSets](<https://www.omg.org/spec/Commons/CodesAndCodeSets/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [FunctionalEntities](<https://spec.edmcouncil.org/fibo/ontology/BE/20260701/FunctionalEntities/FunctionalEntities/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines the fundamental concepts for entities defined by their function, such as the relationship to the various forms which one or another functionally-defined entity may take. It also includes a number of basic types of entity defined by function, such as business and non-profit. The concepts in this ontology are intended to be extensible in other ontologies which may be dedicated to specific kinds of functionally-defined business entity or organization.
- **license**: 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Functional Entities Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20150201/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified per the issue resolutions identified in the FIBO BE 1.1 RTF report. Changes include deprecation of the SoleProprietorship class and making it equivalent to the class with the same name in the Sole Proprietorships ontology. This version also introduces a new FunctionalEntity class, as the parent of FunctionalBusinessEntity in this ontology and as the parent of Government in the GovernmentEntities ontology.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20160801/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified by the FIBO 2.0 revision to address missing labels and definitions on the deprecated sole proprietorship class to match those in the equivalent class.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified to generalize certain unions where they were no longer required and eliminate an unused import.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190201/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190901/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified to eliminate duplication of concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200301/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified to revise and extend the definition of merchant, to support merchant category codes as needed for representation of credit card transactions, merge business and functional business entity and eliminate commerce and commercial activity (which are not used anywhere in FIBO), and to clean up definitions and make them ISO 704 compliant.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200901/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified to add the concept of an association.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified to address a circular definition on association.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20210201/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified to reflect the move of some organization-specific concepts from BE to FND.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20211001/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified to address text formatting hygiene issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20220801/FunctionalEntities/FunctionalEntities.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/FunctionalEntities/FunctionalEntities.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/FunctionalEntities/FunctionalEntities.rdf version of this ontology was augmented to include general definitions for syndicate and syndicate member (LOAN-169).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20241101/FunctionalEntities/FunctionalEntities.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20250301/FunctionalEntities/FunctionalEntities.rdf version of the ontology was modified to loosen various constraints to better reflect use case requirements (SEC-205).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20251001/FunctionalEntities/FunctionalEntities.rdf version of the ontology was modified to replace references to the now deprecated hasTag property in Relations with its equivalent in OMG Commons (FND-412).
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
