---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is interest only
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the contractual terms include or would have included interest only payments
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/isInterestOnly
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: is interest only
type: Ontology Property
---

# is interest only

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/isInterestOnly>

## Definition

indicates whether the contractual terms include or would have included interest only payments

## Relationships

- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is interest only
- **definition** (en): indicates whether the contractual terms include or would have included interest only payments

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
