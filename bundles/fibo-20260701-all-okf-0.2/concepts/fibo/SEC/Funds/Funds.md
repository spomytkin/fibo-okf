---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines fundamental concepts about funds and collective investment vehicles (CIVs).
  - predicate: http://purl.org/dc/terms/contributor
    value: Federated Knowledge, LLC
  - predicate: http://purl.org/dc/terms/contributor
    value: ProBanker Simulations, LLC
  - predicate: http://purl.org/dc/terms/contributor
    value: Thematix Partners LLC
  - predicate: http://purl.org/dc/terms/contributor
    value: Wells Fargo Bank, N.A.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2018-2025 Object Management Group\n\
      \nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation\
      \ files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use,\
      \ copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to\
      \ whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this\
      \ permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED\
      \ 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\n\t\tSee https://opensource.org/licenses/MIT."
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Funds Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20201201/Funds/Funds.rdf version of this ontology was modified
      to replace the original fibo-sec-fnd-fnd prefix with fibo-sec-fund-fund for the sake of clarity and to change the restriction
      on LegalFundStructure from an equivalence to a subclass relationship to address a reasoning error as well as adding
      a missing restriction on jurisdiction.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210501/Funds/Funds.rdf version of this ontology was modified
      to move the definition of SpecialPurposeVehicle to the Pools ontology to make it available for use more generally.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220101/Funds/Funds.rdf version of this ontology was modified
      to eliminate a deprecated element for SpecialPurposeVehicle, which was moved to Pools last quarter.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220501/Funds/Funds.rdf version of this ontology was modified
      to address text formatting hygiene issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220801/Funds/Funds.rdf version of the ontology was modified
      to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Funds/Funds.rdf version of this ontology was modified
      to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating
      redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Funds/Funds.rdf version of this ontology was modified
      to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389), and
      to add the notion of a private credit fund and adjust inconsistencies in private equity fund (SEC-203).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250301/Funds/Funds.rdf version of this ontology was modified
      to broaden the definition of fund unit (SEC-200) and add certain private fund details (SEC-208).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250901/Funds/Funds.rdf version of this ontology was modified
      to add fund-specific roles and unitized funds (SEC-213).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20251201/Funds/Funds.rdf version of this ontology was modified
      to eliminate an erroneous abbreviation (SEC-216).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20260401/Funds/Funds.rdf version of this ontology was modified
      to reflect migration of concepts from accounting equity to ownership in FND (FND-409).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 Object Management Group
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2026 EDm Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/
  - concept: /concepts/fibo/BE/Trusts/Trusts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/
  - concept: /concepts/fibo/FND/Law/LegalCapacity.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/
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
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/20260401/Funds/Funds/
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/
  - concept: /concepts/fibo/SEC/Securities/Pools.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Locations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: Funds Ontology
type: Ontology Definition
---

# Funds Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/>

## Relationships

- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [CorporateOwnership](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md)
- **Related to**: [Trusts](/concepts/fibo/BE/Trusts/Trusts.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [EquityInstruments](/concepts/fibo/SEC/Equities/EquityInstruments.md)
- **Related to**: [Pools](/concepts/fibo/SEC/Securities/Pools.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [Funds](<https://spec.edmcouncil.org/fibo/ontology/SEC/20260401/Funds/Funds/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines fundamental concepts about funds and collective investment vehicles (CIVs).
- **contributor**: Federated Knowledge, LLC
- **contributor**: ProBanker Simulations, LLC
- **contributor**: Thematix Partners LLC
- **contributor**: Wells Fargo Bank, N.A.
- **license**: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2018-2025 Object Management Group  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  		See https://opensource.org/licenses/MIT.
- **label** (en): Funds Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20201201/Funds/Funds.rdf version of this ontology was modified to replace the original fibo-sec-fnd-fnd prefix with fibo-sec-fund-fund for the sake of clarity and to change the restriction on LegalFundStructure from an equivalence to a subclass relationship to address a reasoning error as well as adding a missing restriction on jurisdiction.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210501/Funds/Funds.rdf version of this ontology was modified to move the definition of SpecialPurposeVehicle to the Pools ontology to make it available for use more generally.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220101/Funds/Funds.rdf version of this ontology was modified to eliminate a deprecated element for SpecialPurposeVehicle, which was moved to Pools last quarter.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220501/Funds/Funds.rdf version of this ontology was modified to address text formatting hygiene issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220801/Funds/Funds.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Funds/Funds.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Funds/Funds.rdf version of this ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389), and to add the notion of a private credit fund and adjust inconsistencies in private equity fund (SEC-203).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250301/Funds/Funds.rdf version of this ontology was modified to broaden the definition of fund unit (SEC-200) and add certain private fund details (SEC-208).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250901/Funds/Funds.rdf version of this ontology was modified to add fund-specific roles and unitized funds (SEC-213).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20251201/Funds/Funds.rdf version of this ontology was modified to eliminate an erroneous abbreviation (SEC-216).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20260401/Funds/Funds.rdf version of this ontology was modified to reflect migration of concepts from accounting equity to ownership in FND (FND-409).
- **copyright**: Copyright (c) 2018-2025 Object Management Group
- **copyright**: Copyright (c) 2018-2026 EDm Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
