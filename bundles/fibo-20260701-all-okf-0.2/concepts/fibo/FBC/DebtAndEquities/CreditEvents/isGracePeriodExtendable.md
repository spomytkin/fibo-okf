---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is grace period extendable
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether or not the grace period may be extended, which may be jurisdiction specific
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/isGracePeriodExtendable
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: is grace period extendable
type: Ontology Property
---

# is grace period extendable

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/isGracePeriodExtendable>

## Definition

indicates whether or not the grace period may be extended, which may be jurisdiction specific

## Relationships

- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is grace period extendable
- **definition** (en): indicates whether or not the grace period may be extended, which may be jurisdiction specific

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
