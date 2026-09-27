---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: collar
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option trading strategy that involves buying a downside put and selling an upside call that is implemented to protect
      against large losses, but which also limits large upside gains
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CallOption
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/PutOption
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionTradingStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Collar
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: collar
type: Ontology Class
---

# collar

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Collar>

## Definition

option trading strategy that involves buying a downside put and selling an upside call that is implemented to protect against large losses, but which also limits large upside gains

## Relationships

- **Subclass of**: [OptionTradingStrategy](/concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [CallOption](/concepts/fibo/DER/DerivativesContracts/Options/CallOption.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [PutOption](/concepts/fibo/DER/DerivativesContracts/Options/PutOption.md)

## Annotations

- **label** (en): collar
- **definition** (en): option trading strategy that involves buying a downside put and selling an upside call that is implemented to protect against large losses, but which also limits large upside gains

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
