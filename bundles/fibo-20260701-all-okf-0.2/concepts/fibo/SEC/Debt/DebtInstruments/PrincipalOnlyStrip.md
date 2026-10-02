---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: principal-only strip
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a strip that represents the principal portion of the monthly payments on the underlying debt instrument, such as
      a bond
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/InterestOnlyStrip.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/InterestOnlyStrip
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/Strip.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/Strip
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PrincipalOnlyStrip
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: principal-only strip
type: Ontology Class
---

# principal-only strip

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PrincipalOnlyStrip>

## Definition

a strip that represents the principal portion of the monthly payments on the underlying debt instrument, such as a bond

## Relationships

- **Subclass of**: [Strip](/concepts/fibo/SEC/Debt/DebtInstruments/Strip.md)

## Constraints

- **Disjoint with**: [InterestOnlyStrip](/concepts/fibo/SEC/Debt/DebtInstruments/InterestOnlyStrip.md)

## Annotations

- **label** (en): principal-only strip
- **definition** (en): a strip that represents the principal portion of the monthly payments on the underlying debt instrument, such as a bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
