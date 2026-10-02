---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit enhancement agreement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collateral agreement that governs the exchange of collateral between parties to mitigate counterparty credit risk
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A credit enhancement agreement ensures that collateral or a guarantee is established to secure obligations under
      the agreement. Features may include specification of the kinds of collateral or guarantee that may be used together
      with the relevant valuation methods, thresholds for the value of the collateral and haircuts applied based on mitigating
      market risk, margin requirements, dispute resolution with respect to collateral valuation and margin calls, and other
      operational details related to the transfer, substitution, and return of the collateral if established or posted.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: collateralization
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: credit support agreement
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: financial collateral arrangement
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: margin arrangement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy
    value: Nb2c15054d19d48ea8f137ab5ca078249
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditEnhancementBeneficiary
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasBeneficiary
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractPrincipal
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/CollateralAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/CollateralAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditEnhancementAgreement
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
- id: fibo-source-a6bc9592ee
  resource: references/fibo/FBC/DebtAndEquities/Guaranty.rdf
  sha256: a6bc9592eeebb061e99b2dc168751d4b3612dbcc32c86c50959e17011e4247b0
  title: FIBO source FBC/DebtAndEquities/Guaranty.rdf
title: credit enhancement agreement
type: Ontology Class
---

# credit enhancement agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditEnhancementAgreement>

## Definition

collateral agreement that governs the exchange of collateral between parties to mitigate counterparty credit risk

## Relationships

- **Subclass of**: [CollateralAgreement](/concepts/fibo/FND/Agreements/Contracts/CollateralAgreement.md)

## Constraints

- **[isCollateralizedBy](/concepts/fibo/FBC/DebtAndEquities/Debt/isCollateralizedBy.md)**: some values from value `Nb2c15054d19d48ea8f137ab5ca078249`
- **[hasBeneficiary](/concepts/fibo/FND/Agreements/Contracts/hasBeneficiary.md)**: some values from of type [CreditEnhancementBeneficiary](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditEnhancementBeneficiary.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [ContractPrincipal](/concepts/fibo/FND/Agreements/Contracts/ContractPrincipal.md)

## Annotations

- **label** (en): credit enhancement agreement
- **definition** (en): collateral agreement that governs the exchange of collateral between parties to mitigate counterparty credit risk
- **explanatoryNote** (en): A credit enhancement agreement ensures that collateral or a guarantee is established to secure obligations under the agreement. Features may include specification of the kinds of collateral or guarantee that may be used together with the relevant valuation methods, thresholds for the value of the collateral and haircuts applied based on mitigating market risk, margin requirements, dispute resolution with respect to collateral valuation and margin calls, and other operational details related to the transfer, substitution, and return of the collateral if established or posted.
- **synonym** (en): collateralization
- **synonym** (en): credit support agreement
- **synonym** (en): financial collateral arrangement
- **synonym** (en): margin arrangement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
