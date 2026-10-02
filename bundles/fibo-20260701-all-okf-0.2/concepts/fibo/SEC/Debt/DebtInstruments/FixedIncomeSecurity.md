---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fixed income security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: tradeable debt instrument that provides a return in the form of fixed periodic payments and typically the return
      of principal at maturity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Fixed income securities provide payments according to a regular schedule. This does not necessarily mean that the
      payments themselves are of a fixed amount, however.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FixedIncomeSecurity
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: fixed income security
type: Ontology Class
---

# fixed income security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FixedIncomeSecurity>

## Definition

tradeable debt instrument that provides a return in the form of fixed periodic payments and typically the return of principal at maturity

## Relationships

- **Subclass of**: [TradableDebtInstrument](/concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)

## Annotations

- **label**: fixed income security
- **definition**: tradeable debt instrument that provides a return in the form of fixed periodic payments and typically the return of principal at maturity
- **explanatoryNote**: Fixed income securities provide payments according to a regular schedule. This does not necessarily mean that the payments themselves are of a fixed amount, however.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
