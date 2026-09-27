---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest-only strip
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a strip that represents the non-principal portion of the monthly payments on the underlying debt instrument, such
      as a bond
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: An interest-only strip can be reintegrated into other synthetic or engineered products. For example, interest-only
      strips can be pooled to create or make up a portion of a larger collateralized mortgage obligation (CMO), asset-backed
      security (ABS) or collateralized debt obligation (CDO) structure.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An interest-only strip holder is interested in rising rates and no prepayment, as prepayment would cause them forfeit
      future interest payments and receive nothing from the return of the principal.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: IO strip
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/Strip.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/Strip
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/InterestOnlyStrip
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: interest-only strip
type: Ontology Class
---

# interest-only strip

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/InterestOnlyStrip>

## Definition

a strip that represents the non-principal portion of the monthly payments on the underlying debt instrument, such as a bond

## Relationships

- **Subclass of**: [Strip](/concepts/fibo/SEC/Debt/DebtInstruments/Strip.md)

## Annotations

- **label** (en): interest-only strip
- **definition** (en): a strip that represents the non-principal portion of the monthly payments on the underlying debt instrument, such as a bond
- **example**: An interest-only strip can be reintegrated into other synthetic or engineered products. For example, interest-only strips can be pooled to create or make up a portion of a larger collateralized mortgage obligation (CMO), asset-backed security (ABS) or collateralized debt obligation (CDO) structure.
- **explanatoryNote**: An interest-only strip holder is interested in rising rates and no prepayment, as prepayment would cause them forfeit future interest payments and receive nothing from the return of the principal.
- **synonym** (en): IO strip

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
