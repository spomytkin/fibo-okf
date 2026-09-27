---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines the fundamental concepts for representing private limited companies -- i.e., companies that
      have characteristics of corporations and of partnerships but are neither.
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
    value: Private Limited Companies Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version
      of this ontology was modified per the FIBO 2.0 RFC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version
      of this ontology was modified to simplify / merge the legal person and formal organization class hierarchies, and add
      limited liability company, limited liability company taxed as a corporation, managing member, and private limited company.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version
      of this ontology was modified to eliminate a smart quote in an explanatory note on manager-managed limited liability
      company, and to reflect the move of OrganizationMember from Parties to Organizations in FND
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version
      of this ontology was modified to fix spelling errors.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20211201/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version
      of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230201/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version
      of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version
      of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons)
      v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version
      of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library
      (Commons) v1.2 (FND-389).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20250301/PrivateLimitedCompanies/PrivateLimitedCompanies/
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/
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
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/
sources:
- id: fibo-source-ed254b1923
  resource: references/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
  sha256: ed254b1923d2aaa91861926940b56bbacc941588b902d6479417e85b06987c0d
  title: FIBO source BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
title: Private Limited Companies Ontology
type: Ontology Definition
---

# Private Limited Companies Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/>

## Relationships

- **Related to**: [LegalPersons](/concepts/fibo/BE/LegalEntities/LegalPersons.md)
- **Related to**: [ControlParties](/concepts/fibo/BE/OwnershipAndControl/ControlParties.md)
- **Related to**: [Executives](/concepts/fibo/BE/OwnershipAndControl/Executives.md)
- **Related to**: [OwnershipParties](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [PrivateLimitedCompanies](<https://spec.edmcouncil.org/fibo/ontology/BE/20250301/PrivateLimitedCompanies/PrivateLimitedCompanies/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines the fundamental concepts for representing private limited companies -- i.e., companies that have characteristics of corporations and of partnerships but are neither.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. 		Copyright (c) 2013-2025 Object Management Group, Inc. 		 		Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Private Limited Companies Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version of this ontology was modified per the FIBO 2.0 RFC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version of this ontology was modified to simplify / merge the legal person and formal organization class hierarchies, and add limited liability company, limited liability company taxed as a corporation, managing member, and private limited company.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version of this ontology was modified to eliminate a smart quote in an explanatory note on manager-managed limited liability company, and to reflect the move of OrganizationMember from Parties to Organizations in FND
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version of this ontology was modified to fix spelling errors.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20211201/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230201/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **copyright**: Copyright (c) 2016-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2016-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
