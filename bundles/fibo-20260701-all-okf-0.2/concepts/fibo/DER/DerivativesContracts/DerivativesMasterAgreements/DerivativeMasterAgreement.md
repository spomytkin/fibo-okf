---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: derivative master agreement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: master agreement covering derivatives transactions to be carried out between the parties to this contract
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'Related to conditions precedent that may apply: "Each obligation of each party under Section 2(a)(i) is subject
      to (1) the condition precedent that no Event of Default or Potential Event of Default with respect to the other party
      has occurred and is continuing, (2) the condition precedent that no Early Termination Date in respect of the relevant
      Transaction has occurred or been effectively designated and (3) each other applicable condition precedent specified
      in this Agreement. " In the above, the Obligations defined under Section 2(a)(i) of the Master Agrement is the obligation
      to make each payment or delivery defined in a Confirmation for a transaction carried out under this Master Agreement.'
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'Sample preamble to one of these: "EXAMPLE BANK, a Michigan banking corporation and SAMPLECOMPANY US, INC. a Delaware
      corporation have entered and/or anticipate entering into one or more transactions (each a "Transaction") that are or
      will be governed by this Master Agreement, which includes the schedule (the "Schedule"), and the documents and other
      confirming evidence (each a "Confirmation") exchanged between the parties confirming those Transactions. "'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The ISDA Master Agreement (Multicurrency-Cross Border version published in 1992) enables trading counterparties
      to include foreign exchange transactions under a global cross-product close-out netting master agreement. Because there
      are significant differences in market practices between the derivatives markets and the international foreign exchange
      spot and forward markets, parties to the ISDA frequently incorporate the ISDA FX and Currency Options Definitions and
      further tailor the ISDA Schedule to reflect standard market practice for the foreign exchange products.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
  - concept: /concepts/fibo/FND/Agreements/Contracts/MasterAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MasterAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesMasterAgreements/DerivativeMasterAgreement
sources:
- id: fibo-source-d9f057f57c
  resource: references/fibo/DER/DerivativesContracts/DerivativesMasterAgreements.rdf
  sha256: d9f057f57c2fbab0f06a73b8281b7d476e79c36502bb7a47cc8b00f51ec459d2
  title: FIBO source DER/DerivativesContracts/DerivativesMasterAgreements.rdf
title: derivative master agreement
type: Ontology Class
---

# derivative master agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesMasterAgreements/DerivativeMasterAgreement>

## Definition

master agreement covering derivatives transactions to be carried out between the parties to this contract

## Relationships

- **Subclass of**: [CreditAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md)
- **Subclass of**: [MasterAgreement](/concepts/fibo/FND/Agreements/Contracts/MasterAgreement.md)

## Annotations

- **label** (en): derivative master agreement
- **definition** (en): master agreement covering derivatives transactions to be carried out between the parties to this contract
- **example** (en): Related to conditions precedent that may apply: "Each obligation of each party under Section 2(a)(i) is subject to (1) the condition precedent that no Event of Default or Potential Event of Default with respect to the other party has occurred and is continuing, (2) the condition precedent that no Early Termination Date in respect of the relevant Transaction has occurred or been effectively designated and (3) each other applicable condition precedent specified in this Agreement. " In the above, the Obligations defined under Section 2(a)(i) of the Master Agrement is the obligation to make each payment or delivery defined in a Confirmation for a transaction carried out under this Master Agreement.
- **example** (en): Sample preamble to one of these: "EXAMPLE BANK, a Michigan banking corporation and SAMPLECOMPANY US, INC. a Delaware corporation have entered and/or anticipate entering into one or more transactions (each a "Transaction") that are or will be governed by this Master Agreement, which includes the schedule (the "Schedule"), and the documents and other confirming evidence (each a "Confirmation") exchanged between the parties confirming those Transactions. "
- **explanatoryNote** (en): The ISDA Master Agreement (Multicurrency-Cross Border version published in 1992) enables trading counterparties to include foreign exchange transactions under a global cross-product close-out netting master agreement. Because there are significant differences in market practices between the derivatives markets and the international foreign exchange spot and forward markets, parties to the ISDA frequently incorporate the ISDA FX and Currency Options Definitions and further tailor the ISDA Schedule to reflect standard market practice for the foreign exchange products.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
