---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit index
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: reference index that is a function of credit events that change the value of an underlying portfolio
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Such an index does not necessarily reference a static portfolio, as there may be provisions for replacing defaulted
      securities on which the index depends.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/BasketOfCreditRisks
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices/ReferenceIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/ReferenceIndex
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CreditIndex
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: credit index
type: Ontology Class
---

# credit index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CreditIndex>

## Definition

reference index that is a function of credit events that change the value of an underlying portfolio

## Relationships

- **Subclass of**: [ReferenceIndex](/concepts/fibo/IND/MarketIndices/BasketIndices/ReferenceIndex.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [BasketOfCreditRisks](/concepts/fibo/IND/MarketIndices/BasketIndices/BasketOfCreditRisks.md)

## Annotations

- **label** (en): credit index
- **definition** (en): reference index that is a function of credit events that change the value of an underlying portfolio
- **explanatoryNote** (en): Such an index does not necessarily reference a static portfolio, as there may be provisions for replacing defaulted securities on which the index depends.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
