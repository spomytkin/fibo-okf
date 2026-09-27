---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has redemption terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the specific terms related to redemption as specified in the instrument or a related contract document
  range:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasRedemptionProvision
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: has redemption terms
type: Ontology Property
---

# has redemption terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasRedemptionProvision>

## Definition

indicates the specific terms related to redemption as specified in the instrument or a related contract document

## Relationships

- **Range**: [RedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- **Subproperty of**: [hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)

## Annotations

- **label**: has redemption terms
- **definition**: indicates the specific terms related to redemption as specified in the instrument or a related contract document

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
