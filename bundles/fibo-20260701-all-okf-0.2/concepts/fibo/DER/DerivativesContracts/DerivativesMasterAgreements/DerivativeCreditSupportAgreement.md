---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: derivative credit support agreement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: addendum to the master agreement that governs the exchange of collateral between parties in derivatives transactions
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that in the case of a derivative credit support agreement, the beneficiary actually holds the collateral and
      has the right to ask for additional collateral if its value falls below the threshold agreed upon per the agreement.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesMasterAgreements/DerivativeMasterAgreement
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isSubordinateTo
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditEnhancementAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditEnhancementAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesMasterAgreements/DerivativeCreditSupportAgreement
sources:
- id: fibo-source-d9f057f57c
  resource: references/fibo/DER/DerivativesContracts/DerivativesMasterAgreements.rdf
  sha256: d9f057f57c2fbab0f06a73b8281b7d476e79c36502bb7a47cc8b00f51ec459d2
  title: FIBO source DER/DerivativesContracts/DerivativesMasterAgreements.rdf
title: derivative credit support agreement
type: Ontology Class
---

# derivative credit support agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesMasterAgreements/DerivativeCreditSupportAgreement>

## Definition

addendum to the master agreement that governs the exchange of collateral between parties in derivatives transactions

## Relationships

- **Subclass of**: [CreditEnhancementAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditEnhancementAgreement.md)

## Constraints

- **[isSubordinateTo](/concepts/fibo/FND/Agreements/Contracts/isSubordinateTo.md)**: exact qualified cardinality 1 of type [DerivativeMasterAgreement](/concepts/fibo/DER/DerivativesContracts/DerivativesMasterAgreements/DerivativeMasterAgreement.md)

## Annotations

- **label** (en): derivative credit support agreement
- **definition** (en): addendum to the master agreement that governs the exchange of collateral between parties in derivatives transactions
- **explanatoryNote** (en): Note that in the case of a derivative credit support agreement, the beneficiary actually holds the collateral and has the right to ask for additional collateral if its value falls below the threshold agreed upon per the agreement.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
