---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts relating to types of controlling parties. The concepts defined here are party in
      role concepts, which define the nature of some entity such as an organization or a legal person, in some role such as
      that of owning a controlling interest in the entity or of controlling that entity. These roles are defined in terms
      of the types of control enjoyed by the party, for example de facto or de jure control. An important feature of this
      ontology is the distinction between the holding of a controlling interest (such as voting shares), and the de facto
      existence of control of one body by another as asserted in company filings or as a conclusion drawn from computational
      analysis of controlling interests.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2025 EDM Council, Inc.\n\t\tCopyright (c) 2013-2025 Object Management Group, Inc.\n\t\t\n\t\
      \tPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation\
      \ files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use,\
      \ copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to\
      \ whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this\
      \ permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED\
      \ 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Control Parties Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/OwnershipAndControl/ControlParties.rdf version of this
      ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/OwnershipAndControl/ControlParties.rdf version of this
      ontology was modified per the FIBO 2.0 RFC to add missing labels and definitions, eliminate references to BusinessFacingTypes,
      etc.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/OwnershipAndControl/ControlParties.rdf version of this
      ontology was modified as a part of a simplification strategy for the organizational class hierarchy and to correct reasoning
      anomalies.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190101/OwnershipAndControl/ControlParties.rdf version of this
      ontology was modified to eliminate duplication of concepts with LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200201/OwnershipAndControl/ControlParties.rdf version of this
      ontology was modified to integrate the concept of a situation, situational roles, and corresponding relations with the
      definition of control and eliminate an unused and logically inconsistent property.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200601/OwnershipAndControl/ControlParties.rdf version of the
      ontology was modified to simplify control concepts and relations, eliminate ambiguity in definitions, restate definitions
      to be ISO 704 compliant, and add properties relating control parties to control situations.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/OwnershipAndControl/ControlParties.rdf version of the
      ontology was modified to correct the label on hasControllingOrganizationMember and reflect the move of OrganizationMember
      from Parties to Organizations in FND, and to incorporate the latest insights into how control relations should integrate
      with the control situation.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/OwnershipAndControl/ControlParties.rdf version of the
      ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/OwnershipAndControl/ControlParties.rdf version of the
      ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/OwnershipAndControl/ControlParties.rdf version of the
      ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20250301/OwnershipAndControl/ControlParties/
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/Law/LegalCore.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/
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
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: Control Parties Ontology
type: Ontology Definition
---

# Control Parties Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/>

## Relationships

- **Related to**: [OwnershipParties](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [LegalCore](/concepts/fibo/FND/Law/LegalCore.md)
- **Related to**: [FormalOrganizations](/concepts/fibo/FND/Organizations/FormalOrganizations.md)
- **Related to**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [ControlParties](<https://spec.edmcouncil.org/fibo/ontology/BE/20250301/OwnershipAndControl/ControlParties/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts relating to types of controlling parties. The concepts defined here are party in role concepts, which define the nature of some entity such as an organization or a legal person, in some role such as that of owning a controlling interest in the entity or of controlling that entity. These roles are defined in terms of the types of control enjoyed by the party, for example de facto or de jure control. An important feature of this ontology is the distinction between the holding of a controlling interest (such as voting shares), and the de facto existence of control of one body by another as asserted in company filings or as a conclusion drawn from computational analysis of controlling interests.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. 		Copyright (c) 2013-2025 Object Management Group, Inc. 		 		Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Control Parties Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/OwnershipAndControl/ControlParties.rdf version of this ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/OwnershipAndControl/ControlParties.rdf version of this ontology was modified per the FIBO 2.0 RFC to add missing labels and definitions, eliminate references to BusinessFacingTypes, etc.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/OwnershipAndControl/ControlParties.rdf version of this ontology was modified as a part of a simplification strategy for the organizational class hierarchy and to correct reasoning anomalies.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190101/OwnershipAndControl/ControlParties.rdf version of this ontology was modified to eliminate duplication of concepts with LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200201/OwnershipAndControl/ControlParties.rdf version of this ontology was modified to integrate the concept of a situation, situational roles, and corresponding relations with the definition of control and eliminate an unused and logically inconsistent property.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200601/OwnershipAndControl/ControlParties.rdf version of the ontology was modified to simplify control concepts and relations, eliminate ambiguity in definitions, restate definitions to be ISO 704 compliant, and add properties relating control parties to control situations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/OwnershipAndControl/ControlParties.rdf version of the ontology was modified to correct the label on hasControllingOrganizationMember and reflect the move of OrganizationMember from Parties to Organizations in FND, and to incorporate the latest insights into how control relations should integrate with the control situation.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/OwnershipAndControl/ControlParties.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/OwnershipAndControl/ControlParties.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/OwnershipAndControl/ControlParties.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
