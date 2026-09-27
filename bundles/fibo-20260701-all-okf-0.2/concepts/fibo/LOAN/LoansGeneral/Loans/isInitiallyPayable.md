---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is initially payable
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the obligation arising from the covered loan was, or in the case of an application, would have
      been initially payable to the financial institution
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/isInitiallyPayable
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: is initially payable
type: Ontology Property
---

# is initially payable

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/isInitiallyPayable>

## Definition

indicates whether the obligation arising from the covered loan was, or in the case of an application, would have been initially payable to the financial institution

## Relationships

- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is initially payable
- **definition** (en): indicates whether the obligation arising from the covered loan was, or in the case of an application, would have been initially payable to the financial institution

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
