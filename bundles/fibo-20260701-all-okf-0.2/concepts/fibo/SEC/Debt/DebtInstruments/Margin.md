---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: margin
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a variable that is added to a specified index rate to determine the fully indexed interest rate charged to a borrower
      on a credit balance
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: spread
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Variable
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/Margin
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: margin
type: Ontology Class
---

# margin

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/Margin>

## Definition

a variable that is added to a specified index rate to determine the fully indexed interest rate charged to a borrower on a credit balance

## Relationships

- **Subclass of**: [Variable](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Variable>)

## Annotations

- **label**: margin
- **definition**: a variable that is added to a specified index rate to determine the fully indexed interest rate charged to a borrower on a credit balance
- **synonym**: spread

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
