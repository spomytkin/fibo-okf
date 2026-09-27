---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: "This ontology specifies indiividuals that represent well-known swaps repositories and intermediaries. Related\
      \ definitions for the corresponding legal entities can be found in the FBC Commercial Registration Authorities ontology.\
      \ \n\t\t\nNote that this ontology is not intended to be exhaustive, but is designed for expansion as FIBO use cases\
      \ or user requirements dictate."
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2018-2025 Object Management Group,\
      \ Inc.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\t\
      See https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Swaps Individuals Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20200301/DerivativesContracts/SwapsIndividuals.rdf version of
      this ontology was revised to replace uses of hasTag in Relations with hasTag from LCC, as the more complex union of
      datatypes in the Relations concept is not needed here.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20200701/DerivativesContracts/SwapsIndividuals.rdf version of
      this ontology was revised to update the LEI URIs to the new form published by the GLEIF on data.world.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20201201/DerivativesContracts/SwapsIndividuals.rdf version of
      this ontology was revised to move designated contract market to the markets ontology in FBC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20201201/DerivativesContracts/SwapsIndividuals.rdf version of
      this ontology was revised to replace references to the legacy LCC UnitedStates country representation with UnitedStatesOfAmerica.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20210701/DerivativesContracts/SwapsIndividuals.rdf version of
      this ontology was revised to clean up the LEI data and individual definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20211201/DerivativesContracts/SwapsIndividuals.rdf version of
      the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20230201/DerivativesContracts/SwapsIndividuals.rdf version of
      this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20230301/DerivativesContracts/SwapsIndividuals.rdf version of
      this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1
      (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20240101/DerivativesContracts/SwapsIndividuals.rdf version of
      the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20250301/DerivativesContracts/SwapsIndividuals.rdf version of
      the ontology was modified to merge details from the old corporations ontology into corporate bodies for consistency
      and useability (BE-259).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20251201/DerivativesContracts/SwapsIndividuals.rdf version of
      the ontology was modified to reflect the migration of registration authorities to the Functional Entities module in
      FBC and better align with the GLEIF LEI model (FND-407).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/20260601/DerivativesContracts/SwapsIndividuals/
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
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
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/
sources:
- id: fibo-source-2b1a72c3a1
  resource: references/fibo/DER/DerivativesContracts/SwapsIndividuals.rdf
  sha256: 2b1a72c3a1db9285b93e97db0ac5f55555a206893741495827272209f11ad849
  title: FIBO source DER/DerivativesContracts/SwapsIndividuals.rdf
title: Swaps Individuals Ontology
type: Ontology Definition
---

# Swaps Individuals Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/SwapsIndividuals/>

## Relationships

- **Related to**: [Swaps](/concepts/fibo/DER/DerivativesContracts/Swaps.md)
- **Related to**: [CommercialRegistrationAuthorities](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [Markets](/concepts/fibo/FBC/FunctionalEntities/Markets.md)
- **Related to**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [RegistrationAuthorities](<https://www.omg.org/spec/Commons/RegistrationAuthorities/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [SwapsIndividuals](<https://spec.edmcouncil.org/fibo/ontology/DER/20260601/DerivativesContracts/SwapsIndividuals/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology specifies indiividuals that represent well-known swaps repositories and intermediaries. Related definitions for the corresponding legal entities can be found in the FBC Commercial Registration Authorities ontology.  		 Note that this ontology is not intended to be exhaustive, but is designed for expansion as FIBO use cases or user requirements dictate.
- **license**: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2018-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Swaps Individuals Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20200301/DerivativesContracts/SwapsIndividuals.rdf version of this ontology was revised to replace uses of hasTag in Relations with hasTag from LCC, as the more complex union of datatypes in the Relations concept is not needed here.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20200701/DerivativesContracts/SwapsIndividuals.rdf version of this ontology was revised to update the LEI URIs to the new form published by the GLEIF on data.world.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20201201/DerivativesContracts/SwapsIndividuals.rdf version of this ontology was revised to move designated contract market to the markets ontology in FBC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20201201/DerivativesContracts/SwapsIndividuals.rdf version of this ontology was revised to replace references to the legacy LCC UnitedStates country representation with UnitedStatesOfAmerica.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20210701/DerivativesContracts/SwapsIndividuals.rdf version of this ontology was revised to clean up the LEI data and individual definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20211201/DerivativesContracts/SwapsIndividuals.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20230201/DerivativesContracts/SwapsIndividuals.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20230301/DerivativesContracts/SwapsIndividuals.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20240101/DerivativesContracts/SwapsIndividuals.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20250301/DerivativesContracts/SwapsIndividuals.rdf version of the ontology was modified to merge details from the old corporations ontology into corporate bodies for consistency and useability (BE-259).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20251201/DerivativesContracts/SwapsIndividuals.rdf version of the ontology was modified to reflect the migration of registration authorities to the Functional Entities module in FBC and better align with the GLEIF LEI model (FND-407).
- **copyright**: Copyright (c) 2018-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
