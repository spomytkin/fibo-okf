---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: Depositary receipts are certificates which represent ownership of some underlying security. They are issued by
      a bank and give the holder the ability to participate in the returns on an instrument that they may not be able to hold
      directly.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: http://opensource.org/licenses/MIT
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Depositary Receipts
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/20221001/Equities/DepositaryReceipts.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210501/Equities/DepositaryReceipts.rdf version of this ontology
      was modified to expand the definition of a depositary receipt to cover a broader range of securities.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20211101/Equities/DepositaryReceipts.rdf version of this ontology
      was modified to further refine the definition of a depositary receipt, add participatory notes, and broaden explanatory
      notes to allow for coverage of Chinese ADRs.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220101/Equities/DepositaryReceipts.rdf version of this ontology
      was modified to address text formatting hygiene issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220801/Equities/DepositaryReceipts.rdf version of this ontology
      was modified to add the concept of a Chinese depositary receipt.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Equities/DepositaryReceipts.rdf version of this ontology
      was modified to move the property, 'is conferred on' to the Legal Capacity ontology and to use the Commons Ontology
      Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/2023020120230301/Equities/DepositaryReceipts.rdf version of this
      ontology was modified to address a deprecated term that was replaced with a new term over 6 months ago (FND-386) and
      eliminate punning issues (LOAN-169).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2024 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2024 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/EasternAsiaGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/EasternAsiaGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/SouthernAsiaGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/AsianJurisdiction/SouthernAsiaGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/WesternEuropeGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/EuropeanJurisdiction/WesternEuropeGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Equities/DepositaryReceipts/
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/
  - concept: /concepts/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesClassification.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesRestrictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: Depositary Receipts
type: Ontology Definition
---

# Depositary Receipts

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/>

## Relationships

- **Related to**: [EasternAsiaGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/EasternAsiaGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [SouthernAsiaGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/AsianJurisdiction/SouthernAsiaGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [EUGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/EUGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [WesternEuropeGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/EuropeanJurisdiction/WesternEuropeGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [USGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [DebtInstruments](/concepts/fibo/SEC/Debt/DebtInstruments.md)
- **Related to**: [EquityInstruments](/concepts/fibo/SEC/Equities/EquityInstruments.md)
- **Related to**: [USSecuritiesRestrictions](/concepts/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.md)
- **Related to**: [SecuritiesClassification](/concepts/fibo/SEC/Securities/SecuritiesClassification.md)
- **Related to**: [SecuritiesRestrictions](/concepts/fibo/SEC/Securities/SecuritiesRestrictions.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [DepositaryReceipts](<https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Equities/DepositaryReceipts/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: Depositary receipts are certificates which represent ownership of some underlying security. They are issued by a bank and give the holder the ability to participate in the returns on an instrument that they may not be able to hold directly.
- **license**: http://opensource.org/licenses/MIT
- **label** (en): Depositary Receipts
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/20221001/Equities/DepositaryReceipts.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210501/Equities/DepositaryReceipts.rdf version of this ontology was modified to expand the definition of a depositary receipt to cover a broader range of securities.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20211101/Equities/DepositaryReceipts.rdf version of this ontology was modified to further refine the definition of a depositary receipt, add participatory notes, and broaden explanatory notes to allow for coverage of Chinese ADRs.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220101/Equities/DepositaryReceipts.rdf version of this ontology was modified to address text formatting hygiene issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220801/Equities/DepositaryReceipts.rdf version of this ontology was modified to add the concept of a Chinese depositary receipt.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Equities/DepositaryReceipts.rdf version of this ontology was modified to move the property, 'is conferred on' to the Legal Capacity ontology and to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/2023020120230301/Equities/DepositaryReceipts.rdf version of this ontology was modified to address a deprecated term that was replaced with a new term over 6 months ago (FND-386) and eliminate punning issues (LOAN-169).
- **copyright**: Copyright (c) 2013-2024 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2024 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
