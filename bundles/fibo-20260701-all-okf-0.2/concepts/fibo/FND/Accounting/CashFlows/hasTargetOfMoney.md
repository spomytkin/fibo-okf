---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has target of funds
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: refers to the sink for some amount of money
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Documents/refersTo
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/hasTargetOfMoney
sources:
- id: fibo-source-11f30e320a
  resource: references/fibo/FND/Accounting/CashFlows.rdf
  sha256: 11f30e320a47607eb0377d4c97d55d7f8607ad5ba323af00057df476c78573e2
  title: FIBO source FND/Accounting/CashFlows.rdf
title: has target of funds
type: Ontology Property
---

# has target of funds

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/hasTargetOfMoney>

## Definition

refers to the sink for some amount of money

## Relationships

- **Subproperty of**: [refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)

## Annotations

- **label**: has target of funds
- **definition**: refers to the sink for some amount of money

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
