---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts relating to corporation-specific ownership. Roles are defined in terms of the ownership
      enjoyed by the party, and are the specific examples of these concepts as they apply to companies incorporated by the
      issuance of shares.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group,\
      \ Inc.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\nSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Corporate Ownership Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/OwnershipAndControl/CorporateOwnership.rdf version of
      this ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/OwnershipAndControl/CorporateOwnership.rdf version of
      this ontology was modified per the FIBO 2.0 RFC to reference shareholders' equity in the definition of a shareholder.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/OwnershipAndControl/CorporateOwnership.rdf version of
      this ontology was modified to generalize the definition of beneficial owner rather than limiting it to shareholding
      and eliminate a duplicate restriction on shareholder.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190201/OwnershipAndControl/CorporateOwnership.rdf version of
      this ontology was modified to modify the inheritance hierarchy for beneficial owner to replace owner with controlling
      party as one of its parent classes.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200601/OwnershipAndControl/CorporateOwnership.rdf version of
      this ontology was modified to replace isEquityHeldBy with its parent, isHeldBy, eliminate redundant classes that were
      not used anywhere, and clean up a few definitions to be less ambiguous, not circular, and to conform with ISO 704.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200901/OwnershipAndControl/CorporateOwnership.rdf version of
      this ontology was revised to simplify the contract party hierarchy and add concepts related to beneficial ownership.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/OwnershipAndControl/CorporateOwnership.rdf version of
      this ontology was revised to eliminate references to external dictionary sites that no longer resolve.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20210101/OwnershipAndControl/CorporateOwnership.rdf version of
      this ontology was revised to incorporate the latest insights into how control relations should integrate with the control
      situation.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/OwnershipAndControl/CorporateOwnership.rdf version of
      the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/OwnershipAndControl/CorporateOwnership.rdf version of
      the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1
      (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/OwnershipAndControl/CorporateOwnership.rdf version of
      the ontology was modified to align the concept of beneficial ownership with the broader ownership pattern (SEC-202).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20250701/OwnershipAndControl/CorporateOwnership.rdf version of
      the ontology was modified to clarify the differences between a shareholding, purchase lot, and tax lot (SEC-200).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20250801/OwnershipAndControl/CorporateOwnership.rdf version of
      the ontology was modified to eliminate unused references (FND-411) and to reflect migration of concepts from accounting
      equity to ownership in FND (FND-409).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20260701/OwnershipAndControl/CorporateOwnership/
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
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
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/
sources:
- id: fibo-source-4d1bc90c45
  resource: references/fibo/BE/OwnershipAndControl/CorporateOwnership.rdf
  sha256: 4d1bc90c4583cdc3c4f8228a8afb505706731dd0d76b848f6678e714ee5ac147
  title: FIBO source BE/OwnershipAndControl/CorporateOwnership.rdf
title: Corporate Ownership Ontology
type: Ontology Definition
---

# Corporate Ownership Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/>

## Relationships

- **Related to**: [CorporateBodies](/concepts/fibo/BE/LegalEntities/CorporateBodies.md)
- **Related to**: [LegalPersons](/concepts/fibo/BE/LegalEntities/LegalPersons.md)
- **Related to**: [OwnershipParties](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [RegistrationAuthorities](<https://www.omg.org/spec/Commons/RegistrationAuthorities/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [CorporateOwnership](<https://spec.edmcouncil.org/fibo/ontology/BE/20260701/OwnershipAndControl/CorporateOwnership/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts relating to corporation-specific ownership. Roles are defined in terms of the ownership enjoyed by the party, and are the specific examples of these concepts as they apply to companies incorporated by the issuance of shares.
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **label**: Corporate Ownership Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/OwnershipAndControl/CorporateOwnership.rdf version of this ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/OwnershipAndControl/CorporateOwnership.rdf version of this ontology was modified per the FIBO 2.0 RFC to reference shareholders' equity in the definition of a shareholder.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/OwnershipAndControl/CorporateOwnership.rdf version of this ontology was modified to generalize the definition of beneficial owner rather than limiting it to shareholding and eliminate a duplicate restriction on shareholder.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190201/OwnershipAndControl/CorporateOwnership.rdf version of this ontology was modified to modify the inheritance hierarchy for beneficial owner to replace owner with controlling party as one of its parent classes.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200601/OwnershipAndControl/CorporateOwnership.rdf version of this ontology was modified to replace isEquityHeldBy with its parent, isHeldBy, eliminate redundant classes that were not used anywhere, and clean up a few definitions to be less ambiguous, not circular, and to conform with ISO 704.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200901/OwnershipAndControl/CorporateOwnership.rdf version of this ontology was revised to simplify the contract party hierarchy and add concepts related to beneficial ownership.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/OwnershipAndControl/CorporateOwnership.rdf version of this ontology was revised to eliminate references to external dictionary sites that no longer resolve.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20210101/OwnershipAndControl/CorporateOwnership.rdf version of this ontology was revised to incorporate the latest insights into how control relations should integrate with the control situation.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/OwnershipAndControl/CorporateOwnership.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/OwnershipAndControl/CorporateOwnership.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/OwnershipAndControl/CorporateOwnership.rdf version of the ontology was modified to align the concept of beneficial ownership with the broader ownership pattern (SEC-202).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20250701/OwnershipAndControl/CorporateOwnership.rdf version of the ontology was modified to clarify the differences between a shareholding, purchase lot, and tax lot (SEC-200).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20250801/OwnershipAndControl/CorporateOwnership.rdf version of the ontology was modified to eliminate unused references (FND-411) and to reflect migration of concepts from accounting equity to ownership in FND (FND-409).
- **copyright**: Copyright (c) 2013-2025 Object Management Group
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
