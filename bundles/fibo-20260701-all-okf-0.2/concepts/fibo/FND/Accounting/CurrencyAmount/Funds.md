---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: funds
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: artificial currency used as calculation basis for another currency(s) and accounting purposes
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: Codes for the representation of currencies and funds, ISO 4217, Eighth edition, 2015-08-01, section 3.3
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Funds
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: funds
type: Ontology Class
---

# funds

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Funds>

## Definition

artificial currency used as calculation basis for another currency(s) and accounting purposes

## Relationships

- **Subclass of**: [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Constraints

- **[hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Annotations

- **label**: funds
- **definition**: artificial currency used as calculation basis for another currency(s) and accounting purposes
- **definitionOrigin**: Codes for the representation of currencies and funds, ISO 4217, Eighth edition, 2015-08-01, section 3.3

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
