---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines partnerships and related concepts. The concepts distinguish general from limited partners,
      as well as the types of equity that they hold. Included are abstract definitions of partnership types based on whether
      they have general, limited or both kinds of partners. Both legally incorporated and non incorporated forms of partnerships
      are covered.
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
    value: Partnerships Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/Partnerships/Partnerships.rdf version of this ontology
      was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/Partnerships/Partnerships.rdf version of this ontology
      was modified per the FIBO 2.0 RFC to reference shareholders' equity vs. stockholders' equity and correct a number of
      restrictions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/Partnerships/Partnerships.rdf version of this ontology
      was modified to simplify / merge the legal person and formal organization class hierarchies.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20181101/Partnerships/Partnerships.rdf version of this ontology
      was modified to reflect the move of hasObjective to FND to enable higher level reuse.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190401/Partnerships/Partnerships.rdf version of this ontology
      was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190901/Partnerships/Partnerships.rdf version of this ontology
      was modified to eliminate duplication with concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200201/Partnerships/Partnerships.rdf version of this ontology
      was restructured to simplify the overall structure of partnerships, eliminate kinds of partnerships that do not exist,
      simplify the concept of a partnership agreement, loosen or eliminate restrictions as appropriate, add common forms of
      partnership that were missing, and revise definitions to be ISO 704 compliant.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200601/Partnerships/Partnerships.rdf version of this ontology
      was modified to reflect the move of OrganizationMember from Parties to Organizations in FND.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/Partnerships/Partnerships.rdf version of this ontology
      was modified to fix spelling errors.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20211201/Partnerships/Partnerships.rdf version of this ontology
      was modified to address text formatting hygiene issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20220801/Partnerships/Partnerships.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/Partnerships/Partnerships.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC),
      eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/Partnerships/Partnerships.rdf version of this ontology
      was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/Partnerships/Partnerships.rdf version of the ontology
      was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2
      (FND-389).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20250301/Partnerships/Partnerships/
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/
  - concept: /concepts/fibo/FND/Law/LegalCapacity.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/
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
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: Partnerships Ontology
type: Ontology Definition
---

# Partnerships Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/>

## Relationships

- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [LegalPersons](/concepts/fibo/BE/LegalEntities/LegalPersons.md)
- **Related to**: [ControlParties](/concepts/fibo/BE/OwnershipAndControl/ControlParties.md)
- **Related to**: [OwnershipParties](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [Partnerships](<https://spec.edmcouncil.org/fibo/ontology/BE/20250301/Partnerships/Partnerships/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines partnerships and related concepts. The concepts distinguish general from limited partners, as well as the types of equity that they hold. Included are abstract definitions of partnership types based on whether they have general, limited or both kinds of partners. Both legally incorporated and non incorporated forms of partnerships are covered.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Partnerships Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/Partnerships/Partnerships.rdf version of this ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/Partnerships/Partnerships.rdf version of this ontology was modified per the FIBO 2.0 RFC to reference shareholders' equity vs. stockholders' equity and correct a number of restrictions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/Partnerships/Partnerships.rdf version of this ontology was modified to simplify / merge the legal person and formal organization class hierarchies.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20181101/Partnerships/Partnerships.rdf version of this ontology was modified to reflect the move of hasObjective to FND to enable higher level reuse.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190401/Partnerships/Partnerships.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190901/Partnerships/Partnerships.rdf version of this ontology was modified to eliminate duplication with concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200201/Partnerships/Partnerships.rdf version of this ontology was restructured to simplify the overall structure of partnerships, eliminate kinds of partnerships that do not exist, simplify the concept of a partnership agreement, loosen or eliminate restrictions as appropriate, add common forms of partnership that were missing, and revise definitions to be ISO 704 compliant.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200601/Partnerships/Partnerships.rdf version of this ontology was modified to reflect the move of OrganizationMember from Parties to Organizations in FND.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/Partnerships/Partnerships.rdf version of this ontology was modified to fix spelling errors.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20211201/Partnerships/Partnerships.rdf version of this ontology was modified to address text formatting hygiene issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20220801/Partnerships/Partnerships.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/Partnerships/Partnerships.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/Partnerships/Partnerships.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/Partnerships/Partnerships.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
