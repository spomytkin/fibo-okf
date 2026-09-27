---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: partial redemption allocation convention
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: convention used to determine how the partial call will be actioned with respect to bond selection
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasRateValue
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/Convention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/Convention
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PartialRedemptionAllocationConvention
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: partial redemption allocation convention
type: Ontology Class
---

# partial redemption allocation convention

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PartialRedemptionAllocationConvention>

## Definition

convention used to determine how the partial call will be actioned with respect to bond selection

## Relationships

- **Subclass of**: [Convention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/Convention.md)

## Constraints

- **[hasRateValue](/concepts/fibo/FND/Accounting/CurrencyAmount/hasRateValue.md)**: max qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: partial redemption allocation convention
- **definition**: convention used to determine how the partial call will be actioned with respect to bond selection

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
