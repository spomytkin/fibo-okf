---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: option holder
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that owns an option
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In a call, the option holder has the right, but not the obligation, to buy the underlying asset, while, in a put,
      the option holder has the right to sell the underlying asset. An option holder may sell the option contract itself,
      at which point the buyer becomes the option holder. Once the instrument is exercised there are typically additional,
      relevant obligations with regard to settlement.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/holds
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Owner
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionHolder
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: option holder
type: Ontology Class
---

# option holder

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionHolder>

## Definition

party that owns an option

## Relationships

- **Subclass of**: [Owner](/concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md)

## Constraints

- **[holds](/concepts/fibo/FND/Relations/Relations/holds.md)**: some values from of type [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)

## Annotations

- **label** (en): option holder
- **definition** (en): party that owns an option
- **explanatoryNote** (en): In a call, the option holder has the right, but not the obligation, to buy the underlying asset, while, in a put, the option holder has the right to sell the underlying asset. An option holder may sell the option contract itself, at which point the buyer becomes the option holder. Once the instrument is exercised there are typically additional, relevant obligations with regard to settlement.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
