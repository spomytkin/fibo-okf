---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: purchase lot
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial asset that is a block of securities or other financial assets bought in one transaction on a given date
      at a specific price
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Buying 100 shares of Apple on Jan 10 at $150/share is one purchase lot; buying 50 more shares on Mar 15 at $160/share
      is another purchase lot.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Purchase lot is typically used as a trading term by brokers and portfolio managers to describe how holdings are
      grouped.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/consistsOfNumberOfUnits
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/FinancialAsset
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/PurchaseLot
sources:
- id: fibo-source-4d1bc90c45
  resource: references/fibo/BE/OwnershipAndControl/CorporateOwnership.rdf
  sha256: 4d1bc90c4583cdc3c4f8228a8afb505706731dd0d76b848f6678e714ee5ac147
  title: FIBO source BE/OwnershipAndControl/CorporateOwnership.rdf
title: purchase lot
type: Ontology Class
---

# purchase lot

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/PurchaseLot>

## Definition

financial asset that is a block of securities or other financial assets bought in one transaction on a given date at a specific price

## Relationships

- **Subclass of**: [FinancialAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md)

## Constraints

- **[consistsOfNumberOfUnits](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/consistsOfNumberOfUnits.md)**: exact qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: purchase lot
- **definition**: financial asset that is a block of securities or other financial assets bought in one transaction on a given date at a specific price
- **example**: Buying 100 shares of Apple on Jan 10 at $150/share is one purchase lot; buying 50 more shares on Mar 15 at $160/share is another purchase lot.
- **explanatoryNote**: Purchase lot is typically used as a trading term by brokers and portfolio managers to describe how holdings are grouped.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
